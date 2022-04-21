import websocket
import json
from datetime import datetime, timedelta

from utils import Struct

ws = websocket.WebSocket()
ws.connect("ws://209.126.82.146:8080")

data = dict()
struct = dict()


try:
    start = datetime.now()
    while True:
        ws_data = json.loads(ws.recv())
        if ws_data['a'] in data:
            data[ws_data["a"]].append(ws_data["b"])
        else:
            data[ws_data["a"]] = [ws_data["b"]]
        now = datetime.now()
        if now >= start + timedelta(minutes=1):
            result = dict()
            for i in data:
                print("Aqui 2")
                arr = Struct(data[i])
                struct['max_number'] = arr.max_number()
                struct['min_number'] = arr.min_number()
                struct['first_number'] = arr.first_num()
                struct['last_number'] = arr.last_num()
                struct['number_of_prime_numbers'] = arr.number_of_prime_numbers()
                struct['number_of_odd_numbers'] = arr.number_of_odd_numbers()
                result[i] = struct
                struct = dict()
            print(result)
            start = datetime.now()
            data = dict()
except KeyboardInterrupt:
    ws.close()
    print('Interrupted')
