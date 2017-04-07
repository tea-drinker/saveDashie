#!/usr/bin/env python3

import Place
from time import sleep
import dashie
import websocket_utils
import json
from threading import Thread
import websocket

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
          (x, y) = next(iter(keys))

          target_color = discord_list[(x, y)]
          #current_pixel_data = place.get(x, y)
          #verified_current_color = current_pixel_data["color"]

          print("Painting", x, y, target_color)
          #if (verified_current_color == target_color):
              #print("Pixel already harmonised: ", current_pixel_data)
              #del discord_list[(x, y)]
              #sleep(1)
          #else:
          response = place('{{"type":"place", "x":{}, "y":{}, "color":{} }}'.format(x, y, target_color))
          print(response)
          del discord_list[(x, y)]

def unpacker(next_step_function):
    def process(message):
        next_step_function(message["payload"])
    return process

def coarse_filter(next_step_function):
    def process(payload):

        x = payload["x"]
        y = payload["y"]
   
        if x >= dashie.left and x < dashie.right and y >=dashie.top and y < dashie.bottom:
           next_step_function(payload)
        else:
           print('coarse don\' care')
    return process

def fine_filter(next_step_function):
    def process(payload):
        dashie_x = payload["x"] - dashie.left
        dashie_y = payload["y"] - dashie.top

        if dashie.img[dashie_y][dashie_x] != -1:
            next_step_function(payload)
        else:
            print("fine don't care")
    return process

def aggregator(discord_list):
    def process(payload):
        x = payload["x"]
        y = payload["y"]
        dashie_x = x - dashie.left
        dashie_y = y - dashie.top
        
        if payload["color"] != dashie.img[dashie_y][dashie_x]:
            print("Discord!", payload)
            discord_list[(x, y)] = dashie.img[dashie_y][dashie_x]

        elif (x, y) in discord_list:
            print("Pixel element harmonised", payload)
            del discord_list[(x, y)]
    return process

global cooldown
def cooldown(message):
    cooldown = message["wait"]

if __name__ == "__main__":
    #freeze_support()

    import argparse
    import getpass

    parser = argparse.ArgumentParser(description='Save dashie on /r/places!')
    parser.add_argument('--user', help='Reddit username')
    parser.add_argument('--passwd', help='Reddit password')
    parser.add_argument('--url', help='WebSockets URL')

    args = parser.parse_args()

    if args.url is None:
        args.url = input("Enter WebSockets URL: ")


    discord_list = {}

    agg = aggregator(discord_list)
    ff = fine_filter(agg)
    cf = coarse_filter(ff)

    mr = websocket_utils.message_router("type")
    mr.add_route("pixel", cf)
    mr.add_route("cooldown", cooldown)

    jmp = websocket_utils.json_message_parser(mr.process)
    wsp = websocket_utils.websocket_message_processor(jmp)
    wsl = websocket.WebSocketApp(args.url, on_message=wsp)
    th = Thread(target=wsl.run_forever)
    th.start()

    sleep(5)

    while 1:
        repaint(discord_list, wsl.send)
        sleep(cooldown)
        cooldown = 0
        print(discord_list)
    
    p.terminate()
    
