"""The format_departments function should accept a list of 
dictionaries in the following format and return a list of lists 
containing the department_name.

The file is run by calling this module with the python keyword.

Example:
    python src/format_departments.py

To run the test file, please use the below:
    pytest test/test_format_departments.py
"""

def format_departments(list):
    """Takes a list of dictionaries and returns a list of lists 
    with each value of the key 'department'.

    Args:
        list: A list of dictionaries.

    Returns:
        A list of lists.
    """

    """Below is a more complex for loop to implement error handling
    and to inform the user exactly which index of the dictionary 
    iterated, is missing the key.
    """
    
    dept_name_list = []
    for index_no, dict in enumerate(list, start=0):
        print(index_no)
        try:
            dept_name_list.append([dict['department']])
        except KeyError:
            return f'dictionary at index {index_no} is missing a key of "department"'


    """Below is a more simple comprehension with basic error handling
    functionality, informing of the missing key.
    """
    
    # try:
    #     dept_name_list = [[name['department']] for name in list]
    #     return dept_name_list
    # except KeyError:
    #     return 'a passed dictionary is missing a key of department'

    return dept_name_list
