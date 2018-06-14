""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def table_structure():
    table_struct = ['id', 'title', 'price', 'month', 'day', 'year']
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
        sales_table = data_manager.get_table_from_file('sales/sales.csv')

        sub_options = ["Display sales",
                    "Add new sold game",
                    "Remove sold game",
                    "Update sold game",
                    "Check sold with the lowest price ",
                    "Check items sold between a given date"]
        
        ui.print_menu("Sales menu", sub_options, "Main menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(sales_table, table_struct)
        elif option == "2":
            add(sales_table)
        elif option == "3":
            id_input = ui.get_inputs(["Please give an id: "], "")
            remove(sales_table, id_input[0])
        elif option == "4":
            id_input = ui.get_inputs(["Please give an id: "], "")
            update(sales_table, id_input[0])
        elif option == "5":
            print(get_lowest_price_item_id(sales_table))
        elif option == "6":
            inputs = ui.get_inputs(["Please give the following data: "], "")
            get_items_sold_between(sales_table, inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5])
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
    # your code


def show_table(table, table_structure):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, table_structure)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    extended_table = common.add_general(table, table_structure())
    data_manager.write_table_to_file('sales.csv', extended_table)
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

    # your code

    return table


# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    lowest_price = 0
    id_code = None
    for sublist in table:
        if int(sublist[2]) > int(lowest_price):
            lowest_price = int(sublist[2])
            id_code = sublist[0]
    return id_code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
