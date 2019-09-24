class Client():
    def __init__(self, name, last_name, cpf):
        self.name = name
        self.last_name = last_name
        self.cpf = cpf

class Account():
    def __init__(self, client, number, balance, limit):
        self.name = client
        self.number = number
        self.balance = balance
        self.limit = limit
    
    def account_deposit(self, value):
        self.value += balance

    def account_plunder(self, value):
        self.value -= balance

    def account_statement(self):
        return balance
    
    def account_transfer(self, destiny, value):
        retreat = self.account_plunder(value)
        if retreat == False:
            return False
        else:
            return True
    