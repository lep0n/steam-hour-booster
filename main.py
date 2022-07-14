from steam.client import SteamClient
from art import tprint

import json
import requests


def validate_games(games: list) -> list[int] | list:
    valid_games = []

    if len(games) == 0:
        print("[ERROR] The list of games is empty! Add them to the config.json file.")

    for game in games:
        game_info = requests.get(
            f"https://store.steampowered.com/api/appdetails/?appids={game}&filters=basic"
        ).json()
        if game_info == "null" or game_info[str(game)]["success"] == False:
            print(
                f"[ERROR] The game ID ({game}) is invalid and can't be found! Change it in the config.json file."
            )
            continue

        valid_games.append(game)

    if len(valid_games) == 0:
        print(
            "[ERROR] All games ID that you indicated were not valid. Change them in the config.json file."
        )

    return valid_games


def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    for account in config["accounts"].values():
        username = account["username"]
        password = account["password"]

        games = account["games"]

        client = SteamClient()
        client.set_credential_location("./users_data")

        print(f"[+] Trying to login the account: {username}")
        client.cli_login(username, password)

        valid_games = validate_games(games)
        if len(valid_games) == 0:
            print(
                f"[-] {username} login fail, because the list of valid games is empty.\n"
            )
            continue

        client.games_played(valid_games)
        print(f"[+] {username} connected successfully, start boosting...\n")

    client.run_forever()


if __name__ == "__main__":
    try:
        tprint(text="Steam  Hour  Booster", font="standart")
        print("github.com/lep0n")
        main()

    except KeyboardInterrupt:
        print("\nGoodbye!")
