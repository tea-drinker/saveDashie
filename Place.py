import requests
from time import sleep

class Place(object):
    def __init__(self, user, passwd, greedy=False):
        """
        user: reddit username
        pass: reddit password
        greedy: keep trying to perform request
        """

        self.session = requests.session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144"})

        self.greedy = greedy

        payload= {'op': 'login',
                  'user': user,
                  'passwd': passwd}
        self.session.post("https://www.reddit.com/post/login", data=payload)

        sleep(1)

        self.last = self.session.get("https://reddit.com/api/me.json")
        self.modhash = self.last.json()["data"]["modhash"]
        self.session.headers.update({"x-modhash": self.modhash})
    def _get(self, x, y):
        payload = {"x": x,
                   "y": y}
        return self.session.get("https://www.reddit.com/api/place/pixel.json", params=payload)
    def get(self, x=0, y=0):
        """get the color information at a given pixel
        x: x-coordinates
        y: y-coordinates
        """
        self.last = self._get(x,y)
        if self.greedy:
            while self.last.status_code == 429:
                sleep(1)
                self.last = self._get(x,y)
        return self.last.json()

    def _draw(self, x=0, y=0, color=0):
        payload = {"x": x,
                   "y": y,
                   "color": color}
        return self.session.post("https://www.reddit.com/api/place/draw.json", data=payload)

    def draw(self, x=0, y=0, color=0):
        """draw a color at given coordinates
        x: x-coordinates
        y: y-coordinates
        color: color to draw at coordinates
        """
        self.last = self._draw(x,y,color)
        if self.greedy:
            while self.last.status_code == 429:
                json = self.last.json()
                if "wait_seconds" in json:
                    wait=json["wait_seconds"]
                    print("Waiting: {}s".format(wait))
                    sleep(wait)
                else:
                    sleep(1)

                self.last = self._draw(x,y,color)
        return self.last.json()

def randerase(place):
    from random import randint
    print("Running Random Erase")
    while 1:
        x = randint(0,999)
        y = randint(0,999)
        pixel = place.get(x, x)
        if "color" in pixel and pixel["color"]!=0:
            place.draw(x,y,0)
            print("Erasing {}x{}".format(x,y))
        sleep(1)

def dieblue(place):
    print("Running dieblue")
    while 1:
        for x in range(999,0,-1):
            for y in range(999,0,-1):
                print("Checking: {}x{}".format(x,y))
                r = place.get(x,y)
                if "color" in r and r["color"]==13:
                    print("Clearing Blue")
                    place.draw(x,y,color=0)
                sleep(1)

if __name__ == "__main__":
    import argparse
    import getpass

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--user', help='Reddit username')
    parser.add_argument('--passwd', help='Reddit password')
    parser.add_argument('program', help='/r/place macro to run')

    args = parser.parse_args()
    if args.user is None:
        args.user = input("Enter Reddit Username: ")
    if args.passwd is None:
        args.passwd = getpass.getpass()

    place = Place(args.user, args.passwd, greedy=True)

    try:
        if args.program == "randerase":
            randerase(place)
        if args.program == "dieblue":
            dieblue(place)
        raise("Unknown Program: {}".format(args.program))
    except KeyboardInterrupt:
        print("Well, bye")
