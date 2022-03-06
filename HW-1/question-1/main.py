import numpy as np


def init(n):
    return np.ones(n, dtype=np.int64)


def dot(a_vector, b_vector, is_vertical):
    if not is_vertical and len(b_vector) == len(a_vector):
        return np.dot(a_vector, np.array(b_vector))
    return None


def out(a_vector, b_vector, is_vertical, selector):
    if is_vertical and len(a_vector) >= selector > 0:
        result = np.multiply(b_vector, a_vector[selector - 1])
        return result, False, len(b_vector)
    else:
        return a_vector, is_vertical, len(a_vector)


def cross(a_vector, b_vector):
    if len(a_vector) == 3 and len(b_vector) == 3:
        result = np.cross(a_vector, np.array(b_vector))
        return result / np.sqrt(result.dot(result))
    return None


def hadamard(a_vector, b_vector):
    if len(a_vector) == len(b_vector):
        return np.multiply(a_vector, b_vector)
    else:
        return a_vector


def print_vector(a_vector, is_vertical):
    if is_vertical:
        for i in a_vector:
            print(int(i), end="\n")
    else:
        for i in a_vector:
            print(int(i), end=" ")
        print()


def main():
    n = int(input())  # number of vector entries
    q = int(input())  # number of queries
    a = init(n)
    is_vertical = True

    for num in range(q):
        query = str(input())
        if query.startswith("T"):
            is_vertical = not is_vertical

        elif query.startswith("dot"):
            b = np.array([int(s) for s in query[4:].split()])
            result = dot(a, b, is_vertical)
            if result is not None:
                print(int(result))

        elif query.startswith("out"):
            comma_index = query.find(',')
            b = np.array([int(s) for s in query[4:comma_index - 1].split()])
            selector = int(query[comma_index + 2:])
            a, is_vertical, n = out(a, b, is_vertical, selector)

        elif query.startswith("cross"):
            b = [int(s) for s in query[6:].split()]
            result = cross(a, b)
            if result is not None:
                for i in result[:]:
                    format_float = "{:.4f}".format(i)
                    print(format_float, end=" ")
                print()

        elif query.startswith("had"):
            b = [int(s) for s in query[4:].split()]
            a = hadamard(a, b)

        elif query.startswith("print"):
            print_vector(a, is_vertical)

        else:
            a = init(int(query[6:]))


if __name__ == '__main__':
    main()
