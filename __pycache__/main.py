# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:58:01 2020

@author: User
"""

from temp import DemirBank
from Branch import DemirBankBrach
from ATM import AtmMachine

Syrgak_account = DemirBank(name='Syrgak', surname='Talantbek', id= 6666, amount=45000)
#temp_account = DemirBankBrach(id_account=6666, object_account=Syrgak_account)



#Saltanat = DemirBank(name='Saltanat', surname='Omuralieva', id= 8888, amount=10000)
#Saltanat.check_balance()

#temp_account.transfer_money(Syrgak_account, Saltanat, 15000)

atm_record =AtmMachine(id_account=6666, object_account=Syrgak_account)
atm_record.withdraw(10000, Syrgak_account)