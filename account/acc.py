class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance =int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposit(self,amount):
        self.balance=self.balance+amount

    def commit(self):
        with open(self.filepath, 'w')as file:
            file.write(str(self.balance))

class Checking(Account):
    """ This class generates checking account objects"""

    type="checking"

    def __init__(self,filepath,fee):
        Account.__init__(self,filepath)
        self.fee =fee

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee

jackschecking  = Checking("account//jack.txt",1)
jackschecking.transfer(100)
print(jackschecking.balance)
jackschecking.commit()

jonschecking  = Checking("account//john.txt",1)
jonschecking.transfer(100)
print(jonschecking.balance)
jonschecking.commit()

print(jonschecking.type)
print(jonschecking.__doc__)
