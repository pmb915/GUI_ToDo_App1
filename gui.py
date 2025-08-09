
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
list_box = sg.Listbox(tooltip="Display and let select ToDo's for edit/removal",
                      size=(44,8), key='todolist', enable_events=True,
                      values=populate_todo_list(todo_file))
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")

# show_button = sg.Button("Show")
# clear_button = sg.Button("Clear")
exit_button = sg.Button("Quit")

# define the layout
my_layout = [[label],
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
    event, values = window.read()
    # if your want to Quit or close Windows
    print(event)
    print(values)
    match event:
        case "Add":
            todo_list = populate_todo_list(todo_file)
            print( "Add :- ", values['todo']+'\n')
            new_item = values['todo']+'\n'
            try:
                index_to_add = todo_list.index(new_item)
                print('Index to add:', index_to_add)
                print(f"Todo item : {new_item.strip('\n')}, is already exists!!")
            except ValueError:
                # print('Index to add:', index_to_add)
                todo_list.append(new_item)
                write_file(todo_file, todo_list)
                window['todolist'].update(values=todo_list)
                print(todo_list)


        case "Edit":
            # item_to_edit = values['todolist'][0].replace('\n','')
            item_to_edit = values['todolist'][0]
            new_item = values['todo']+'\n'
            todo_list = populate_todo_list(todo_file)
            # print(todo_list)
            try:
                index_to_edit = todo_list.index(item_to_edit)
                todo_list[index_to_edit] = new_item
                write_file(todo_file, todo_list)
                print(f"item_to_edit = {item_to_edit.strip('\n')}, is replaced with: {new_item.strip('\n')}")
                values['todo']
                window['todolist'].update(values=todo_list)
                # window['todo'].update(values=None)
            except ValueError as e:
                print(f"Error: {e}")
        case "Remove":
            # item_to_edit = values['todolist'][0].replace('\n','')
            item_to_remove = values['todolist'][0]
            todo_list = populate_todo_list(todo_file)
            try:
                index_to_remove = todo_list.index(item_to_remove)
                todo_list.remove(item_to_remove)
                write_file(todo_file, todo_list)
                print(f"item_to_remove = {item_to_remove.strip('\n')}, is removed!")
                window['todolist'].update(values=todo_list)
                window['todo'].update(value='')
            except Exception as e:
                print(f"Error: {e}")
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



