import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
TOKEN_FILE = BASE_DIR / "data" / "token.text"


def get_token():
    if TOKEN_FILE.exists():
        # read the existing token
        with open(file=TOKEN_FILE, mode="r") as read_file:
            TOKEN = read_file.read().strip()
    else:
        # generate a new token for the first time
        TOKEN = secrets.token_hex(24)

        # save token to file
        with open(file=TOKEN_FILE, mode="w") as write_file:
            write_file.write(TOKEN)

    return TOKEN
