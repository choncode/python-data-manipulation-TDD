"""The format_staff function should accept a list of dictionaries 
representing staff data and a list of dictionaries representing 
the new department data.

The file is run by calling this module with the python keyword.

Example:
    python src/format_staff.py

To run the test file, please use the below:
    pytest test/test_format_staff.py
"""

def format_staff(staff_list, department_list):
    """Takes two arguments of lists of dictionaries and returns
    first_name, last_name and matching referenced department_id.

    Args:
        staff_list: A list of dictionaries.
        department_list: A list of dictionaries.

    Returns:
        A list of lists.
    """

    dept_value_lookup = {}
    for dict in department_list:
        dept_value_lookup[dict['department_name']] = dict['department_id']

    formatted_list = []
    for dict in staff_list:
        formatted_list.append([
            dict['first_name'],
            dict['last_name'], 
            dept_value_lookup[dict['department']]
        ]
        )

    return formatted_list