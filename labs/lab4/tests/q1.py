test = {   'hidden': False,
    'name': 'q1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> list(df_new.columns) == '
                                               "['currency', 'main_category', "
                                               "'sub_category', 'duration', "
                                               "'goal_usd', 'country', "
                                               "'blurb_length', 'name_length', "
                                               "'status']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> all(df_new.loc[0]) == '
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
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
