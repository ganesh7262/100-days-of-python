# number gussing game



def random_number_generator():
    '''generates a random number between 1-100 inclusive'''
    from random import randint
    return randint(1,100)

def game_difficulty():
    '''game difficulty'''
    choice=input("Choose Difficulty, Enter hard or easy: ")
    if choice=='hard':
        return 5
    elif choice=='easy':
        return 10
    else:
        print("wrong input")
        game_difficulty()


def user_guess_diff(user_guess:int,rand_num:int):
    '''tells the how off the user guess  is '''
    if rand_num-user_guess>5:
        print(" guess is Too hogh")
        return
    else:
        print("guess is too low")
        return
        


def game_loop(rand_num:int,choices:int):
    '''actual game loop'''
    for i in range(choices):
        print(f"You have {choices-i} tries left")
        print(rand_num)
        user_guess=int(input("Guess a number: "))
        if user_guess==rand_num:
            print("You guessed right!!!")
            if input("Do you want to continue: ")=='yes':
                game_loop(random_number_generator(),game_difficulty())
            else:
                return      
        else:
            user_guess_diff(user_guess=user_guess,rand_num=rand_num)
    print("You lost")
    if input("Do you want to continue(type yes):  ")=='yes':
        game_loop(random_number_generator(),game_difficulty())
    else:
        return











# game loop:
game_loop(random_number_generator(),game_difficulty())

