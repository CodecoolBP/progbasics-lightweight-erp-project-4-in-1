""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

def table_structure():
    table_struct = ['id', 'name', 'manufacturer', 'purchase_year', 'durability']
    return table_struct

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    while True:
        inventory_table = data_manager.get_table_from_file('inventory/inventory.csv')

        sub_options = ["Display inventory",
                    "Add a new console type",
                    "Remove a console type",
                    "Update a console",
                    "Available consoles (not yet available)",
                    "Average durability times by manufacturers (not yet available)"]
        
        ui.print_menu("Inventory menu", sub_options, "Main menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(inventory_table)
        elif option == "2":
            add(inventory_table)
        elif option == "3":
            id_input = ui.get_inputs(["Please give an id: "], "")
            remove(inventory_table, id_input[0])
        elif option == "4":
            id_input = ui.get_inputs(["Please give an id: "], "")
            update(inventory_table, id_input[0])
        elif option == "5":
            get_available_items(table)
        elif option == "6":
            get_average_durability_by_manufacturers
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")

def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    extended_table = common.add_general(table, table_structure())
    data_manager.write_table_to_file('inventory/inventory.csv', extended_table)
    
    return extended_table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    update_table = common.update_general(table, table_structure(), id_)
    data_manager.write_table_to_file('inventory/inventory.csv', update_table)

    return update_table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
