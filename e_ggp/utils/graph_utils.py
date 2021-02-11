# Copyright 2021 (c) anonymous-4989 - All Rights Reserved
#

import numpy as np


def adj_list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = np.zeros((n, n), dtype=np.float)
    for i in range(n):
        for j in adj_list[i]:
            adj_matrix[i, j] = 1
    return adj_matrix
