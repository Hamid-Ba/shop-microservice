from persistence.models import Product

class ProductService:
    
    def get_all(self):
        keys = Product.all_pks()
        
        for key in keys:
            product = Product.get(key)
            yield {
                "id": product.pk,
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity
            }
        
        
product_service = ProductService()