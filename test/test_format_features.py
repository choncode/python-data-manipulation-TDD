from src.format_features import format_features

items_list = [
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear', 'amount': 5
    }, 
    {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount': 10
    }
    ]

items_list_2 = [
    {
        'item_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear', 'amount': 5
    }, 
    {
        'item_id': 2,
        'item_name': 'Eau de Fromage',
        'department': 'Beauty',
        'amount': 10
    }
    ]


def test_returns_a_list_of_dictionaries_as_a_list():
    result = format_features(items_list)
    assert isinstance(result, list)

def test_returns_correct_values_from_argument():
    result = format_features(items_list)
    assert ['Designer'] in result
    assert ['Faux-Faux-Leather'] in result
    assert ['Fragrance'] in result

def test_returns_unique_values_from_argument():
    result = format_features(items_list)
    flat_result = [string for list in result for string in list]
    assert len(set(flat_result)) == len(result)

def test_returns_error_if_missing_key():
    result = format_features(items_list_2)
    assert result == "a passed dictionary is missing a key of 'features'"





