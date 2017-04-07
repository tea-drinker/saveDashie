#!/usr/bin/env python3

import json
import websocket
from time import sleep

class websocket_dummy:
    def recv(self):
        return '{"type":"place", "payload":{"x":770, "y":416, "color":0, "author":"tea-drinker"}}'

def websocket_factory(from_location):
    def get():
        if type(from_location) == str:
            url = from_location
        elif type(from_location) == function:
            url = from_location()

        return websocket.create_connection(url)
    return get

class websocket_listener:
    
    def __init__(self, websocket_factory, next_step_function):
        self.websocket_factory = websocket_factory
        self.next_step = next_step_function
    
    def run(self):
            ws = self.websocket_factory()
        #try:
            message = ws.recv()
            self.next_step(message)
        #except:
        #todo: some exception handlers

def websocket_message_processor(next_step_function):
    def process(websocket, message):
        if type(message) == str:
            next_step_function(message)
        
        else:
            print('Unknown message:', message)
    return process

def json_message_parser(next_step_function):
    def process(message):
        data = json.loads(message)
        next_step_function(data)
    return process

class message_router:
    def __init__(self, type_field):
        super(message_router, self).__init__()
        self.type_field = type_field
        self.routes = {}

    def add_route(self, value, next_step):
        self.routes[value] = next_step

    def process(self, message):
        if message[self.type_field] in self.routes:
            self.routes[message[self.type_field]](message)

if __name__ ==  '__main__':
    #dump debug data from websocket
    jmp = json_message_parser(print)
    wsp = websocket_message_processor(jmp)
    wsl = websocket.WebSocketApp('ws://pxls.space/ws', on_message = wsp)

    wsl.run_forever()

