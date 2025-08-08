"""
# module for todo application
"""
import os

def clear_terminal():
    """
    Clears the terminal screen based on the operating system.
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def populate_todo_list(todo_file):
    """
    # read todo_file and populate todo list
    :return:
    """
    try:
        with open(todo_file, 'r') as fp:
            todo_list = fp.readlines()
    except FileNotFoundError:
        todo_list = []
    return todo_list
#
def write_file(mfile, lst):
    """
    :param mfile:
    :param lst:
    :return: None
    populates todo_list
    """
    with open(mfile, 'w') as fptr:
        fptr.writelines(lst)

#
def display_todo_list(lst):
    """
    :Accepts list as a parameter and displays each item with index position:
    :return None:
    """
    for index, item in enumerate(lst):
        print(f"position: {index} - todo: {item.strip('\n')}")

if __name__ == '__main__':
    clear_terminal()
    print(f"Hello: {__name__}, filename is : {__file__}")