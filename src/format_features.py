"""The format_features function should accept a list of 
dictionaries in the following format and return a list of 
lists containing the feature_name.

The file is run by calling this module with the python keyword.

Example:
    python src/format_features.py

To run the test file, please use the below:
    pytest test/test_format_features.py
"""

def format_features(list):
    """Takes a list of dictionaries and returns a list of lists 
    with the unique values of features.

    Args:
        list: A list of dictionaries.

    Returns:
        A list of lists.
    """
    
    features_list = []

    try:
        for dict in list:
            for features in dict['features']:
                features_list.append(features)

        features_list = set(features_list)
        unique_features_list = [[feature] for feature in features_list]
        return unique_features_list
    except Exception as error:
        return f'a passed dictionary is missing a key of {error}'



    