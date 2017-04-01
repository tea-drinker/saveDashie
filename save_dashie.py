import Place
from time import sleep
import dashie
import websocket
import json
from multiprocessing import Process, Manager, freeze_support

def repaint(discord_list, place):
   while 1:
      try:
          keys = discord_list.keys()
      except:
          print("Error fetching keys. Quitting")
          return

      if len(discord_list.keys()) == 0:
          sleep(10)
      else:
          (x, y) = discord_list.keys()[0]
          print("Painting", x, y, discord_list[(x, y)])
          place.draw(x, y, discord_list[(x, y)])
          del discord_list[(x, y)]
          sleep(660)

def monitor_dashie(url):
    ws = websocket.create_connection(url)
    while 1:
       payload = ws.recv()

       if payload == b'\x03\xe8':
           print("server is overloaded. Quitting")
           return
       try: 
           payload = json.loads(payload)["payload"]
       except:
           print("json parse error", payload)
           sleep(10)
           continue

       if "x" not in payload:
          continue

       real_x = payload["x"]
       dashie_x = real_x - dashie.left

       real_y = payload["y"]
       dashie_y = real_y - dashie.top

       if real_x >= dashie.left and real_x < dashie.right and \
          real_y >=dashie.top and real_y < dashie.bottom:
          if payload["color"] != dashie.img[dashie_y][dashie_x]:
              print("Discord!", payload)
              discord_list[(real_x, real_y)] = dashie.img[dashie_y][dashie_x]

          elif (real_x, real_y) in discord_list:
              print("Pixel element harmonised", payload)
              del discord_list[(real_x, real_y)]



if __name__ == "__main__":
    freeze_support()

    import argparse
    import getpass

    parser = argparse.ArgumentParser(description='Save dashie on /r/places!')
    parser.add_argument('--user', help='Reddit username')
    parser.add_argument('--passwd', help='Reddit password')
    parser.add_argument('--url', help='WebSockets URL')

    args = parser.parse_args()
    if args.user is None:
        args.user = input("Enter Reddit Username: ")
    if args.passwd is None:
        args.passwd = getpass.getpass()
    if args.url is None:
        args.url = input("Enter WebSockets URL: ")

    place = Place.Place(args.user, args.passwd, greedy=True)

    discord_list = Manager().dict()
    p = Process(target=repaint, args=(discord_list,place,))
    p.start()

    monitor_dashie(args.url)

