from turtle import Screen
from nameLocation import NameLocation
import pandas as pd

# initiate nameLocation class
nameLocation = NameLocation()

# Pull in states data
states_data = pd.read_csv("50_states.csv")
states = states_data["state"].to_list()
guessed_states = []

# Setup map screen
main_screen = Screen()
main_screen.setup(width=725, height=491)
main_screen.bgpic("blank_states_img.gif")

# Setup input screen
correct = 0
input_screen = Screen()
 
while correct < 50:
    state_input = input_screen.textinput(title=f"{correct}/50 States Correct", prompt="What's another state name?").title()
    if state_input in states:
        correct += 1
        guessed_states.append(state_input)
        x = int(states_data[states_data["state"] == state_input]["x"])
        y = int(states_data[states_data["state"] == state_input]["y"])
        state_location = (x, y)
        nameLocation.stateLocation(state_input, state_location)
    if state_input == "Exit":
        export = [state for state in states if state not in guessed_states]
        break



# export = {"states": []}

# for state in states:
#     if state not in guessed_states:
#         export["states"].append(state)

export_df = pd.DataFrame(export)
export_df.to_csv("missed_states.csv", index=False)
        
main_screen.exitonclick()