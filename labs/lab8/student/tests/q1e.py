test = {   'hidden': False,
    'name': 'q1e',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> np.all(Y_hat1 == '
                                               'model1.predict(X))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(loss1, '
                                               'avg_squared_loss(Y, Y_hat1))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(loss1, '
                                               '2328790.795189534)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
