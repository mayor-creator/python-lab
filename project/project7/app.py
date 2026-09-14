from pathlib import Path

import fastf1
import matplotlib.pyplot as plt
import pandas as pd

cache_dir = Path("./cache")
cache_dir.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(cache_dir))

session = fastf1.get_session(2026, "Madrid", "Q")
session.load()

print(f"Country: {session.event['Country']}")
print(f"Location: {session.event['Location']}")
print(f"Session Name: {session.name}")
print(f"Grand Prix: {session.event['EventName']}")

# ---------------------------------------------------------------
# 1. Split the laps into Q1 / Q2 / Q3 and grab each driver's
#    fastest lap in each segment.
# ---------------------------------------------------------------
q1_laps, q2_laps, q3_laps = session.laps.split_qualifying_sessions()


def fastest_by_driver(laps, label):
    """Return a DataFrame of each driver's best lap time in this segment."""
    if laps is None or laps.empty:
        return pd.DataFrame(columns=["Driver", label])
    idx = laps.groupby("Driver")["LapTime"].idxmin()
    best = laps.loc[idx, ["Driver", "LapTime"]].copy()
    best[label] = best["LapTime"].dt.total_seconds()
    return best[["Driver", label]]


q1_best = fastest_by_driver(q1_laps, "Q1")
q2_best = fastest_by_driver(q2_laps, "Q2")
q3_best = fastest_by_driver(q3_laps, "Q3")

# Merge all three into one table (drivers eliminated in Q1 will have
# NaN for Q2/Q3, eliminated in Q2 will have NaN for Q3).
combined = q1_best.merge(q2_best, on="Driver", how="outer").merge(
    q3_best, on="Driver", how="outer"
)

# Attach team names from the session results for coloring the plot.
team_lookup = session.results.set_index("Abbreviation")["TeamName"].to_dict()
combined["Team"] = combined["Driver"].map(team_lookup)

# ---------------------------------------------------------------
# 2. Build a simple "predicted pace" score.
#    Weighted average of whichever segments the driver ran, with
#    Q3 weighted most heavily (best indicator of ultimate pace),
#    Q1 weighted least (often includes fuel-saving/traffic laps).
# ---------------------------------------------------------------
weights = {"Q1": 1, "Q2": 2, "Q3": 3}


def weighted_pace(row):
    total, weight_sum = 0.0, 0
    for seg, w in weights.items():
        if pd.notna(row[seg]):
            total += row[seg] * w
            weight_sum += w
    return total / weight_sum if weight_sum else float("nan")


combined["PredictedPace"] = combined.apply(weighted_pace, axis=1)

# Drivers with no valid lap at all (e.g. DNS) are dropped.
combined = combined.dropna(subset=["PredictedPace"])

# Rank fastest -> slowest = predicted finishing order.
combined = combined.sort_values("PredictedPace").reset_index(drop=True)
combined.index += 1  # 1-based grid/finish position

print("\nPredicted order (based on weighted Q1/Q2/Q3 pace):")
print(combined[["Driver", "Team", "Q1", "Q2", "Q3", "PredictedPace"]])

# ---------------------------------------------------------------
# 3. Plot: horizontal bar chart, fastest predicted pace at top.
# ---------------------------------------------------------------
teams = combined["Team"].unique()
cmap = plt.get_cmap("tab20")
team_colors = {team: cmap(i % 20) for i, team in enumerate(teams)}
bar_colors = combined["Team"].map(team_colors)

fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(
    combined["Driver"][::-1],
    combined["PredictedPace"][::-1],
    color=bar_colors[::-1],
)
ax.set_xlabel("Predicted pace (s) — weighted avg of Q1/Q2/Q3 best laps")
ax.set_title(
    f"{session.event['EventName']} {session.event.year} — Predicted Race Order"
)
ax.set_xlim(
    combined["PredictedPace"].min() - 0.5, combined["PredictedPace"].max() + 0.5
)

# Only need each team once in the legend.
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in team_colors.values()]
ax.legend(handles, team_colors.keys(), bbox_to_anchor=(1.02, 1), loc="upper left")

plt.tight_layout()
plt.savefig("predicted_race_order.png", dpi=150)
plt.show()
