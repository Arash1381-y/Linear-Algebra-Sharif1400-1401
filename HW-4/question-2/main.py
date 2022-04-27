import numpy as np


def is_linear_combination_of_base(base, dot):
    base.append(dot)
    matrix = np.array(base, dtype='float64').transpose()
    make_echelon_form(matrix)
    return any_solution(matrix)


def make_echelon_form(matrix):
    row_num = matrix.shape[0] - 1
    column_num = matrix.shape[1] - 1
    pivot_row = 0
    pivot_column = 0
    while pivot_row <= row_num and pivot_column <= column_num:
        column = [abs(element) for element in matrix[pivot_row:, pivot_column]]
        i_non_zero = np.argmax(column) + pivot_row
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


def any_solution(matrix):
    column_num = matrix.shape[1] - 1
    for row in matrix[:]:
        if truncate(row[column_num], 8) != 0:

            is_ok = False
            for i in range(column_num):
                if row[column_num - 1 - i] != 0:
                    is_ok = True
                    break

            if not is_ok:
                return False

    return True


def truncate(num, n):
    integer = int(num * (10 ** n)) / (10 ** n)
    return float(integer)


def main():
    dim, count_dots = map(int, input().split())
    dots_lists = []
    for i in range(count_dots):
        dot = [int(entry) for entry in input().split()]
        dots_lists.append(dot)

    base_vector_list = []
    dim = 0
    for dot in dots_lists:
        result = is_linear_combination_of_base(base_vector_list, dot)
        if not result:
            dim += 1
        else:
            base_vector_list.pop()

    print(len(base_vector_list))


if __name__ == '__main__':
    main()
