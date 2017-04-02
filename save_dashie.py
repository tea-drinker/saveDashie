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
          print("Nothing to fix!")
          sleep(10)
      else:
          (x, y) = discord_list.keys()[0]

          target_color = discord_list[(x, y)]
          current_pixel_data = place.get(x, y)
          verified_current_color = current_pixel_data["color"]

          print("Painting", x, y, target_color)
          if (verified_current_color == target_color):
              print("Pixel already harmonised: ", current_pixel_data)
              del discord_list[(x, y)]
              sleep(1)
          else:
              response = place.draw(x, y, target_color)
              del discord_list[(x, y)]

              if "wait_seconds" not in response:
                  print("Unknown response. Sleeping 10 seconds")
                  print(response)
                  response["wait_seconds"] = 10
              elif "error" not in response:
                  print("Cool down", response["wait_seconds"], "seconds")
              elif response["error"] == 429:
                  print("Can't paint yet. Sleeping", response["wait_seconds"], "seconds")
              else:
                  print("unknown error", response, " Sleeping 10 seconds")
                  response["wait_seconds"] = 10

              sleep(response["wait_seconds"])

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
          if payload["color"] != dashie.img[dashie_y][dashie_x] and dashie.img[dashie_y][dashie_x] != -1:
              print("Discord!", payload)
              discord_list[(real_x, real_y)] = dashie.img[dashie_y][dashie_x]

          elif (real_x, real_y) in discord_list:
              print("Pixel element harmonised", payload)
              del discord_list[(real_x, real_y)]
              print(len(discord_list.keys()), "errors left to repair")



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

    place = Place.Place(args.user, args.passwd, greedy=False)

    discord_list = Manager().dict()
    p = Process(target=repaint, args=(discord_list,place,))
    p.start()

    monitor_dashie(args.url)
