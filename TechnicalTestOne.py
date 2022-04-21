import websocket
import json
from datetime import datetime, timedelta

from models import Struct

# Creating websocket object
ws = websocket.WebSocket()
# We connect to the websocket
ws.connect("ws://209.126.82.146:8080")

data = dict()  # Dictionary to save the data captured from the websocket, ordered by blocks
struct = dict()  # Dictionary to save the structure of the blocks

try:
    start = datetime.now()  # Initial Time
    while True:
        ws_data = json.loads(ws.recv())  # Websocket data capture
        if ws_data['a'] in data:
            data[ws_data["a"]].append(ws_data["b"])
        else:
            data[ws_data["a"]] = [ws_data["b"]]
        now = datetime.now()  # Current current time check
        # If the current time is one minute or more create the structure
        if now >= start + timedelta(minutes=1):
            result = dict()  # Output dictionary of block data with its structure
            for i in data:
                arr = Struct(data[i])
                struct['max_number'] = arr.max_number()
                struct['min_number'] = arr.min_number()
                struct['first_number'] = arr.first_num()
                struct['last_number'] = arr.last_num()
                struct['number_of_prime_numbers'] = arr.number_of_prime_numbers()
                struct['number_of_odd_numbers'] = arr.number_of_odd_numbers()
                result[i] = struct
                struct = dict()  # Reset the dictionary structure
            print(result)
            start = datetime.now()  # Reset the initial timer
            data = dict()  # Reset the websocket data capture dictionary
except KeyboardInterrupt:
    """If there is a keyboard interrupt, the websocket is closed and the cycle ends"""
    ws.close()
    print('Interrupted')
