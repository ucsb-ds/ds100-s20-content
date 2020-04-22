test = {   'hidden': False,
    'name': 'q5a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> all(df_new.loc[0]) == '
                                               'all(pd.Series({"currency":"USD", '
                                               '"main_category":"games", '
                                               '"sub_category":"Tabletop '
                                               'Games", "duration": 16.0, '
                                               '"goal_usd":2000.0, "country": '
                                               '"US", "blurb_length":14, '
                                               '"name_length":7, '
                                               '"status":"successful"}))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'df_success.loc[4].main_category '
                                               '== '
                                               'df_success.loc[14].main_category\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> "failed" not in '
                                               'df_success["status"]\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
