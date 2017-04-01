import Place
from time import sleep
import dashie
import websocket
import json
from multiprocessing import Process, Manager

#Put your credentials in userDetails.py so changes to this file can be safely pushed.
import user_details

def repaint(discord_list):
   p = Place.Place(user_details.user, user_details.passwd, greedy=False)
   while 1:
      print("test", discord_list.keys())
      if len(discord_list.keys()) == 0:
          sleep(10)
      else:
          (x, y) = discord_list.keys()[0]
          print("Painting", x, y, discord_list[(x, y)])
          p.draw(x, y, discord_list[(x, y)])
          del discord_list[(x, y)]
          sleep(660)

def monitor_dashie():
    ws = websocket.create_connection(user_details.url)
    while 1:
       payload = ws.recv()

       if payload == b'\x03\xe8':
           print("server is overloaded. Quitting")
           exit()
       
       payload = json.loads(payload)["payload"]
       if "x" not in payload:
          continue

       real_x = payload["x"]
       dashie_x = real_x - dashie.left

       real_y = payload["y"]
       dashie_y = real_y - dashie.top

       if real_x >= dashie.left and real_x <= dashie.right and \
          real_y >=dashie.top and real_y <= dashie.bottom:
          if payload["color"] != dashie.img[dashie_y][dashie_x]:
              print("Discord!", payload)
              discord_list[(real_x, real_y)] = dashie.img[dashie_y][dashie_x]

          elif (real_x, real_y) in discord_list:
              print("Pixel element harmonised", payload)
              del discord_list[(real_x, real_y)]



if __name__ == "__main__":
    discord_list = Manager().dict()
    p = Process(target=repaint, args=(discord_list,))
    p.start()

    monitor_dashie()
