class bank:
    def __init__(self):
        pass
    def transaction(self):
        print('Total transaction value')

    def account_opening(self):
        print("The total account opening is")

    def deposite(self):
        print('"The total deposite is')


class HDFC_bank():
    def hdfc_to_icic(self):
        print("this will show you all the transaction happened to hdfc to icic")

    def deposite(self):
        print('"The total deposite is 222')

class ineuron_bank:
    def hello(self):
        print('hello there')


class icfc(bank,HDFC_bank, ineuron_bank):
    pass


t = icfc()

t.deposite()

t.hello()
