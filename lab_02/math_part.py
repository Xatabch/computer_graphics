import numpy as np

def multiply_matrix(x, m, y, z, matrix1, matrix2):

    if m == y:
        result = []
        for i in range(x):
            result.append([])
            for j in range(y):
                result[i].append(0)
                for k in range(z):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result
    else:
        return -1

def transference(zero_params_array, dx, dy):
    '''Высчитывает новые значения параметров точек после смещения'''

    # "нормирую" ось координат
    dy *= -1

    # маска содержить индексы параметров фигуры, которые нужно преобразовывать
    mask = [0, 2, 4, 6, 8, 10, 12, 14, 15]

    # матрица преобразования
    M =[[1, 0, 0],[0, 1, 0], [dx, dy, 1]]

    result_params_array = []

    for i, item in enumerate(zero_params_array):
        if i in mask:
            if zero_params_array[i][2] == 1:
                matrix = [zero_params_array[i]]
                result = multiply_matrix(1, 3, 3, 3, matrix, M)
                result_params_array.append(result)
            else:
                result_params_array.append([])
                for j in range(len(zero_params_array[i])):
                    matrix = [zero_params_array[i][j]]
                    result = multiply_matrix(1, 3, 3, 3, matrix, M)
                    result_params_array[i].append(result[0])
        else:
            result_params_array.append(zero_params_array[i])

    return result_params_array


def scaling(zero_params_array, xm, ym, kx, ky):

    # матрица преобразований
    M = [[kx, 0, 0],[0, ky, 0],[0, 0, 1]]

    result_params_array = []

    for i in range(len(zero_params_array)):
        if zero_params_array[i][2] == 1:
            matrix = [zero_params_array[i]]
            result = multiply_matrix(1,3,3,3,matrix,M)
            result_params_array.append(result)
        else:
            result_params_array.append([])
            for j in range(len(zero_params_array[i])):
                matrix = [zero_params_array[i][j]]
                result = multiply_matrix(1,3,3,3,matrix,M)
                result_params_array[i].append(result[0])

    return result_params_array

