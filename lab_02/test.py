param_array = [[-145.0, 0.0, 1.0], [35.0, 35.0, 1.0], [0.0, 85.0, 1.0],
               [35.0, 35.0, 1.0], [145.0, 0.0, 1.0],
               [35.0, 35.0, 1.0], [0.0, -85.0, 1.0], [35.0, 35.0, 1.0],
               [0.0, 0.0, 1.0],
               [20.0, 20.0, 1.0], [0.0, 0.0, 1.0],
               [180.0, 120.0, 1.0], [0.0, 0.0, 1.0], [110.0, 50.0, 1.0],
               [[0.0, 0.0, 1.0],[-180.0, 180.0, 1.0],[-70.0, 180.0, 1.0]],
               [[0.0, 0.0, 1.0], [180.0, 180.0, 1.0], [70.0, 180.0, 1.0]], 0.0]

f = open("array","w")
mask = [14, 15, 16]
for i in range(len(param_array)):
    if i not in mask:
        for j in range(len(param_array[i])):
            f.write(str(param_array[i][j]))
            if j != len(param_array[i])-1:
                f.write(' ')
        f.write('\n')
    elif i in mask and i != 16:
        for z in range(len(param_array[i])):
            for k in range(len(param_array[i][z])):
                f.write(str(param_array[i][z][k]))
                if k != len(param_array[i][z])-1:
                    f.write(' ')
            if z != len(param_array[i]) - 1:
                f.write(',')
        f.write('\n')
f.write(str(param_array[16]))