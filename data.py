import pandas as pd

class store:
    
    fruit_names = []
    fruit_prices = []
    
    vegetable_names = []
    vegetable_prices = []
    
    def __init__(self):
        vegetables_data = pd.read_csv("Vegetable_Prices_2022.csv")
        fruits_data = pd.read_csv("Fruit Prices 2022.csv")
    
        for item in range(len(fruits_data["name"])):
            self.fruit_names.append(fruits_data["name"][item])
            self.fruit_prices.append(fruits_data["price"][item])
        
        for item in range(len(vegetables_data["name"])):
            self.vegetable_names.append(vegetables_data["name"][item])
            self.vegetable_prices.append(vegetables_data["price"][item])                
                                                                       