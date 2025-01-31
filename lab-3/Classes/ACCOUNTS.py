class Account:
    def __init__(self,owner = "None",balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount:float = 0.0):
        self.balance += amount
        print(f"{amount}$ added to your Account.\nNow your balance is {self.balance}$")
        
    def withdrawal(self,amount:float = 0.0):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount}$ withdrawed from your Account.\nNow your balance is {self.balance}$")
        else:
            print(f"Your balance {self.balance}$ is less than {amount}$")

obj5 = Account("Demid",300.0)
obj5.deposit(54000.0)
obj5.withdrawal(300.0)
