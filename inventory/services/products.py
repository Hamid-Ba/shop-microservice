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
    
    def get_by(self, id: str):
        try:
            return Product.get(id)
        except:
            return False
        
    def create(self, product):
        product = Product(**product.model_dump())
        return product.save()
        
    def delete_by(self, id:str):
        try:
            Product.delete(id)
            return True
        except:
            return False
        
        
product_service = ProductService()