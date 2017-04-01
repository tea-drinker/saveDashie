import Place
from time import sleep
import dashie
import websocket
import json
from multiprocessing import Process, Manager
"""
user = "<reddit username>"
passwd = "<reddit password>"
url = "<Websocket URL from the devtools panel>"
"""

def repaint(discord_list):
   p = Place.Place(user, passwd, greedy=False)
   while 1:
      print("test", discord_list.keys())
      if len(discord_list.keys()) == 0:
          sleep(10)
      else:
          (x, y) = discord_list.keys()[0]
          print("Painting", x, y, dashie.img[y-dashie.top][x-dashie.left])
          p.draw(x, y, dashie.img[y-dashie.top][x-dashie.left])
          del discord_list[(x, y)]
          sleep(600)

discord_list = Manager().dict()
p = Process(target=repaint, args=(discord_list,))
p.start()

ws = websocket.create_connection(url)
while 1:
   payload = json.loads(ws.recv())["payload"]
   if "x" not in payload:
      continue
   elif payload["x"]>=dashie.left and payload["x"]<=dashie.right and \
      payload["y"]>=dashie.top and payload["y"]<=dashie.bottom:
      if payload["color"] != dashie.img[payload["y"]-dashie.top][payload["x"]-dashie.left]:
          print("Discord!", payload)
          discord_list[(payload["x"], payload["y"])] = payload["color"]
      elif (payload["x"], payload["y"]) in discord_list:
          print("Pixel element harmonised", payload)
          del discord_list[(payload["x"], payload["y"])]
