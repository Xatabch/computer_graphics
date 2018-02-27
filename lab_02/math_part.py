import numpy as np

def transference(zero_points_params_array, dx, dy):
    '''Высчитывает новые значения параметров точек после смещения'''

    M = np.matrix(np.array([[1, 0, 0],[0, 1, 0], [dx, dy, 1]]))

    new_points_params_array = []

    for i in range(len(zero_points_params_array)):
        if len(zero_points_params_array[i]) == 2:
            new_points_params_array.append(zero_points_params_array[i])
            new_points_params_array[i].append(1)
        else:
            new_points_params_array.append([])
            for j in range(len(zero_points_params_array[i])):
                tmp = zero_points_params_array[i][j]
                tmp.append(1)
                new_points_params_array[i].append(tmp)

    result_points_params_array = []

    for i in range(len(new_points_params_array)):
        if len(new_points_params_array[i]) == 3:
            matrix = np.matrix(np.array(new_points_params_array[i]))
            result = np.dot(matrix, M)
            result_points_params_array.append(list(np.array(result)))
        else:
            result_points_params_array.append([])
            for j in range(len(new_points_params_array[i])):
                matrix = np.matrix(np.array(new_points_params_array[i][j]))
                result = np.dot(matrix, M)
                result_points_params_array[i].appned(result)

    return result_points_params_array
