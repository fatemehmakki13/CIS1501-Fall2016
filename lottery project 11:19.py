import random 
import math
class PowerBall:
    ticket_cost = 2
    def __init__(self):          
        whiteball = list(range(1,70))
        random.shuffle(whiteball)
        whiteball = whiteball[0:5]
        redBall = random.randint(1,26)

    #WhiteChosen = list(range(1,70))


    def get_winnings (self,winning_ticket):
        ticket_cost = 2
        WinningWhiteBalls = 0
        PrizeWon = 0
        WinningRedBall = False
 #       print(self.whiteball)
        print(winning_ticket.whiteball)
#        print(self.redBall)
        print(winning_ticket.redBall)
        for i in self.whiteball:
            if i in winning_ticket.whiteball:
                WinningWhiteBalls += 1
        if self.redBall == winning_ticket.redBall:
            WinningRedBall = True
        print(WinningWhiteBalls)
        if WinningWhiteBalls == 0 and WinningRedBall == True:
            PrizeWon = 4
            print('Total Winnings: $4')
        elif WinningWhiteBalls == 1 and WinningRedBall == False:
            PrizeWon = 4
            print('Total Winnings: $4')
        elif WinningWhiteBalls == 2 and WinningRedBall == True:
            PrizeWon = 7
            print('Total Winnings: $7')
        elif WinningWhiteBalls == 3 and WinningRedBall == False:
            PrizeWon = 7
            print('Total Winnings: $7')
        elif WinningWhiteBalls == 3 and WinningRedBall == True:
            PrizeWon = 100
            print('Total Winnings: $100')
        elif WinningWhiteBalls == 4 and WinngingRedBall == False:
            PrizeWon == 100
            print('Total Winnings: $100')
        elif WinningWhiteBalls == 4 and WinnningRedBall == True:
            PrizeWon = 50000
            print('Total Winnings: $5000')
        elif WinningWhiteBalls == 5 and WinningRedBall == False:
            PrizeWon == 1000000
            print('Total Winnings: $100000')
        elif WinningWhiteBalls == 5 and WinningRedBall == False:
            PrizeWon == 320000000
            print('You have hit the jackpot!')
            print('Total Winnings: $320000000')
            
        return PrizeWon
   

ticket_count = int(input("Enter amount of tickets you'd like to buy"))
totalSpent = 2 * ticket_count
total_winnings = 0 

netLoss = ('Your netloss is', total_winnings - totalSpent)
print(netLoss)



if __name__ == "__main__":
    ticket_count = int(input("Enter amount of tickets you'd like to buy"))
    winning_tickets = PowerBall()
    totalSpent = 0
for ticket in range(ticket_count):
    ticketBought = PowerBall()
    winning_tickets.get_winnings
    totalSpent += ticketBought.ticket_cost
    print('The total cost of your tickets is: $%d' % totalSpent)
    
   
