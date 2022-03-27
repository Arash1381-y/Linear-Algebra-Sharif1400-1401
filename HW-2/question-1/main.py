from collections import defaultdict

import numpy as np


def find_k_nearest(base_matrix, voted):
    vector = [float(v) for v in input().split()]
    tiled_matrix = np.tile(vector, (voted, 1))
    transfer_vector = (base_matrix - tiled_matrix)
    vector_two_power = transfer_vector * transfer_vector
    dist_vector = np.sum(vector_two_power, axis=1)
    index_sorted = np.argsort(dist_vector)
    voted_candidate = defaultdict(lambda: 0)
    return index_sorted, voted_candidate


def find_max_key(voted_candidate):
    selected_key = -1
    max_vote = -1
    print(voted_candidate)
    for k, v in voted_candidate.items():
        if v > max_vote:
            max_vote = v
            selected_key = k
        elif v == max_vote and k < selected_key:
            selected_key = k
    return selected_key


def find_candidate(base_matrix, k_near, not_voted, voted, voted_candidate_by_neighbors):
    for i in range(not_voted):
        index_sorted, voted_candidate = find_k_nearest(base_matrix, voted)

        for j in range(k_near):
            index = voted_candidate_by_neighbors[index_sorted]
            voted_candidate[index] += 1

        selected_key = find_max_key(voted_candidate)
        print(selected_key, end=" ")


def main():
    k_near, voted, not_voted = map(int, input().split())

    voted_neighbors = []
    for i in range(voted):
        vector = [float(v) for v in input().split()]
        voted_neighbors.append(vector)

    voted_candidate_by_neighbors = [int(v) for v in input().split()]

    base_matrix = np.array(voted_neighbors)
    find_candidate(base_matrix, k_near, not_voted, voted, voted_candidate_by_neighbors)


if __name__ == '__main__':
    main()
