from time import sleep

from persistence import models
from event_handler import redis
from infrastructure.dependencies import payment_context


class OrderService():
        
    def get_by(self, id: int, context: payment_context):
        order = context.query(models.Order).get(id)
        return order if order else False
    
    def place_order(self, product, count, context: payment_context):
        try:
            order = models.Order()

            order.product_id = product.get("pk")
            order.price = product.get("price")
            order.fee = 0.2 * product.get("price")
            order.quantity = count
            order.total = 1.2 * product.get("price")
            order.status = "pending"
            
            context.add(order)
            context.commit()
            
            return {
                "id" : order.id,
                "product_id" : order.product_id,
                "total": order.total,
                "price": order.price,
                "fee": order.fee,
                "count": order.quantity,
                "status": order.status
            }
        except:
            return False
    
    def deliverd_order_by(self, id: int, context: payment_context):
        try:
            sleep(5)
            order = context.query(models.Order).get(id)
            
            order.status = "Delivered"
            context.add(order)
            context.commit()
            
            order = {
                "id" : order.id,
                "product_id" : order.product_id,
                "total": order.total,
                "price": order.price,
                "fee": order.fee,
                "count": order.quantity,
                "status": order.status
            }
            
            try:
                redis.xgroup_create("delivered_status", "inventory-group")
            except:
                print("Inventory Group Has Already Been Created")
            redis.xadd("delivered_status", order, "*")

            return True
        except Exception as e:
            return print(str(e))
        
    def refound_order_by(self, id:int, context: payment_context):
        try:
            order = context.query(models.Order).get(id)
            
            order.status = "ReFound"
            context.add(order)
            context.commit()
            
            
            order = {
                "id" : order.id,
                "product_id" : order.product_id,
                "total": order.total,
                "price": order.price,
                "fee": order.fee,
                "count": order.quantity,
                "status": order.status
            }
            return order
        except:
            return False
order_service = OrderService()