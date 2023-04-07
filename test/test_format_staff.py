from src.format_staff import format_staff

staff_list =[
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    }, {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
    ]

department_list =[
    {
        'department_id': 1,
        'department_name':'Beauty'
    }, {
        'department_id': 2,
        'department_name':'Footwear'
    }
    ]

def test_returns_a_list_of_dictionaries_as_a_list():
    result = format_staff(staff_list, department_list)
    assert isinstance(result, list)

def test_returns_correct_value_from_first_name():
    result = format_staff(staff_list, department_list)
    assert 'Duncan' in result[0]
    assert 'Cat' in result[1]

def test_returns_correct_value_from_last_name():
    result = format_staff(staff_list, department_list)
    assert 'Hoang' in result[1]

def test_returns_correct_value_from_department_id():
    result = format_staff(staff_list, department_list)
    assert 1 in result[0]
    assert 2 in result[1]


