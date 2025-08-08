
from  support_func import clear_terminal , write_file, populate_todo_list , display_todo_list
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do action")
add_button = sg.Button("Add")
# remove_button = sg.Button("Remove")
# edit_button = sg.Button("Edit")
# show_button = sg.Button("Show")
# clear_button = sg.Button("Clear")
exit_button = sg.Button("Quit")

# define the layout
my_layout = [[label], [input_box, add_button], [exit_button]]

# Create the window
window = sg.Window("My To-Do Application", layout=my_layout)
while True:
    event, values = window.read()
    # if your want to Quit or close Windows
    if (event == sg.WIN_CLOSED)  or event == "Quit":
        break



# Finish up by removing from the screen
window.close()



