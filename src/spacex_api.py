import requests


def get_ships():
    url = "http://ec2-18-229-131-87.sa-east-1.compute.amazonaws.com/v3/ships"
    r = requests.get(url)
    return r.json()


def main():
    print(len(get_ships()))


if __name__ == '__main__':
    main()
