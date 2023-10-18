import requests
from time import sleep

from event_handler import redis

key = "refound_status"
group = "payment-group"
    
while True:
    try:
        results = redis.xreadgroup(group, key, {key: ">"}, None)
        
        if results != []:
            for result in results:
                obj: dict = result[1][0][1]
                res = requests.post(f"http://127.0.0.1:8001/orders/refound/{int(obj.get('id'))}")
    except Exception as e:
        print(str(e))
        
    sleep(1)