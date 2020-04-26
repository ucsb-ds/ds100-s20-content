test = {   'hidden': False,
    'name': 'q1a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> isinstance(bike, '
                                               'pd.DataFrame)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bike['holiday'].dtype == "
                                               "np.dtype('O')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bike['weekday'].dtype == "
                                               "np.dtype('O')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "list(bike['weekday'].iloc[300:303]) "
                                               "== ['Thu', 'Fri', 'Fri']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "list(bike['workingday'].iloc[370:375]) "
                                               "== ['no', 'no', 'no', 'no', "
                                               "'no']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> bike['weathersit'].dtype "
                                               "== np.dtype('O')\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
