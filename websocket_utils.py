#!/usr/bin/env python3

class websocket_dummy:
    def recv(self):
        return '{type:"place", payload:{"x":1, "y":2, "color":0, author:"tea-drinker"}}'

def websocket_factory():
    return websocket_dummy()

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
    def process(message):
        if type(message) == str:
            next_step_function(message)
        
        else:
            print('Unknown message:', message)
    return process

if __name__ ==  '__main__':
    #dump debug data from websocket
    wsp = websocket_message_processor(print)
    wsl = websocket_listener(websocket_factory, wsp)
    wsl.run()
    