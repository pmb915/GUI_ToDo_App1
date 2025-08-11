
from  support_func import clear_terminal , write_file, populate_todo_list , display_todo_list
import FreeSimpleGUI as sg
import os
import time

current_location = os.getcwd()
# current_code_file_name = os.path.basename(__file__)
todo_file =os.path.join(current_location, 'data',"todo_file.txt")

if not os.path.exists(todo_file):
    with open(todo_file, 'w') as f:
        f.write('')

# defining class for custom error message
class MyCustomError(Exception):
    """
    Custom exception raised for specific error scenarios.
    Attributes:
        message -- explanation of the error
        value -- optional value related to the error
    """
    def __init__(self, message, value=None):
        self.message = message
        self.value = value
        super().__init__(self.message) # Pass the message to the base Exception class


#sg.theme('DarkAmber')
sg.theme('LightGreen')
current_time = ''
clock_label = sg.Text(current_time, key='clock')
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do action", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(tooltip="Display and let select ToDo's for edit/removal",
                      size=(44,8), key='todolist', enable_events=True,
                      values=populate_todo_list(todo_file))
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")

# show_button = sg.Button("Show")
# clear_button = sg.Button("Clear")
exit_button = sg.Button("Quit")

# define the layout
my_layout = [[clock_label],
             [label],
             [input_box, add_button],
             [list_box,
              [edit_button , remove_button]],
             [exit_button]]

# Create the window
window = sg.Window("My To-Do Application",
                   layout=my_layout,
                   font=('Helvetica', 20))
while True:
    clear_terminal()
    event, values = window.read(timeout= 10)
    current_time = time.strftime("%b %d, %Y %H:%M:%S")
    window['clock'].update(current_time)
    # if your want to Quit or close Windows
    print(event)
    print(values)
    match event:
        case "Add":
            try:
                todo_list = populate_todo_list(todo_file)
                print( "Add :- ", values['todo']+'\n')
                if values['todo'].strip() != '':
                    new_item = values['todo']+'\n'
                    index_to_add = todo_list.index(new_item)
                    # print('Index to add:', index_to_add)
                    # print(f"Todo item : {new_item.strip('\n')}, is already exists!!")
                    mesg = f"Todo item : {new_item.strip('\n')}, is already exists!!"
                    sg.popup(mesg, title="Error", font=('Helvetica', 20))
                else:
                    raise MyCustomError("Error: Blank cannot be added !")

            except MyCustomError as e:
                sg.popup(e.message, title="Error", font=('Helvetica', 200))
            except ValueError:
                # print('Index to add:', index_to_add)
                todo_list.append(new_item)
                write_file(todo_file, todo_list)
                window['todolist'].update(values=todo_list)
                window['todo'].update(value='')
                print(todo_list)



        case "Edit":
            try:
                # item_to_edit = values['todolist'][0].replace('\n','')
                item_to_edit = values['todolist'][0]
                new_item = values['todo']
                if '\n' in new_item:
                    new_item = new_item.replace('\n', '')
                new_item = new_item +'\n'
                todo_list = populate_todo_list(todo_file)
                # print(todo_list)
                index_to_edit = todo_list.index(item_to_edit)
                todo_list[index_to_edit] = new_item
                write_file(todo_file, todo_list)
                print(f"item_to_edit = {item_to_edit.strip('\n')}, is replaced with: {new_item.strip('\n')}")
                # values['todo']
                window['todolist'].update(values=todo_list)
                window['todo'].update(value='')
            except Exception as e:
                mesg = f"Error: {e}"
                print(mesg)
                sg.popup(mesg, title="Error", font=('Helvetica', 20))
        case "Remove":
            try:
                # item_to_edit = values['todolist'][0].replace('\n','')
                item_to_remove = values['todolist'][0]
                todo_list = populate_todo_list(todo_file)
                index_to_remove = todo_list.index(item_to_remove)
                todo_list.remove(item_to_remove)
                write_file(todo_file, todo_list)
                # print(f"item_to_remove = {item_to_remove.strip('\n')}, is removed!")
                window['todolist'].update(values=todo_list)
                window['todo'].update(value='')
            except Exception as e:
                mesg = f"Error: {e}"
                sg.popup(mesg, title="Error" , font=('Helvetica', 20))

        case 'todolist' :
            window['todo'].update(value = values['todolist'][0])

        case "Quit" | sg.WIN_CLOSED :
            print("Closing the application")
            exit(0)
        case _:
            pass
    """
    if ((event == sg.WIN_CLOSED)  or ( event == "Quit") ):
        break
    """



# Finish up by removing from the screen
window.close()



