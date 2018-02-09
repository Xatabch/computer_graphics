import math as mt

def size_length(point1,point2,point3):
    '''Возвращает длины трех сторон(a,b,c), проходящих через
       заданные вершины'''

    a = mt.sqrt((point2[1] - point1[1])**2 + (point2[0] - point1[0])**2)
    b = mt.sqrt((point3[1] - point2[1])**2 + (point3[0] - point2[0])**2)
    c = mt.sqrt((point1[1] - point3[1])**2 + (point1[0] - point3[0])**2)

    return a, b, c


def triangle_square(a,b,c):
    '''Возращает площадь треугольника'''
    
    p = (a + b + c)/2 #полупериметр треугольника
    
    return (mt.sqrt(p*(p - a)*(p - b)*(p - c)))


def radius_circumscribed_circle(points_array):
    '''Находит радиус описанной окружности'''

    a,b,c = size_length(points_array[0],points_array[1],points_array[2])
    t_square = triangle_square(a,b,c)

    return ((a*b*c)/(4 * t_square))

def center_circumscribed_circle(points_array):
    '''Находит центр описанной окружности'''

    x1 = points_array[0][0]
    y1 = points_array[0][1]
    x2 = points_array[1][0]
    y2 = points_array[1][1]
    x3 = points_array[2][0]
    y3 = points_array[2][1]

    x12 = x1-x2
    x23 = x2-x3
    x31 = x3-x1
    y12 = y1-y2
    y23 = y2-y3
    y31 = y3-y1

    z1 = x1**2 + y1**2
    z2 = x2**2 + y2**2
    z3 = x3**2 + y3**2

    a = -(y12*z3+y23*z1+y31*z2)/(2*(x12*y31-y12*x31))
    b = (x12*z3+x23*z1+x31*z2)/(2*(x12*y31-y12*x31))

    return a,b

def radius_inscribed_circle(points_array):
    '''Находит радиус вписанной окружности'''

    a,b,c = size_length(points_array[0],points_array[1],points_array[2])
    t_square = triangle_square(a,b,c)

    return ((2 * t_square)/(a + b + c))

def center_inscribed_circle(points_array):
    '''Находит центр вписанной окружности a(x1-x2,y1-y2)
       b(x2-x3,y2-y3),c(x3-x1,y3-y1)'''

    x1 = points_array[0][0]
    y1 = points_array[0][1]
    x2 = points_array[1][0]
    y2 = points_array[1][1]
    x3 = points_array[2][0]
    y3 = points_array[2][1]
    print('x1,x2',x1,x2)

    middle_a_x = (x1 + x2)/2
    middle_a_y = (y1 + y2)/2
    middle_b_x = (x2 + x3)/2
    middle_b_y = (y2 + y3)/2
    middle_c_x = (x3 + x1)/2
    middle_c_y = (y3 + y1)/2
    print('middles a,b: (',middle_a_x,',',middle_a_y,'),(',middle_b_x,',',middle_b_y,')')

    angle_a = (y2-y1)/(x2-x1)
    angle_b = (y3-y2)/(x3-x2)
    angle_c = (y1-y3)/(x1-x3)
    print('angles: ',angle_a,angle_b,angle_c)

    if (abs(angle_a) != 0 and abs(angle_b) != 0):
        max = middle_a_x
        may = middle_a_y
        mbx = middle_b_x
        mby = middle_b_y
        ba = -1/angle_a
        bb = -1/angle_b
    elif (abs(angle_a) != 0 and abs(angle_c) != 0):
        max = middle_a_x
        may = middle_a_y
        mbx = middle_c_x
        mby = middle_c_y
        ba = -1/angle_a
        bb = -1/angle_b
    elif (abs(angle_b) != 0 and abs(angle_c) != 0):
        max = middle_b_x
        may = middle_b_y
        mbx = middle_c_x
        mby = middle_c_y
        ba = -1/angle_b
        bb = -1/angle_c
        
    #bissec_a = -1/angle_a
    #bissec_b = -1/angle_b
    #bissec_c = -1/angle_c
    #print('bissectrises: ',bissec_a,bissec_b,bissec_c)

    a = (ba*max-may+mby-bb*mbx)/(ba-bb)
    b = ba*(a - max) + may

    return a,b


def square_circumscribed_circle(point1,point2,point3):
    '''Возвращает площадь описанной окружности'''

    points_array = []
    points_array.append(point1)
    points_array.append(point2)
    points_array.append(point3)
    
    radius = radius_circumscribed_circle(points_array)

    return (mt.pi * radius**2)


def square_inscribed_circle(point1,point2,point3):
    '''Возвращает радиус вписанной окружности'''

    points_array = []
    points_array.append(point1)
    points_array.append(point2)
    points_array.append(point3)
    
    radius = radius_inscribed_circle(points_array)

    return (mt.pi * radius**2)


def check_degeneracy(point1,point2,point3):
    '''Проверяет треугольник на вырожденность'''
    
    points_array = []
    points_array.append(point1)
    points_array.append(point2)
    points_array.append(point3)

    a,b,c = size_length(points_array[0],points_array[1],points_array[2])
    t_square = triangle_square(a,b,c)

    if t_square != 0:
        return 0
    else:
        return 1

def find_min_square(points_array):
    '''Возвращает три точки треугольника для которого
       разность площадей вписанной и описанной окружностей минимальна'''

    points_of_minimum = [0,0,0]
    min_square = 1000000
    check = 0
    for i in range(len(points_array)):
        for j in range(len(points_array)):
            for k in range(len(points_array)):
                if (i != j) and (i != k) and (j != k):
                    check = check_degeneracy(points_array[i],points_array[j],points_array[k])
                    if(check == 0):
                        circumscribed_circle = square_circumscribed_circle(points_array[i],points_array[j],points_array[k])
                        inscribed_circle = square_inscribed_circle(points_array[i],points_array[j],points_array[k])

                        if(abs(circumscribed_circle - inscribed_circle) < min_square):
                            min_square = abs(circumscribed_circle - inscribed_circle)
                            points_of_minimum[0] = points_array[i]
                            points_of_minimum[1] = points_array[j]
                            points_of_minimum[2] = points_array[k]
                    else:
                        print('Вырожден',points_array[i],points_array[j],points_array[k])


    return points_of_minimum
                        
