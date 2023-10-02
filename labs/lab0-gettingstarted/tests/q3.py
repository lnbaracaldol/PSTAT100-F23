OK_FORMAT = True

test = {   'name': 'q3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> type(valid_values) == np.ndarray\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(valid_values) <= len(random_arr)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # testing that every element in valid_values is in random_arr\n>>> all(x in random_arr for x in valid_values)\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
