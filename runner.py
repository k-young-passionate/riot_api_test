import json
import requests
import argparse
import datetime

from config import API_KEY, RIOT_API_BASE

SUMMONER_NAME = "/lol/summoner/v4/summoners/by-name/{summoner_name}"
BY_SUMMONER = "/lol/spectator/v4/active-games/by-summoner/{summoner_id}"

headers = {
    "X-Riot-Token": API_KEY,
    "Content-Type": "application/json; charset=utf-8"
}


def user_id(user_name):
    url = RIOT_API_BASE + SUMMONER_NAME

    res = requests.get(url.format(summoner_name=user_name), headers=headers)
    res = json.loads(res.text)

    return res["id"]


def game_status(summoner_id):
    url = RIOT_API_BASE + BY_SUMMONER
    res = requests.get(url.format(summoner_id=summoner_id), headers=headers)
    res = json.loads(res.text)
    game_length = res["gameLength"]
    game_start_time = res["gameStartTime"] / 1000.0
    game_start_time_human_readable = datetime.datetime.fromtimestamp(game_start_time).strftime('%Y-%m-%d %H:%M:%S')

    return game_start_time_human_readable, game_length


def main(args):
    user_name = args.user_name
    try:
        summoner_id = user_id(user_name)
    except KeyError:
        print("User Not found")
        return

    try:
        start_time, elapsed_time = game_status(summoner_id)
    except KeyError:
        print("Game is not started yet.")
        return
    
    print(start_time, elapsed_time)

    return elapsed_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_name")
    args = parser.parse_known_args()

    main(args[0])
