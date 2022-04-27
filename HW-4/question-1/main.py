import numpy as np


def main():
    size = int(input())
    rows = []
    for i in range(size):
        row = [int(item) for item in input().split()]
        rows.append(row)
    matrix = np.array(rows, dtype="float64")
    matrix = np.concatenate((matrix, np.identity(size)), axis=1)
    make_row_reduce_echelon_form(matrix, size - 1)
    result = matrix[:, size :]
    result = np.round(result[0:size + 1, :])
    result = result.astype("int32")
    for row in result[:]:
        for element in row:
            print(element, end=" ")
        print()


def make_row_reduce_echelon_form(matrix, size):
    row_num = size
    column_num = size
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
            column_up_pivot = matrix[0:pivot_row, pivot_column]
            reducer_up_pivot_matrix = np.outer(column_up_pivot, pivot_row_divided)
            reducer_below_pivot_matrix = np.outer(column_below_pivot, pivot_row_divided)
            matrix[0:pivot_row] -= reducer_up_pivot_matrix
            matrix[pivot_row + 1:] -= reducer_below_pivot_matrix
            matrix[pivot_row] /= matrix[pivot_row][pivot_column]
            pivot_row += 1
            pivot_column += 1


if __name__ == '__main__':
    main()
