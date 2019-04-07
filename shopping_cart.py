class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total=0
        self.employee_discount=None
        self.items=[]
     
    
    def add_item(self, name, price, quantity=1):
        self.items.append([name,price,quantity])
        self.total+= price*quantity
        print (self.items)
        return self.total
        pass
    

    
    def mean_item_price(self):
        mean = None
        for i in self.items :
            print ( self.items[i][1]) 
        return mean

    def median_item_price(self):
        pass

    def apply_discount(self):
        pass

    def void_last_item(self):
        pass