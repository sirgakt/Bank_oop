# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:07:34 2020

@author: User
"""

from temp import DemirBank

class AtmMachine(DemirBank):
    
    def __init__(self, id_account, object_account):
        self.id = object_account.verification()
        if self.id != id_account:
            raise TypeError('Verification Error')
        else:
            print("Verification passed")

    def withdraw(self, amount, object_account):
        return object_account.withdraw(amount)
    
    
