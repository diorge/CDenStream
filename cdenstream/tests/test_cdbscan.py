import numpy as np
from ..cdbscan import cdbscan


def test_easy_clusters_no_constraints():
    points = np.array([[1, 1],
                       [52, 3],
                       [1, 2],
                       [2, 3],
                       [50, 4],
                       [51, 2]])
    epsilon = 5
    minpts = 2
    clusters = cdbscan(points, epsilon=epsilon, minpts=minpts)
    assert sorted(sorted(clusters)[0]) == [0, 2, 3]
    assert sorted(sorted(clusters)[1]) == [1, 4, 5]
