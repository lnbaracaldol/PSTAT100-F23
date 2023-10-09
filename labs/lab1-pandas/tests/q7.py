OK_FORMAT = True

test = {   'name': 'q7',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': ">>> #if there are multiple years in which your friend's name was used, then choose the 2nd index of the 2D array\n"
                                               ">>> # else if there's only one year in which your friend's name was used, then choose the 1st index of the 1D array\n"
                                               '>>> (friend_slice.shape[1] == 3) if (len(friend_slice.shape) == 2) else (friend_slice.shape[0] == 3)   \n'
                                               '...     \n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> friend_slice.columns[0] == 'Count'\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> #check that friend_name appears as the index of the data frame\n>>> friend_name == (friend_slice.index).unique().all()\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> #checks if the index utilized has only one value\n'
                                               '>>> # (which should be the name of your friend)\n'
                                               '>>> \n'
                                               '>>> (friend_slice.index).unique().shape == (1,)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
