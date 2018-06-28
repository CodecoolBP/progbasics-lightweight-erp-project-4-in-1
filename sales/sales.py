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
# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual sale price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the sale was made
# customer_id: string, id from the crm

# importing everything you need
import os
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def table_structure():
    table_struct = ['id ', 'title ', 'price ', 'month ', 'day ', 'year ']
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
                    "Check items sold between a given date",
                    "Get title by id",
                    "Get title by id from table",
                    "Get the last sold item's id",
                    "Get the last sold item's id from table",
                    "Get the last sold item's title from table",
                    "Get the sum of prices by ids",
                    "Get the sum of prices from table by ids",
                    "Get customer ID by sale ID",
                    "Get customer ID by sale ID from table",
                    "Get all customer IDs",
                    "Get all customer IDs from table",
                    "Get all sales IDs for customer IDs",
                    "Get all sales IDs for customer IDs from table",
                    "Get num of sales per customer IDs",
                    "Get num of sales per customer IDs from table"]
        
        ui.print_menu("Sales menu", sub_options, "Main menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(sales_table, table_structure())
        elif option == "2":
            add(sales_table)
        elif option == "3":
            id_input = ui.get_inputs(["Please give an id: "], "")
            remove(sales_table, id_input[0])
        elif option == "4":
            id_input = ui.get_inputs(["Please give an id: "], "")
            update(sales_table, id_input[0])
        elif option == "5":
            ui.print_result(get_lowest_price_item_id(sales_table), "What is the id of the item that was sold for the lowest price?")
        elif option == "6":
            inputs = ui.get_inputs(["Year from: ", "Month from: ", "Day from: ", "Year to: ", "Month to: ", "Day to: "], "Please give the following data:")
            get_items_sold_between(sales_table, int(inputs[1]), int(inputs[2]), int(inputs[0]), int(inputs[4]), int(inputs[5]), int(inputs[3]))
        elif option == "7":
            id_input = ui.get_inputs(["Please give an id: "], "")
            get_title_by_id(id_input[0])
        elif option == "8":
            id_input = ui.get_inputs(["Please give an id: "], "")
            get_title_by_id_from_table(sales_table, id_input[0])
        elif option == "9":
            ui.print_result(get_item_id_sold_last(), "What is the most recently sold item's id?")
        elif option == "10":
            get_item_id_sold_last_from_table(sales_table)
        elif option == "11":
            get_item_title_sold_last_from_table(sales_table)
        elif option == "12":
            id_input = ui.get_inputs(["Please give an id: "], "")
            get_the_sum_of_prices(id_input)
        elif option == "13":
            id_input = ui.get_inputs(["Please give an id: "], "")
            ui.print_result(get_the_sum_of_prices_from_table(sales_table, id_input), "What is the total of given ids' prices?")
        elif option == "14":
            id_input = ui.get_inputs(["Please give an id: "], "")
            ui.print_result(get_customer_id_by_sale_id(id_input[0]), "The ID of the person who bought this game: ")
        elif option == "15":
            id_input = ui.get_inputs(["Please give an id: "], "")
            ui.print_result(get_customer_id_by_sale_id_from_table(id_input[0]), "The ID of the person who bought this game: ")
        elif option == "16":
            ui.print_result(get_all_customer_ids(), "These are all the customer IDs: ")
        elif option == "17":
            ui.print_result(get_all_customer_ids_from_table(), "These are all the customer IDs: ")
        elif option == "18":
            get_all_sales_ids_for_customer_ids()
        elif option == "19":
            get_all_sales_ids_for_customer_ids_form_table(sales_table)
        elif option == "20":
            ui.print_result(get_num_of_sales_per_customer_ids(), "The num of all sales for their IDs")
        elif option == "21":
            ui.print_result(get_num_of_sales_per_customer_ids_from_table(sales_table), "The num of all sales for their IDs")
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
    data_manager.write_table_to_file('sales/sales.csv', extended_table)
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
    data_manager.write_table_to_file("sales/sales.csv", cut_table)

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
    data_manager.write_table_to_file('sales/sales.csv', update_table)

    return update_table


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
    
    month_from, day_from, year_from = str(month_from), str(day_from), str(year_from)
    month_to, day_to, year_to = str(month_to), str(day_to), str(year_to)
    if len(month_from) == 1:
        month_from = "0" + month_from
    if len(day_from) == 1:
        day_from= "0" + day_from
    if len(month_to) == 1:
        month_to = "0" + month_to
    if len(day_to) == 1:
        day_to = "0" + day_to
    start_date = year_from + month_from + day_from
    end_date = year_to + month_to + day_to
    result_dict = {}
    result_indecies = []
    final = []
    for i, sublist in enumerate(table):
        result_dict[str(i)] = sublist[5]
        if len(sublist[3]) == 1:
            result_dict[str(i)] += "0" + sublist[3]
        else:
            result_dict[str(i)] += sublist[3]
        if len(sublist[4]) == 1:
            result_dict[str(i)] += "0" + sublist[4]
        else:
            result_dict[str(i)] += sublist[4]
    for key, value in result_dict.items():
        if value >= start_date and value <= end_date:
            result_indecies.append(key)
    for i, sublist in enumerate(table):
        for index in result_indecies:
            if i == int(index):
                final.append(sublist)
    return ui.print_result(final, "Which items are sold between two given dates?")

# functions supports data abalyser
# --------------------------------

# INNENTŐL

def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str the title of the item
    """

    result = None
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    for sublist in sales_table:
        if id == sublist[0]:
            result = sublist[1]
    return result
    return ui.print_result(None, "What title belongs to the given id?")


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str the title of the item
    """
    result = None
    for sublist in table:
        if id == sublist[0]:
            result = sublist[1]
    return result
    return ui.print_result(None, "What title belongs to the given id?")


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    result_dict = {}
    for sublist in sales_table:
        result_dict[sublist[0]] = sublist[5]
        if len(sublist[3]) == 1:
            result_dict[sublist[0]] += "0" + sublist[3]
        else:
            result_dict[sublist[0]] += sublist[3]
        if len(sublist[4]) == 1:
            result_dict[sublist[0]] += "0" + sublist[4]
        else:
            result_dict[sublist[0]] += sublist[4]
    result_value = max(result_dict.values())
    result_key = [k for k,v in result_dict.items() if v == result_value]
    return result_key[0]
    

def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _id_ of the item that was sold most recently.
    """

    result_dict = {}
    for sublist in table:
        result_dict[sublist[0]] = sublist[5]
        if len(sublist[3]) == 1:
            result_dict[sublist[0]] += "0" + sublist[3]
        else:
            result_dict[sublist[0]] += sublist[3]
        if len(sublist[4]) == 1:
            result_dict[sublist[0]] += "0" + sublist[4]
        else:
            result_dict[sublist[0]] += sublist[4]
    result_value = max(result_dict.values())
    result_key = [k for k,v in result_dict.items() if v == result_value]
    return result_key[0]
    return ui.print_result(result_key[0], "What is the most recently sold item's id?")


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        (str) the _title_ of the item that was sold most recently.
    """

    result_dict = {}
    for sublist in table:
        result_dict[sublist[1]] = sublist[5]
        if len(sublist[3]) == 1:
            result_dict[sublist[1]] += "0" + sublist[3]
        else:
            result_dict[sublist[1]] += sublist[3]
        if len(sublist[4]) == 1:
            result_dict[sublist[1]] += "0" + sublist[4]
        else:
            result_dict[sublist[1]] += sublist[4]
    result_value = max(result_dict.values())
    result_key = [k for k,v in result_dict.items() if v == result_value]
    return result_key[0]
    return ui.print_result(result_key[0], "What is the most recently sold item's title?")


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    items = [i.split(', ') for i in item_ids]
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    sum_of_prices = 0
    for sublist in sales_table:
        for elem in items[0]:
            if elem == sublist[0]:
                sum_of_prices += int(sublist[2])
            else:
                continue
    return sum_of_prices            
    return ui.print_result(sum_of_prices, "What is the total of given ids' prices?")


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        (number) the sum of the items' prices
    """

    items = [i.split(', ') for i in item_ids]
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    sum_of_prices = 0
    for sublist in sales_table:
        for elem in items[0]:
            if elem == sublist[0]:
                sum_of_prices += int(sublist[2])
            else:
                continue
    return sum_of_prices
    

'''START FCKIN HERE !!!!
'''
# EDDIG!!!!!!!!

def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
         sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """

    person = ""
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    for customer in sales_table:
        if sale_id == customer[0]:
            person = str(customer[6])
    return person
    

def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
         customer_id that belongs to the given sale id
    """
    person = ""
    for customer in table:
        if sale_id == customer[0]:
            person = str(customer[6])
    return person


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.
    Returns a set of customer_ids that are present in the table.
    Returns:
         set of customer_ids that are present in the table
    """

    all_customer_ids = []
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    for ids in sales_table:
        all_customer_ids.append(ids[6])
    return all_customer_ids


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.
    Args:
        table (list of list): the sales table
    Returns:
         set of customer_ids that are present in the table
    """

    all_customer_ids = set()
    for ids in sales_table:
        all_customer_ids.add(ids[6])
    return all_customer_ids
    

def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
    # not finished
    ids = {}
    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    for sublist in sales_table:
        if sublist[6] not in ids:
            ids[sublist[6]] = sublist[0]
        else:
            ids[sublist[6]] += sublist[0]
    return ids


def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code

    pass


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    sales_table = data_manager.get_table_from_file('sales/sales.csv')
    num_of_sales = {}
    for record in sales_table:
        if record[6] not in num_of_sales:
            num_of_sales[record[6]] = 0
    for rec in sales_table:
        for id_ in num_of_sales:
            if id_ == rec[6]:
                num_of_sales[id_] += 1
    return num_of_sales
    
    
def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    num_of_sales = {}
    for record in table:
        if record[6] not in num_of_sales:
            num_of_sales[record[6]] = 0
    for rec in table:
        for id_ in num_of_sales:
            if id_ == rec[6]:
                num_of_sales[id_] += 1
    return num_of_sales
