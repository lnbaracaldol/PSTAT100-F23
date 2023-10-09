OK_FORMAT = True

test = {   'name': 'q8',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> common_girl_names_2010.shape[1] == 5\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> common_girl_names_2010.shape[0] < 3\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> #checking that there is only one state, sex, and year\n'
                                               ">>> len(common_girl_names_2010['State'].unique()) == len(common_girl_names_2010['Sex'].unique()) == len(common_girl_names_2010['Year'].unique()) == "
                                               '1 \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
