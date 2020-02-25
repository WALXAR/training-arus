import requests


def get_ships(base_url):
    url = f"{base_url}/v3/ships"
    r = requests.get(url)
    return r.json()


def main():
    print(len(get_ships()))


if __name__ == "__main__":
    main()
