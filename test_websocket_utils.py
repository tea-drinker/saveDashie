#!/usr/bin/env python3

import unittest
import websocket_utils

class TestWebsocketDummy(unittest.TestCase):

    ws = websocket_utils.websocket_dummy()
    
    def test_return_type(self):
        self.assertEqual(type(TestWebsocketDummy.ws.recv()), str)


class TestWebsocketListener(unittest.TestCase):
    
    def test_return_type(self):
        global message
        def capture(m):
            global message
            message = m
        wsl = websocket_utils.websocket_listener(websocket_utils.websocket_factory, capture)
        wsl.run()
        self.assertEqual(type(message), str)


class TestWebsocketMessageProcessor(unittest.TestCase):

    def test_filtering(self):
        global message
        def capture(m):
            global message
            message = m
        
        wmp = websocket_utils.websocket_message_processor(capture)
        wmp('test')
        
        self.assertEqual(type(message), str)
        self.assertEqual(message, 'test')
        
        message = None
        wmp(b'test')
        self.assertEqual(type(message), type(None))
        
        
        
if __name__ == '__main__':
    unittest.main()