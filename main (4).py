#Python program to create bankaccount class
#With both a deposit() and a withdraw() function
class Bank_Account:
  def __init__(self):
      self.balance=0
      print("Hello!!! Welcome to the deposit & withdrawal machine")
  def deposit(self):
      amount=float(input("Enter amount to be deposited:"))
      self.balance +=amount
      print("\n Amonut deposited:", amount)
  def withdraw(self):
      amount=float(input("Enter amount to be withdrawal:"))
      if self.balance>=amount:
         self.balance-=amount
         print("\n you withdrew:",amount )
      else:
         print("\n insufficient balance")
  def desplat(self):
      print("\n net available balance =",self.balance)
#Driver code
#Creating an object of class
s=Bank_Account()
#Calling functions with that class
s.deposit()
s.withdraw()
s.display()



  

    
