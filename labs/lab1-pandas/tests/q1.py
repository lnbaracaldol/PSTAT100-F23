OK_FORMAT = True

test = {   'name': 'q1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> type(fruit_info['rank1']) == pd.core.series.Series\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> fruit_info.shape == (4,3)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> (fruit_info.loc[0, 'rank1'] == 1) or (fruit_info.loc[0, 'rank1'] == 2) or (fruit_info.loc[0, 'rank1'] == 3) or (fruit_info.loc[0, 'rank1'] == 4)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> max(fruit_info['rank1']) - min(fruit_info['rank1']) == 3\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
