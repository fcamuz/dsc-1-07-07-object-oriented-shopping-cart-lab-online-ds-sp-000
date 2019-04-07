class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total=0
        self.employee_discount=emp_discount
        self.items=[]
     
    
    def add_item(self, name, price, quantity=1):
        self.items.append([name,price,quantity])
        self.total+= price*quantity
      #  print (self.items)
        return self.total
        
    
    
    def mean_item_price(self):
        mean=0
        for i in range(len(self.items)):
            mean = mean + self.items[i][2]
        mean= self.total/mean
        return mean
    

    def median_item_price(self):
        med_price=[]
        for i in range(len(self.items)):
            k=1
            if k==self.items[i][2]:
                med_price.append(self.items[i][1])
           
            else:
                for k in range(self.items[i][2]):
                    med_price.append(self.items[i][1])
                    
        med_price.sort()
        length=(len(med_price))

        if length %2 == 0:
            x= int(length/2)
            return ((med_price[x-1]+med_price[x])/2)
        else :
            x=int((length-1)/2)
            return(med_price[x])
        

    def apply_discount(self):
        disc_total = self.total
        if self.employee_discount==None:
            return("Sorry, there is no discount to apply to your cart :(")
        else:
            disc_total= disc_total-disc_total*self.employee_discount/100
            return(disc_total) 
        #return self.total
        

    def void_last_item(self):
        if self.items:
            last_item=self.items[-1]
            if last_item[2]>1:
                self.total=self.total-last_item[1]
                self.items[-1][2]=last_item[2]-1
            else:
                self.items.pop()
                self.total=self.total-last_item[1]
            return self.total
        else:
            print("There are no items in your cart")