from turtle import Screen, Turtle
import turtle
import pandas as pd

states_data=pd.read_csv("50_states.csv")
all_states=states_data["state"].tolist()


image="blank_states_img.gif"


screen=Screen()
screen.title("U.S states game")
screen.addshape(image)
turtle.shape(image)

guesse_states=[]
while len(guesse_states)<50:
    user_ans=screen.textinput(f"Guess the state({len(guesse_states)}/50)","Whats anotoher states name?").title()
    if user_ans=="Exit":
        break
    if user_ans in all_states:
        sd=states_data[states_data["state"]==user_ans]
        tim=Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(sd.x),int(sd.y))
        tim.write(user_ans)
        guesse_states.append(user_ans)


not_guessed=states_data[states_data["state"].isin(list(set(all_states)-set(guesse_states)))].to_csv("not_guessed")
print(not_guessed)



turtle.mainloop()




