"""https://zhuanlan.zhihu.com/p/146190385"""

import numpy as np


def intersection_of_multi_lines(strt_points, directions):
    '''
    strt_points: line start points; numpy array, nxdim
    directions: list dierctions; numpy array, nxdim

    return: the nearest points to n lines
    '''

    n, dim = strt_points.shape

    G_left = np.tile(np.eye(dim), (n, 1))
    G_right = np.zeros((dim * n, n))

    for i in range(n):
        G_right[i * dim:(i + 1) * dim, i] = -directions[i, :]

    G = np.concatenate([G_left, G_right], axis=1)
    d = strt_points.reshape((-1, 1))

    m = np.linalg.inv(np.dot(G.T, G)).dot(G.T).dot(d)

    # return m[0:dim]
    return m


if __name__ == '__main__':
    ##########################################################################################
    ##test case
    strt_point = np.zeros((2, 3))
    strt_point[0, :] = np.array([0, 0, -10])
    strt_point[1, :] = np.array([-10, 0, 0])

    directions = np.zeros((2, 3))
    directions[0, :] = np.array([1, 0, 0])
    directions[1, :] = np.array([0, 1, 0])

    inters = intersection_of_multi_lines(strt_point, directions)
    print('[DEBUG] intersection {}'.format(inters))
