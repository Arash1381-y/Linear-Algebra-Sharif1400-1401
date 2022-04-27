import numpy as np


def main():
    array_one = [int(item) for item in input().split()]
    base_list = array_one.copy()
    array_two = [int(item) for item in input().split()]
    np.array(array_one)
    array_two = np.array(array_two)

    column_num = array_two.shape[0]
    base_list.extend([0 for _ in range(column_num - 1)])
    list_2d = []
    for i in range(column_num):
        list_2d.append(base_list.copy())
        base_list.insert(0, 0)
        base_list.pop()

    np.set_printoptions(threshold=np.inf)
    matrix = np.array(list_2d).transpose()
    convolved = np.dot(matrix, array_two.transpose())
    print(convolved)


if __name__ == '__main__':
    main()
