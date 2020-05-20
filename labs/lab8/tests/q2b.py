test = {   'hidden': False,
    'name': 'q2b',
    'points': 6,
    'suites': [   {   'cases': [   {   'code': '>>> np.all(np.isclose(Y_hat2, '
                                               'model2.predict(X_with_cut)))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(loss2, '
                                               'avg_squared_loss(Y, Y_hat2))\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.isclose(loss2, '
                                               '2274781.8081068466)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
