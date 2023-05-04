class Fruit:
   is_natural=True 

def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
       
    def is_cheap(self):
        if self.price > 10:
            return True
        else:
            return False
       
    def fruit_name(self):
        return self.name
   
    def fruit_color(self):
        return "f "This is {self.name} and it is naturally {self.color}
   
    def fruit_price(self):
        return "f" This {self.color},{self.name} is sold at {self.price}"