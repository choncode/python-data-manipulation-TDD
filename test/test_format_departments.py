from src.format_departments import format_departments

dept_list = [
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
    ]

dept_list2 = [
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley'
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
    ]

dept_list3 = [
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
    },
        {
        'staff_id': 3,
        'first_name': 'Joe',
        'last_name': 'Mulvey',
        'department': 'Footwear'
    }
    ]

dept_list4 = [
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    },
        {
        'staff_id': 3,
        'first_name': 'Joe',
        'last_name': 'Mulvey'
    }
    ]



def test_returns_a_list_of_dictionaries_as_a_list():
    result = format_departments(dept_list)
    assert isinstance(result, list)

def test_returns_correct_values_from_argument():
    result = format_departments(dept_list)
    assert 'Beauty' in result[0]
    assert 'Footwear' in result[1]

def test_returns_values_in_nested_lists():
    result = format_departments(dept_list)
    assert len(result) == 2
    assert result[0] == ['Beauty']
    assert result[1] == ['Footwear']

def test_returns_error__with_index_if_dictionary_has_no_department_key():
    result = format_departments(dept_list2)
    assert result == 'dictionary at index 0 is missing a key of "department"'
    result = format_departments(dept_list3)
    assert result == 'dictionary at index 1 is missing a key of "department"'
    result = format_departments(dept_list4)
    assert result == 'dictionary at index 2 is missing a key of "department"'

"""The below test is commented out because it can only be used
with the commented out code for the simpler error handling
"""
# def test_returns_error_if_dictionary_has_no_department_key():
#     result = format_departments(dept_list2)
#     assert result == 'a passed dictionary is missing a key of department'


