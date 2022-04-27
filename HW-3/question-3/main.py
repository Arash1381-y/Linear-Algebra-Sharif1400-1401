import cmath
import math

import numpy as np


class Rotator:
    def __init__(self, vector):
        self.vector = np.array(vector).transpose()

    def rotate_about_x(self, radian):
        cos_angle = math.cos(radian)
        sin_angle = math.sin(radian)
        rotation_matrix = np.array([[1, 0, 0],
                                    [0, cos_angle, -sin_angle],
                                    [0, sin_angle, cos_angle]], dtype="float64")
        self.vector = np.dot(rotation_matrix, self.vector)

    def rotate_about_y(self, radian):
        cos_angle = math.cos(radian)
        sin_angle = math.sin(radian)
        rotation_matrix = np.array([[cos_angle, 0, sin_angle],
                                    [0, 1, 0],
                                    [-sin_angle, 0, cos_angle]], dtype="float64")
        self.vector = np.dot(rotation_matrix, self.vector)

    def rotate_about_z(self, radian):
        cos_angle = math.cos(radian)
        sin_angle = math.sin(radian)
        rotation_matrix = np.array([[cos_angle, -sin_angle, 0],
                                    [sin_angle, cos_angle, 0],
                                    [0, 0, 1]], dtype="float64")
        self.vector = np.dot(rotation_matrix, self.vector)


def main():
    np.set_printoptions(formatter={'float': lambda x: "{0:0.1f}".format(x)}, threshold=np.inf)
    nodes_num = int(input())
    list_2d = []
    for i in range(nodes_num):
        vector = [int(item) for item in input().split()]
        list_2d.append(vector)

    x_radian, y_radian, z_radian = map(float, input().split())
    matrix = []
    for i in range(nodes_num):
        rotator = Rotator(list_2d[i])
        rotator.rotate_about_x(x_radian)
        rotator.rotate_about_y(y_radian)
        rotator.rotate_about_z(z_radian)
        matrix.append(rotator.vector)

    print(np.array(matrix))


if __name__ == '__main__':
    main()
