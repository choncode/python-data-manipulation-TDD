"""The format_stock function should accept a list of dictionaries 
in the following format and return a list containing 
the item_name and the amount.

The file is run by calling this module with the python keyword.

Example:
    python src/format_stock.py

To run the test file, please use the below:
    pytest test/test_format_stock.py
"""

def format_stock(list):
    """Takes a list of dictionaries and returns a list of lists 
    with the value of item_name and amount.

    Args:
        list: A list of dictionaries.

    Returns:
        A list of lists.
    """
    try:
        stock_amount = [[stock['item_name'], stock['amount']] for stock in list]
        return stock_amount
    except KeyError as error:
        return f'the passed dictionary is missing key {error}'


