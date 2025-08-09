
from  support_func import clear_terminal , write_file, populate_todo_list , display_todo_list
import FreeSimpleGUI as sg
import os

current_location = os.getcwd()
# current_code_file_name = os.path.basename(__file__)
todo_file =os.path.join(current_location, 'data',"todo_file.txt")

sg.theme('DarkAmber')
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do action", key='todo')
add_button = sg.Button("Add")
# remove_button = sg.Button("Remove")
# edit_button = sg.Button("Edit")
# show_button = sg.Button("Show")
# clear_button = sg.Button("Clear")
exit_button = sg.Button("Quit")

# define the layout
my_layout = [[label],
             [input_box, add_button],
             [exit_button]]

# Create the window
window = sg.Window("My To-Do Application",
                   layout=my_layout,
                   font=('Helvetica', 20))
while True:
    clear_terminal()
    event, values = window.read()
    # if your want to Quit or close Windows
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = populate_todo_list(todo_file)
            print( "Add :- ", values['todo'])
            todo_list.append(values['todo']+'\n')
            write_file(todo_file, todo_list)
            print(todo_list)
        case "Quit" | sg.WIN_CLOSED :
            print("Closing the application")
            break
        case _:
            pass
    """
    if ((event == sg.WIN_CLOSED)  or ( event == "Quit") ):
        break
    """



# Finish up by removing from the screen
window.close()



