import requests, argparse

from config import API_KEY, RIOT_API_BASE


BY_SUMMONER = "/lol/spectator/v4/active-games/by-summoner/{summoner_id}"


# TODO: find game time and return the time
def main(*args):
    summoner_id = args["user_id"]

    url = RIOT_API_BASE + BY_SUMMONER

    headers = {
        "X-Riot-Token": API_KEY,
        "Content-Type": "application/json; charset=utf-8"
    }

    res = requests.get(url.format(summoner_id=summoner_id), headers=headers)

    print(res.text)
    



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_id")
    args = parser.parse_known_args()
    main(args[0])