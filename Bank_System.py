
class User():
   def __init__(self,name,age,gender):
    self.name =name
    self.age =age
    self.gender=gender
	
   def show_details(self):
    print("Personal Details\n")
    print("Name ",self.name)
    print("Age ",self.age)	
    print("Gender",self.gender)
     
class Bank(User):
    def __init__(self,name,age,gender):
     super().__init__(name,age,gender)
     self.balance=0
    def deposit(self,amount):
     self.balance+=amount 
     print("Acount balance has been updated : $",self.balance)
    def withdraw(self,amount):
     self.amount=amount
     if self.amount>self.balance:
       print("Insufficient Funds | Balance Avaliable : $ ",self.balance)
     else:
       self.balance-=amount
       print("Acount balance has been updated : $",self.balance)		
      	 
    def view_balance(self):
      print("Acount balance : $",self.balance)

	  

	  
Dina= Bank("Dina",23,"Female")
Dina.name
Dina.show_details()
Dina.deposit(2000)
Dina.deposit(2000)
Dina.deposit(6000)
Dina.withdraw(1000)
Dina.view_balance()


