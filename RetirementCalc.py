import math 

PersonsAge = int(input('How old are you?'))
RetirementAge = int(input('At what age are you retiring at?'))
YearsTillRetirement = RetirementAge - PersonsAge 
MattMoney = float(input('How much do you currently have under your mattress?'))
BankSavings = float(input('What is your balance in bank savings?'))
BondMoney = float(input('What is your balance in bonds?'))
StockMoney = float(input('What is your balance in stocks?'))

B = open('bonds.txt','r')
Blines = B.readlines()
Blines = list(map(float,Blines))
B.close()

S = open('stocks.txt','r')
Slines = S.readlines()
Slines = list(map(float,Slines))
S.close()

for i in range(0,YearsTillRetirement):
    BankSavings= BankSavings * (1.02)
    BondMoney= BondMoney*(1+Blines[i])
    StockMoney = StockMoney*(1+Slines[i])
    Choice = 0
    while Choice != '5':
        Choice = input(print(""" 'What is the value of all options below?' 
        1. Money under mattress
        2. Money in a banks saving account
        3. Money invested in 'bonds'
        4. Money invested in 'stocks'
        5. Finished investing
        """))

        if Choice == '1':
            MattMoney = MattMoney + float(input('How much money did you put under your mattress this year?')) 
        elif Choice == '2':
            BankSavings= BankSavings + float(input('How much are you going to add to the bank savings?'))
        elif Choice == '3':
            BondMoney = BondMoney + float(input('How much money are you going to deposit?'))
        elif Choice == '4':
            StockMoney = StockMoney + float(input('How much money are you going to invest?'))

print(BankSavings,'This is the amount of your Bank Savings')
print(BondMoney,'Your total amount of Bond Money')
print(StockMoney,'Your total amount of stock money')
print(MattMoney,'Your total amount of Mattress money')
    
    
f = open('Retirement.txt','w')
f.write('Bank savings: ' + str (BankSavings) + '\n')
f.write('Mattress Money: ' + str (MattMoney) + '\n')
f.write('Bond Money: '+ str(BondMoney) + '\n')
f.write('Stock Money: '+ str(StockMoney) + '\n')
f.close()
    

T = MattMoney + BankSavings + BondMoney + StockMoney
print(T,'total balance in all accounts')
T = T * 0.97 **YearsTillRetirement 
print(T,'Total balance with inflation')





33
