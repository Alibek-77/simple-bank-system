class NegativeNumberError(Exception):
    pass
class NotFoundEnoughError(Exception):
    pass
class AccountNotFoundError(Exception):
    pass
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f"Account:(owner:{self.owner},balance={self.balance})"
    def deposit(self,amount):
        if amount<0:
            raise NegativeNumberError('Teris sandy salyga bolmaydy!')
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount<=0:
            raise NegativeNumberError('Teris nemese 0 aksha sheshyge bolmaydy!')
        if amount<=self.balance:
            self.balance-=amount
            return self.balance
        raise NotFoundEnoughError('Balans zhetkiliksiz!')
    def get_balance(self):
        return self.balance
class Bank:
    def __init__(self):
        self.accounts=[]
    def add_account(self,account):
        self.accounts.append(account)
    def find_account(self,owner):
        for account in self.accounts:
            if account.owner==owner:
                return f"{owner} esimdi account bar!"
        return f"{owner} esimdi account zhok!"
    def list_accounts(self):
        for acc in self.accounts:
            print(acc)
    def transfer(self,from_owner,to_owner,amount):
        sender=None
        receiver=None
        for acc in self.accounts:
            if acc.owner==from_owner:
                sender=acc
            if acc.owner==to_owner:
                receiver=acc
        if sender is None:
            raise AccountNotFoundError(f"{from_owner} esimdi account tabylmady!")
        if receiver is None:
            raise AccountNotFoundError(f"{to_owner} esimdi account tabylmady!")
        sender.withdraw(amount)
        receiver.deposit(amount)
        return f"{from_owner}-{to_owner}:{amount} tg audaryldy!"
try:
    bank=Bank()
    acc1=Account('Alibek',100)
    acc2=Account('Sultan',1000)
    acc3=Account('Araue',400)
    acc4=Account('Taizhan',10000)
    acc1.deposit(1000)
    acc2.withdraw(100)
    bank.add_account(acc1)
    bank.add_account(acc2)
    bank.add_account(acc3)
    bank.add_account(acc4)
    print(bank.transfer('Sultan','Alibek',200))
    print(bank.find_account('Alibek'))
    print(bank.find_account('Aisuly'))
except NotFoundEnoughError as e:
    print('Kate:',e) 
except NegativeNumberError as f:
    print('Kate:',f)
except AccountNotFoundError as e:
    print('Kate:',e)
print(acc1.get_balance())
print(acc2.get_balance())
bank.list_accounts()
print(bank)