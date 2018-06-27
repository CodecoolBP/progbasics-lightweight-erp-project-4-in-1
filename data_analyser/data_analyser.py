# This module creates reports for marketing department.
# This module can run independently from other modules.
# Has no own datastructure but uses other modules.
# Avoud using the database (ie. .csv files) of other modules directly.
# Use the functions of the modules instead.

# todo: importing everything you need

# importing everything you need
import os
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
    User can access default special features from here.
    User can go back to main menu from here.

    Returns:
        None
    """

    while True:
        sub_options = ["Get the last buyer's name",
                        "Get the last buyer's id",
                        "Get the buyer's name spent most and the money spent",
                        "Get the buyer's id spent most and the money spent",
                        "Get the most frequent buyers names",
                        "Get the most frequent buyers id"]
        
        ui.print_menu("Data Analyzer menu", sub_options, "Main menu")

        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            ui.print_result(get_the_last_buyer_name(), "Who is the last sold item's owner?")
        elif option == "2":
            get_the_last_buyer_id()
        elif option == "3":
            get_the_buyer_name_spent_most_and_the_money_spent()
        elif option == "4":
            get_the_buyer_id_spent_most_and_the_money_spent
        elif option == "5":
            get_the_most_frequent_buyers_names()
        elif option == "6":
            get_the_most_frequent_buyers_ids
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        Customer name of the last buyer
    """
    # sales -> latest buyed item -> buyer id
    # crm buyer id -> buyer name

    sales_id = sales.get_item_id_sold_last()
    buyer_id = sales.get_customer_id_by_sale_id(sales_id)
    buyer_name = crm.get_name_by_id(buyer_id)
    return buyer_name
    # return ui.print_result(buyer_name, "Who is the last sold item's owner?")


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """

    # your code

    pass


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.
    Returns a tuple of customer name and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer name and the sum the customer spent
    """

    # your code

    pass


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """

    # your code

    pass


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customers' name) who bought most frequently.
    Returns an ordered list of tuples of customer names and the number of their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer names and num of sales
    """

    # your code

    pass


def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent.
    Returns an ordered list of tuples of customer id and the number their sales.
    (The first one bought the most frequent.)
    eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]

    Args:
        num: the number of the customers to return.

    Returns:
        Ordered list of tuples of customer ids and num of sales
    """

    # your code

    pass
