# jack , queen and king -> 10
# every other card -> face value
#  Ace can take 1/11 which user can determine -> 1 if u exceed 21 and 11 if u dont
# should have done it more neatly using functions
from random import choice
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]


def black_jack():
    '''This is the function written for playing black_jack'''
    start=input("Do you want to play Blackjack?(y for Yes/ n for No): ")
    if start=="y":
        user_cards=[choice(cards),choice(cards)]
        dealer=[choice(cards),choice(cards)]
        print(user_cards)
        print(dealer[0])
        user_sum=sum(user_cards) 
        while input("Do you want to deal another card: ")=="y":
            new_card=choice(cards)
            user_cards.append(new_card)
            print(user_cards)
            user_sum+=new_card
            if user_sum>21:
                print("you loose")
                return
            else:
                continue
        
        print(user_cards)
        print(dealer)
        if sum(user_cards)>sum(dealer):
            print("You win")
        elif sum(user_cards)<sum(dealer):
            print("You loose")
        else:
            print("draw")
        
        continue_the_game=input("Do you want a rematch?: ")
        if continue_the_game=="y":
            black_jack()
            
    
        
    


black_jack()