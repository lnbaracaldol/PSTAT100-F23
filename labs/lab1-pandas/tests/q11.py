OK_FORMAT = True

test = {   'name': 'q11',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> pivot_names.shape == (2,11)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (pivot_names.columns == list(range(2005,2016))).all() #syntax for range takes in values for start and end+1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> (pivot_names.index == baby_names['Sex'].unique()).all()\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
