from time import sleep

from persistence.database import redis
from services.products import product_service

key = "delivered_status"
group = "inventory-group"
    
while True:
    try:
        results = redis.xreadgroup(group, key, {key: ">"}, None)
        
        if results != []:
            for result in results:
                obj: dict = result[1][0][1]
                res = product_service.decrease_stock(obj.get("product_id"), int(obj.get("count")))
                
                if not res:
                    try:
                        redis.xgroup_create("refound_status", "payment-group")
                    except:
                        pass
                        
                    redis.xadd("refound_status", {"id": obj.get("id")}, "*")
                    
    except Exception as e:
        print(str(e))
        
    sleep(1)