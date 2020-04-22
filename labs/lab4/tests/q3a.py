test = {   'hidden': False,
    'name': 'q3a',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> all(df_clean.columns) == '
                                               'all(df_new.columns)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'df_clean.loc[4].main_category\n'
                                               "'technology'",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               'df_clean.loc[4].main_category '
                                               '== '
                                               'df_clean.loc[192544].main_category\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
