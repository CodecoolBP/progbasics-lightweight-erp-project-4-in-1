""" Common module
implement commonly used functions here
"""

import random
import ui


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    while True:
        generated = chr(random.randint(35,38)) + chr(random.randint(35,38)) + \
        chr(random.randint(48,57)) + chr(random.randint(48,57)) + \
        chr(random.randint(65,90)) + chr(random.randint(65,90)) + \
        chr(random.randint(97,122)) + chr(random.randint(97,122))

        exists = False
        for row in table:
            if str(row[0]) == generated:
                exists = True
                break
        if not exists:
            return generated


def add_general(table, table_structure):
    new_item = ui.get_inputs(table_structure[1:], "Please provide datas:")
    new_item.insert(0, generate_random(table))
    table.append(new_item)
    return table


def update_general(table, table_structure, id_):
    update_item = ui.get_inputs(table_structure[1:], "Please provide datas:")
    update_item.insert(0, id_)

    for index in range(len(table)):
        if str(table[index][0]) == id_:
            table[index] = update_item
    print(table)
    return table
    
