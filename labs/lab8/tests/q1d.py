test = {   'hidden': False,
    'name': 'q1d',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> len(theta) == 4\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(Y_hat[1], '
                                               'linear_model(theta, X)[1])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(loss, '
                                               'avg_squared_loss(Y, Y_hat))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
