import numpy as np
data = np.array([[1, 0, -1], [1, 1, -1], [1, 1, 1], [1, 0, 1],
                     [1, 0, -1], [2, 0, -1], [2, 1, -1], [2, 1, 1],
                     [2, 2, 1], [2, 2, 1], [3, 2, 1], [3, 1, 1],
                     [3, 1, 1], [3, 2, 1], [3, 2, -1]])

data = np.array([[1, 'S', -1], [1, 'M', -1], [1, 'M', 1], [1, 'S', 1],
                     [1, 'S', -1], [2, 'S', -1], [2, 'M', -1], [2, 'M', 1],
                     [2, 'L', 1], [2, 'L', 1], [3, 'L', 1], [3, 'M', 1],
                     [3, 'M', 1], [3, 'L', 1], [3, 'L', -1]])

data = np.array([[1, 'S', -1], [1, 'Mabc', -1], [1, 'Mabc', 1], [1, 'S', 1],
                     [1, 'S', -1], [2, 'S', -1], [2, 'Mabc', -1], [2, 'Mabc', 1],
                     [2, 'Lab', 1], [2, 'Lab', 1], [3, 'Lab', 1], [3, 'Mabc', 1],
                     [3, 'Mabc', 1], [3, 'Lab', 1], [3, 'Lab', -1]])

data = np.array([[1, 'S', 'F'], [1, 'M', 'F'], [1, 'M', 'T'], [1, 'S', 'T'],
                     [1, 'S', 'F'], [2, 'S', 'F'], [2, 'M', 'F'], [2, 'M', 'T'],
                     [2, 'L', 'T'], [2, 'L', 'T'], [3, 'L', 'T'], [3, 'M', 'T'],
                     [3, 'M', 'T'], [3, 'L', 'T'], [3, 'L', 'F']])

data = np.array([[1, 'S', '猫'], [1, 'M', '猫'], [1, 'M', '狗'], [1, 'S', '狗'],
                     [1, 'S', '猫'], [2, 'S', '猫'], [2, 'M', '猫'], [2, 'M', '狗'],
                     [2, 'L', '狗'], [2, 'L', '狗'], [3, 'L', '狗'], [3, 'M', '狗'],
                     [3, 'M', '狗'], [3, 'L', '狗'], [3, 'L', '猫']])