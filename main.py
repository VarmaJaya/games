import turtle
import pandas
data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US_State_game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
all_states = data.state.tolist()

guessed_states =[]
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states", prompt="What's the next state in The US").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
new_list = []

for item in all_states:
    if item not in guessed_states:
        new_list.append(item)
df = pandas.DataFrame(new_list, columns=['states'])
df.to_csv("remaining_states.csv")

screen.exitonclick()