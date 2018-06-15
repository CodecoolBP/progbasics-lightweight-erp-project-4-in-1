""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def table_structure():
    table_struct = ['ID ','Name ','Year ']
    return table_struct


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    hr_table = data_manager.get_table_from_file('hr/persons.csv')

    sub_options =  ["Show staff",
                    "Add person to staff",
                    "Remove person from staff",
                    "Update staff",
                    "Get oldest person",
                    "Get the most average old person"]
    
    ui.print_menu("HR menu", sub_options,"Main menu")

    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(hr_table)
    elif option == "2":
        add(hr_table)
    elif option == "3":
        id_input = ui.get_inputs(["Please give an id: "], "")
        remove(hr_table, id_input[0])
    elif option == "4":
        id_input = common.generate_random
        update(hr_table, id_input[0])
    elif option == "5":
        get_available_items(table)
    elif option == "6":
        get_average_durability_by_manufacturers
    elif option == "0":
        main.main()
    else:
        raise KeyError("There is no such option.")

def show_table(table): #key 1
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    extended_table = common.show_table_general(table)
    presented_table = data_manager.write_table_to_file('inventory/inventory.csv', extended_table)
    

    return presented_table

def add(table): #key2
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    extended_table = common.add_general(table,table_structure())
    data_manager.write_table_to_file('hr/persons.py',extended_table)
    
    return  extended_table


def remove(table, id_): #key3
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    cut_table = common.remove_general(table,id_)
    ui.print_table(cut_table, "Table without specified record")
    data_manager.write_table_to_file("hr/persons.csv",cut_table)

    return cut_table


def update(table, id_): #key4
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    update_process = common.update_general(table,id)
    updated_file = data_manager.write_table_to_file("hr/persons.csv",update_process)

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
