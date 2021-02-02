class Category:
    ledger = []
    name = ""
    
    
    def __init__(self, name):
        self.ledger = []
        self.name = name
     
        
    def deposit(self, amount, description):
        self.ledger.append({"amount" : amount, "description" : description})
    
    
    def get_balance(self):
        balance = 0
        for bal in self.ledger:
            balance += int(bal["amount"])
        return balance
       
        
    def check_funds(self, amount):
        if (self.get_balance() < amount):
            return False
        else:
            return True
            
            
    def withdraw(self, amount, description):
        if self.check_funds(amount):
            self.ledger.append({"amount" : -amount, "description" : description})
            return True
        else:
            return False
            
            
    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.ledger.append({"amount" : -amount, "description" : "Transfer to [Destination Budget Category]"})
            
            budget.ledger.append({"amount" : amount, "description" : "Transfer from [Source budget Category]"})
            return True
            
        else:
            return False
            
        
    def get_heading(self):
        str = stars = ""
        half = (30 - len(self.name)) / 2
        
        for i in range(int(half)):
            stars += "*"
        str = stars + self.name + stars
        
        if len(self.name) % 2 == 1:
            str += "*"
            
        return str
            
            
    def get_desc(self, led_desc):
        descStr = led_desc[:23]
        for i in range(23 - len(descStr)):
            descStr += " "
        return descStr
        
        
    def get_amt(self, amt):
        amtStr = str("{:.2f}".format(amt))
        
        for i in range(7 - len(amtStr)):
            amtStr = " " + amtStr
            
        return amtStr
  
      
    def get_total(self):
        total = 0
        for led in self.ledger:
            total += led["amount"] * 1000
        return total / 1000
   
    
    def get_spent(self):
        withdraw = 0
        
        for led in self.ledger:
            if (led["amount"] < 0):
                withdraw += abs(led["amount"] * 1000)
                
        return floor(withdraw / 1000)
      
    def __str__(self):
        string = self.get_heading() +"\n"
        
        for led in self.ledger:
            string += self.get_desc(led["description"]) + self.get_amt(led["amount"]) + "\n"
        
        #for ledge in self.ledger:
        string += 'Total: ' + str(self.get_total())
        return string
         
       
       
            
 
SPACE = ' '
BAR = '|'
DASH = '-'
BALL = 'o'
TITLE = "Percentage spent by category"

from math import floor
# [[47, 'Food'], [4, 'Clothings'], [47, 'Housing']]
def create_spend_chart(category_list):
    chart = ''
    
    name_percentage_list = convert_list(category_list)
    # print(name_percentage_list)
    
    # Create Title
    chart += TITLE + '\n'
    
    # Create Barchart
    for i in range (100, -10, -10):
        if (i == 100):
            chart += str(i) + BAR
        elif (i == 0):
            chart +=  SPACE + SPACE + str(i) + BAR
        else:
            chart +=  SPACE + str(i) + BAR
            
        for item in name_percentage_list:
            chart += SPACE
            
            if (item[0] < i):
                chart += SPACE
            else:
                chart += BALL
                
        chart += '\n'
        
    # Create bar divider
    for i in range(len(name_percentage_list) * 2 + 4):
        chart += '-'
    chart += '\n'
    
    # Create the name label
    maxLength = getMaximumLength(name_percentage_list)
    
    ch = ''
    for i in range(0, maxLength):
        chart += str(i) + SPACE + SPACE + SPACE
        for item in name_percentage_list:
            if (len(item[1]) > i):
                chart += SPACE + item[1][i]
            else:
                ch += SPACE + SPACE
                chart += SPACE + SPACE
        
        chart += '\n'
    print(chart)
    
    
def convert_list(category_list):
    name_percentage_list = []
    total = 0
    for item in category_list:
        total += item.get_spent() * 1000
        
    total = total / 1000
    for item in category_list:
        name_percentage_list.append([floor(item.get_spent() / total * 100), item.name])
    
    return name_percentage_list
     
     
def getMaximumLength(list_in_list):
    list = []
    for item in list_in_list:
        list.append(len(item[1]))
        
    return max(list)