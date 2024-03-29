""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    list_of_title = []
    for item in title_list:
        list_of_title.append(item.upper())
    table.insert(0, list_of_title)
    length = len(table[0])
    mydict = {}
    for i in range(length):
        mydict[i] = 0
    for sublist in table:
        for i in range(length):
            if len(sublist[i]) > mydict.get(i):
                mydict[i] = len(sublist[i])
    total_length_of_row = sum(mydict.values())
    print("\n" + "*" * (total_length_of_row + length * 3))
    for sublist in table:
        for i in range(length):
            print(sublist[i].center(mydict.get(i)) + " |", end=' ')
        if table.index(sublist) == 0:
            print("\n" + "*" * (total_length_of_row + length * 3))
        else:    
            print("\n" + "-" * (total_length_of_row + length * 3))

 
    # THE OLDER ONE:
    # table.insert(0, title_list)
    # for i, d in enumerate(table):
    #     line = '|'.join(str(x).ljust(15) for x in d)
    #     print(line)
    #     if i == 0:
    #         print('*' * 90)
    #     else:
    #         print('-' * 90)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(label)
    if isinstance(result, list):
        for sublist in result:
            print(sublist)
    elif isinstance(result, dict):
        for key, val in result.items():
            print(key, val)
    else:
        print(result)


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(title)
    for option_index in range(len(list_options)):
        print('(', option_index+1, ')   ', list_options[option_index], sep='')
    print('(0)', exit_message, sep='\t')
    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for labels_index in range(len(list_labels)):
        input_data = input(list_labels[labels_index])
        inputs.append(input_data)
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print('Error: ' + message)
