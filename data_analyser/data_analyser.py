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
            ui.print_result(get_the_last_buyer_id(), "What is the last buyer's id?")
        elif option == "3":
            ui.print_result(get_the_buyer_name_spent_most_and_the_money_spent(), "Which buyer (name) spent the most, and how much is it?")
        elif option == "4":
            ui.print_result(get_the_buyer_id_spent_most_and_the_money_spent, "Which buyer (id) spent the most, and how much is it?")
        elif option == "5":
            ui.print_result(get_the_most_frequent_buyers_names(), "Who are the most frequent buyers (names)?")
        elif option == "6":
            ui.print_result(get_the_most_frequent_buyers_ids(), "Who are the most frequent buyers (ids)?")
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


def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        Customer id of the last buyer
    """

    sales_id = sales.get_item_id_sold_last()
    buyer_id = sales.get_customer_id_by_sale_id(sales_id)
    return buyer_id


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.
    Returns a tuple of customer name and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer name and the sum the customer spent
    """

    max_spent_money_cust_id = None
    max_spent_money = 0
    cust_id_sales_id = sales.get_all_sales_ids_for_customer_ids()
    for key, value in cust_id_sales_id.items():
        sum_of_one_cust = sales.get_the_sum_of_prices(value)
        if sum_of_one_cust > max_spent_money:
            max_spent_money = sum_of_one_cust
            max_spent_money_cust_id = key
    max_spent_money_cust_name = crm.get_name_by_id(max_spent_money_cust_id)
    return max_spent_money_cust_name


def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.
    Returns a tuple of customer id and the sum the customer spent.
    eg.: (aH34Jq#&, 42)

   Returns:
        Tuple of customer id and the sum the customer spent
    """

    max_spent_money_cust_id = None
    max_spent_money = 0
    cust_id_sales_id = sales.get_all_sales_ids_for_customer_ids()
    for key, value in cust_id_sales_id.items():
        sum_of_one_cust = sales.get_the_sum_of_prices(value)
        if sum_of_one_cust > max_spent_money:
            max_spent_money = sum_of_one_cust
            max_spent_money_cust_id = key
    return max_spent_money_cust_id


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

    # {'kH14Jt#&': 8, 'jH34Jk#&': 11, 'kH14Jh#&': 1}
    cust_id_and_sum_of_buyed_items = sales.get_num_of_sales_per_customer_ids()
    for key, value in sorted(cust_id_and_sum_of_buyed_items.items(), key=lambda x: x[1], reverse=True)[num:]:
        del cust_id_and_sum_of_buyed_items[key]
    cust_ids = list(cust_id_and_sum_of_buyed_items)
    cust_names = []
    for elem in cust_ids:
        cust_name = crm.get_name_by_id(elem)
        cust_names.append(cust_name)
    for key, val in cust_id_and_sum_of_buyed_items.items():
        i = 1
        cust_names.insert(i, val)
    return cust_names


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
    # {'kH14Jt#&': 8, 'jH34Jk#&': 11, 'kH14Jh#&': 1}
    cust_id_and_sum_of_buyed_items = sales.get_num_of_sales_per_customer_ids()
    for key, value in sorted(cust_id_and_sum_of_buyed_items.items(), key=lambda x: x[1], reverse=True)[num:]:
        del cust_id_and_sum_of_buyed_items[key]
    # result_list = []
    # result_list.append(set(cust_id_and_sum_of_buyed_items.items()))
    # return result_list
    return cust_id_and_sum_of_buyed_items

