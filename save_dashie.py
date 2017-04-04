#!/usr/bin/env python3

import Place
from time import sleep
import dashie
import websocket_utils
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
    return process

def fine_filter(next_step_function):
    def process(payload):
        dashie_x = payload["x"] - dashie.left
        dashie_y = payload["y"] - dashie.top

        if dashie.img[dashie_y][dashie_x] != -1:
            next_step_function(payload)
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

def configure_app(discord_list):
    agg = aggregator(discord_list)
    ff = fine_filter(agg)
    cf = coarse_filter(ff)
    unpack = unpacker(cf)
    jmp = websocket_utils.json_message_parser(unpack)
    wsp = websocket_utils.websocket_message_processor(jmp)
    wsl = websocket_utils.websocket_listener(websocket_utils.websocket_factory, wsp)
    while 1:
        wsl.run()

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


    discord_list = Manager().dict()
    p = Process(target=configure_app, args=(discord_list,))
    p.start()

    place = Place.Place(args.user, args.passwd, greedy=False)
    while 1:
        repaint(discord_list, place)
    
    p.terminate()
    
