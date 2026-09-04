from pathlib import Path

import fastf1

cache_dir = Path("./cache")
cache_dir.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(cache_dir))

session = fastf1.get_session(2026, "Netherlands", "Q")
session.load()

print(f"Session Name: {session.name}")
print(f"Grand Prix: {session.event['EventName']}")

print("***** Results of the top Ten Qualifiers *****")
print(session.results.iloc[0:10].loc[:, ["Abbreviation", "Q3"]])

fastest_lap = session.laps.pick_fastest()
print(fastest_lap["LapTime"])
print(fastest_lap["Driver"])
