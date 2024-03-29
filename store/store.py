""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def table_structure():
    table_struct = ['id ', 'title ', 'manufacturer ', 'price ', 'in_stock ']
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
        store_table = data_manager.get_table_from_file('store/games.csv')

        sub_options = ["Display games",
                    "Add new game",
                    "Remove a game",
                    "Update a game",
                    "Check how many games each manufacturers has",
                    "Check the average amount of games in stock of a manufacturer"]
        
        ui.print_menu("Store menu", sub_options, "Main menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(store_table, table_structure())
        elif option == "2":
            add(store_table)
        elif option == "3":
            id_input = ui.get_inputs(["Please give an id: "], "")
            remove(store_table, id_input[0])
        elif option == "4":
            id_input = ui.get_inputs(["Please give an id: "], "")
            update(store_table, id_input[0])
        elif option == "5":
            ui.print_result(get_counts_by_manufacturers(store_table), "How many different kinds of game are available of each manufacturer?")
        elif option == "6":
            manufacturer_input = ui.get_inputs(["Please give a manufacturer: "], "")
            ui.print_result(get_average_by_manufacturer(store_table, manufacturer_input[0]), "What is the average amount of games in stock of a given manufacturer?")
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")


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
    data_manager.write_table_to_file('store/games.csv', extended_table)
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

    cut_table = common.remove_general(table,id_)
    ui.print_table(cut_table, "Table without specified record")
    data_manager.write_table_to_file("store/games.csv", cut_table)

    return cut_table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    update_table = common.update_general(table, table_structure(), id_)
    data_manager.write_table_to_file('store/games.csv', update_table)

    return update_table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    games_manufacturers = {}
    for sublist in table:
        if sublist[2] not in games_manufacturers.keys():
            games_manufacturers[sublist[2]] = 1
        else:
            games_manufacturers[sublist[2]] += 1
    return games_manufacturers



def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    total_stock = 0
    number_of_games = 0
    for sublist in table:
        if manufacturer in sublist:
            number_of_games += 1
            total_stock += int(sublist[4])
    result = total_stock / number_of_games
    return result

