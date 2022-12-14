import turtle
import pandas

# Step 1 - setup screen and background
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Step 2 - get the states' x, y positions
# This was already completed by Angela, see 50_stats.csv
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# Step 3 - Ask for user input
# answer_state = screen.textinput(title="Guess", prompt="Guess a state")
# put this on the step 6 loop
# guessed_states = []

# Step 4 - Import csv
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

# Step 5 - Match user input to csv
# all_states = data["state"].to_list()
# if answer_state in all_states:
#     t = turtle.Turtle()
#     t.hideturtle()
#     t.penup()
#     state_data = data[data["state"] == answer_state]
#     t.goto(int(state_data["x"]), int(state_data["y"]))
#     t.write(answer_state) # or from Pandas doc, use t.write(state_data.state.item())

# Step 6 - Create a loop
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct Guess", prompt="Guess a state").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_missed.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state) # or from Pandas doc, use t.write(state_data.state.item())

# Step 7 - exit the game with csv output of missed guesses



# Delete this exit on click and use turtle.mainloop()
# screen.exitonclick()