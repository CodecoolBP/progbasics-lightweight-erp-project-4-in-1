""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def table_structure():
    table_struct = ['id ', 'name ', 'email ', 'subscribed ']
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
        crm_table = data_manager.get_table_from_file('crm/customers.csv')

        sub_options = ["Display crm table",
                    "Add a new customer",
                    "Remove a customer",
                    "Update a customer",
                    "Id of the longest name",
                    "List of subscribed customers",
                    "Get name by id",
                    "Get name by id from table"]
        
        ui.print_menu("Customer Relationship Management menu", sub_options, "Main menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(crm_table)
        elif option == "2":
            add(crm_table)
        elif option == "3":
            id_input = ui.get_inputs(["Please give an id: "], "")
            remove(crm_table, id_input[0])
        elif option == "4":
            id_input = ui.get_inputs(["Please give an id: "], "")
            update(crm_table, id_input[0])
        elif option == "5":
            ui.print_result(get_longest_name_id(crm_table), "What is the id of the customer with the longest name?")    
        elif option == "6":
            ui.print_result(get_subscribed_emails(crm_table), 'Which customers has subscribed to the newsletter?')           
        elif option == "7":
            id_input = ui.get_inputs(["Please give an id: "], "")
            ui.print_result(get_name_by_id(id_input[0]), "What name belongs to the given id?")
        elif option == "8":
            id_input = ui.get_inputs(["Please give an id: "], "")
            ui.print_result(get_name_by_id_from_table(crm_table, id_input[0]), "What name belongs to the given id?")
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

    ui.print_table(table, table_structure())


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    extended_table = common.add_general(table, table_structure())
    data_manager.write_table_to_file('crm/customers.csv', extended_table)
    

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
    ui.print_table(cut_table, "Table without specified record")
    data_manager.write_table_to_file("crm/customers.csv", cut_table)

    return cut_table


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
    data_manager.write_table_to_file('crm/customers.csv', update_table)

    return update_table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """
    max_name, name_id = 'a', None
    
    for row in table:
        if len(row[1]) > len(max_name):
            max_name = row[1]
            name_id = row[0]
        elif len(row[1]) == len(max_name) and row[1] > max_name:
            max_name = row[1]
            name_id = row[0]
    return name_id


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """
    subscribed_emails = []

    for row in table:
        if row[3] == '1':
            subscribed_emails.append(row[2]+'\t'+ '\t'+ row[1])
    return subscribed_emails


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    crm_table = data_manager.get_table_from_file('crm/customers.csv')
    result = None
    for sublist in crm_table:
        if id == sublist[0]:
            result = sublist[1]
    return result


def get_name_by_id_from_table(table, id):

    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str the name of the customer
    """

    result = None
    for sublist in table:
        if id == sublist[0]:
            result = sublist[1]
    return result
    