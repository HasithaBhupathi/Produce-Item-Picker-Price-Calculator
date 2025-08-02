from child import fruit, vegetable
from data import store

### child class (user)
class user:
    
    storage = store()
    
    def __init__(self, category: str, name: str, quantity: int, discount:float):
        self.category = category
        self.name = name
        self.quantity = quantity
        self.discount = discount
    
        if category == "fruit":
            
            for index in range(len(self.storage.fruit_names)):
                if name == self.storage.fruit_names[index]:
                    fruit(self.name, self.storage.fruit_prices[index], self.quantity, self.discount)
                    
            else: 
                pass
            
        elif category == "vegetable":
            
            for index in range(len(self.storage.vegetable_names)):
                if name == self.storage.vegetable_names[index]:
                    vegetable(self.name, self.storage.vegetable_prices[index], self.quantity, self.discount)
                    
            else: 
                pass
                                 