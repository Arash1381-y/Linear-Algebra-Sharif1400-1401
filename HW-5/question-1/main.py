import numpy as np

ACCURACY = 1000


def eig_values(A: np.matrix, iter: int) -> np.array:
    matrix = A
    for i in range(iter):
        q, r = np.linalg.qr(matrix)
        matrix = np.matrix(r * q)
    return np.array(matrix.diagonal())


def main():
    np.set_printoptions(precision=2)
    matrix_as_string = input()
    rows_as_string = matrix_as_string.split(";")
    rows_list = []
    for row in rows_as_string:
        rows_list.append(list(map(int, row.split(","))))

    matrix = np.matrix(rows_list)
    eig_array = eig_values(matrix, ACCURACY)
    eig_array_sort = sorted(eig_array[0], reverse=True)
    for eig in eig_array_sort:
        print(f'{eig:.2f}', end=" ")


if __name__ == '__main__':
    main()
