""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def table_structure():
    table_struct = ['id ', 'month ', 'day ', 'year', 'type ','amount ']
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
        items_table = data_manager.get_table_from_file('accounting/items.csv') #get from data manager
        
        sub_menu_points = ['Display transaction',
                            'Add new transcation',
                            'Remove transcation',
                            'Update transaction',
                            'Best profit year',
                            'Average amount']
        ui.print_menu("Accounting menu",sub_menu_points,"Main menu")
    
        inputs = ui.get_inputs(["Please enter a number: "], "")

        option = inputs[0]

        if option == "1": #display
            show_table(items_table) 
        elif option == "2": #add
            add(items_table)
        elif option == "3": #remove
            id_input = ui.get_inputs(["Please give an id: "], "")
            remove(items_table, id_input[0])
        elif option == "4": #update
            id_input = ui.get_inputs(["Please give an id: "], "")
            update(items_table, id_input[0])
        elif option == "5":
            ui.print_result(which_year_max(items_table),"The following year has the highest profit: ")
            #which_year_max(items_table)
        elif option == "6":
            year = int(input("Which year are you intrested in?: "))
            ui.print_result(avg_amount(items_table,year),"average (per item) profit in a given year: ")
            #avg_amount(items_table,year)
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
    ui.print_table(items_table)

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_tranasction = common.add_general(table,table_structure())
    data_manager.write_table_to_file('accounting/items.csv',new_tranasction)
    
    return table


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
    ui.print_table(cut_table, "Table without specified transaction")
    data_manager.write_table_to_file("hr/persons.csv",cut_table)

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

    

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    empty_dict = {}
    for record in table:
        if record[3] not in table:
            empty_dict[record[3]] = 0
    for rec in table:
        for year in empty_dict:
            if year == rec[3] and rec[4] == "in":
                empty_dict[year] += int(rec[5])
            elif year == rec[3] and rec[4] == "out":
                empty_dict[year] -= int(rec[5])
                
    highest_profit_year = max(empty_dict, key = empty_dict.get)
    final = str(highest_profit_year) + " has profit of: " +  str(empty_dict[highest_profit_year]) + " dollars"
    return final



def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """
    income = 0
    outcome = 0 

    for record in table:
        if year in record and "in" in record:
            profit += int(record[5])
        elif year in record and "out" in record:
            outcome += int(record[5])
    return (income - outcome)/len(table)

