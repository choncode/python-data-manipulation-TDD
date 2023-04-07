from src.format_stock import format_stock

stock_list = [
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, 
    {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount': 10
    }
    ]

stock_list_2 = [
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount': 5
    }, 
    {
        'item_id': 2,
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount': 10
    }
    ]

#  OUTPUT
# [['Louboutin Flip Flops', 5], ['Eau de Fromage', 10]]

def test_returns_list_of_dictionaries_as_a_list():
    result = format_stock(stock_list)
    assert isinstance(result, list)

def test_returns_correct_values_from_argument():
    result = format_stock(stock_list)
    assert 'Louboutin Flip Flops' in result[0]
    assert 5 in result[0]
    assert 'Eau de Fromage' in result[1]
    assert 10 in result[1]

def test_returns_correct_values_in_correct_index():
    result = format_stock(stock_list)
    assert stock_list[0]['item_name'] in result[0]
    assert stock_list[0]['amount'] in result[0]
    assert stock_list[1]['item_name'] in result[1]
    assert stock_list[1]['amount'] in result[1]

def test_returns_values_in_nested_lists():
    result = format_stock(stock_list)
    assert len(result) == 2
    assert result[0] == ['Louboutin Flip Flops', 5]
    assert result[1] == ['Eau de Fromage', 10]

def test_returns_error_if_dictionary_is_missing_key():
    result = format_stock(stock_list_2)
    assert result == "the passed dictionary is missing key 'item_name'"


