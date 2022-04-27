import numpy
import numpy as np


def main():
    dim, set_size, dots_num = map(int, input().split())
    vector_list = []
    for i in range(set_size):
        vector_list.append([float(item) for item in input().split()])

    dots_list = []
    for i in range(dots_num):
        dots_list.append([float(item) for item in input().split()])

    base_vector = vector_list[0]
    for dot in dots_list:
        reduced_vector_list = []
        for vector in vector_list[1:]:
            reduced_vector_list.append(np.subtract(vector, base_vector))

        reduced_vector_list.append(np.subtract(dot, base_vector))
        matrix = np.array(reduced_vector_list).transpose()
        make_echelon_form(matrix)
        find_equations_solution(matrix)

    return 0


def make_echelon_form(matrix):
    row_num = matrix.shape[0] - 1
    column_num = matrix.shape[1] - 1
    pivot_row = 0
    pivot_column = 0
    while pivot_row <= row_num and pivot_column <= column_num:
        column = [abs(element) for element in matrix[pivot_row:, pivot_column]]
        i_non_zero = numpy.argmax(column) + pivot_row
        if matrix[i_non_zero, pivot_column] == 0:
            pivot_column += 1
        else:
            matrix[[pivot_row, i_non_zero]] = matrix[[i_non_zero, pivot_row]]
            pivot_row_divided = matrix[pivot_row] / matrix[pivot_row][pivot_column]
            column_below_pivot = matrix[pivot_row + 1:, pivot_column]
            reducer_matrix = np.outer(column_below_pivot, pivot_row_divided)
            matrix[pivot_row + 1:] -= reducer_matrix
            pivot_row += 1
            pivot_column += 1


def find_equations_solution(matrix):
    column_num = matrix.shape[1] - 1
    for row in matrix[:]:
        if truncate(row[column_num], 8) != 0:

            is_ok = False
            for i in range(column_num):
                if row[column_num - 1 - i] != 0:
                    is_ok = True
                    break

            if not is_ok:
                print("NO")
                return

    print("YES")


def truncate(num, n):
    integer = int(num * (10 ** n)) / (10 ** n)
    return float(integer)


if __name__ == '__main__':
    main()
