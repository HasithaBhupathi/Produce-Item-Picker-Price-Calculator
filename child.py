from perant import Item

### child class "vegitable"
class vegetable(Item):
    
    def __init__(self, name, price, quantity,discount = 0.1 ,category = "vegetable"):
        super().__init__(name, price, quantity)
        
        if discount < 0:
            raise ValueError("Discount should be nin negative")
        
        self.category = category
        self.discount = discount  
            
        Item.all_vegetables.append(self.__dict__)     
    
    
### chaild class "fruit"
class fruit(Item):

    def __init__(self, name, price, quantity, discount = 0.2,category = "friuit"):
        super().__init__(name, price, quantity)         

        if discount < 0:
            raise ValueError("Discount should be nin negative")
        
        self.category = category
        self.discount = discount   
    
        Item.all_fruits.append(self.__dict__)
    
                  