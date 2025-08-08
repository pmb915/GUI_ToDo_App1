"""
Author: Parashar
Date: 4 Aug 2025
Program to create do list via command line

"""

import os
import datetime
import logging
import time
now = time.strftime("%b %d, %Y %H:%M:%S", time.localtime())
print("It is", now, "\n")
from support_func import clear_terminal , write_file, populate_todo_list , display_todo_list


# logging.debug("This is a debug message.")
# logging.info("This is an informational message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# location and filename
current_location = os.getcwd()
current_code_file_name = os.path.basename(__file__)
todo_file =os.path.join(current_location, 'data',"todo_file.txt")
log_file = os.path.join(current_location, 'data',"log_file.txt")
# basic config for logging

logging.basicConfig(filename=log_file,
                    filemode = 'a',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(message)s')

#create logger with 'app_name'
logger = logging.getLogger('todo_application')
#logger.setLevel(logging.INFO)
fh = logging.FileHandler(log_file)
fh.setLevel(logging.INFO)
logger.addHandler(fh)

# ger.info('Beginning todo application')

clear_terminal()
print(f"Current folder location: {current_location}")
print(f"Current file name: {current_code_file_name}")
print (f"todo_file name: {todo_file}")

user_action_prompt = "Type one of --> 'add', 'edit' ,'complete'/'remove',  'show'/'display' , 'quit' : "
prompt = "Enter a todo action ('QUIT' to quit): "

# Continuous loop
todo_list = populate_todo_list(todo_file)
while True:
    clear_terminal()
    """
    Accept user input to perform action and let user manages action list
    """
    user_action = input(user_action_prompt)
    match user_action.strip().lower():
        case 'add':
            user_text = input(prompt)
            msg = f"todo item - '{user_text}' is added"
            todo_list.append(user_text +'\n')
            logger.info(msg)
            print(msg)
            write_file(todo_file, todo_list)
        case 'edit':
            todo_list = populate_todo_list(todo_file)
            if todo_list:
                display_todo_list(todo_list)
                number = int(input("Enter the position for item to edit:"))
                if number < len(todo_list):
                    new_todo = input("Enter todo action to modify:")
                    todo_list[number] = new_todo+'\n'
                    msg=f"todo at position {number} is modified"
                    #print(msg)
                    logger.info(msg)
                    write_file(todo_file, todo_list)

                else:
                    msg=f"No item to modify at position {number}"
                    logger.info(msg)
                    print(msg)
                    continue
            else:
                print("No item in todo list for edit")
                continue
        case 'complete' | 'remove':
            todo_list = populate_todo_list(todo_file)
            if todo_list:
                display_todo_list(todo_list)
                number = int(input("Enter the position for item to complete/remove:"))
                # new_todo = input("Enter todo action to modify:")
                if number < len(todo_list):
                    x=todo_list.pop(number)
                    msg = f"todo item '{x.strip('\n')}' at position {number} is removed"
                    print(msg)
                    logger.info(msg)
                    write_file(todo_file, todo_list)
                else:
                    msg = f"item at position {number}, does not exists"
                    print(msg)
                    logger.info(msg)
                    continue
            else:
                print("No item in todo list for removal")
                continue

        case 'show' | 'display':
            display_todo_list(todo_list)
            continue
        case 'quit':
            msg ='todo application - execution ends'
            print(msg)
            logger.info(msg)
            break
        case _:
            print("Unknown command!!")

exit(0)



