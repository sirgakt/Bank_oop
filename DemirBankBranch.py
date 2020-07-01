from temp import DemirBank

class DemirBankBrach(DemirBank):
   
    def __init__(self, id_account, object_account):
        self.id = object_account.verification()
        if self.id != id_account:
            raise TypeError('Verification Error')
        else:
            print("Verification passed")
            
    def dep(self, amount, object_account):
        return object_ac.deposit(amount)
    
    def transfer_money(self, object_ac_from, object_ac_to, amount):
        if (object_ac_from.withdraw(amount) and object_ac_to.deposit(amount)): 
            print('Transfer passed')
        else:
            print('Transfer Error'  ) 