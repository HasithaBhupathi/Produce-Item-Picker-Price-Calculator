### perant class

class Item:
    
    all_fruits = []
    all_vegetables = []
    
    def __init__(self, name:str, price: float, quantity:int):
        
        if price < 0:
            raise ValueError("Price must be non negative")
        if quantity < 0:
            raise ValueError("Quantity must be non negative")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def final_object_price(self):
        return self.price*self.quantity-self.discount*self.price*self.quantity
    
    @classmethod
    def total_price(cls):
        
        t_price = 0
        for item in cls.all_fruits:
            t_price = t_price+item["price"]*item["quantity"]
        
        for item in cls.all_vegetables:
            t_price = t_price + item["price"]*item["quantity"]
            
        return t_price    
    
    @classmethod
    def total_discount(cls):
        
        t_discount = 0
        for item in cls.all_fruits:
            t_discount = t_discount + item["discount"]*item["price"]*item["quantity"]
            
        for item in cls.all_vegetables:
            t_discount = t_discount + item["discount"]*item["price"]*item["quantity"]    
        
        return t_discount
    
    @staticmethod
    def final_price():
        return Item.total_price() - Item.total_discount()
    
    @staticmethod
    def class_info():
        print("This is a small softwear for adding your item name, item price, item quantity. Then you can calculate your total price, total discount, and final price. Moreover you have access to change item quantiti and it's discount")

    