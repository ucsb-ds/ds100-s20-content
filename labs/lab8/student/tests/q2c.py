test = {   'hidden': False,
    'name': 'q2c',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> np.all(np.isclose(Y_hat3, '
                                               'model3.predict(X_with_cut_color_clarity)))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.all(np.isclose(loss3, '
                                               'avg_squared_loss(Y, Y_hat3)))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(loss3, '
                                               '1336023.526915778)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
