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


def radius_inscribed_circle(points_array):
    '''Находит радиус вписанной окружности'''

    a,b,c = size_length(points_array[0],points_array[1],points_array[2])
    t_square = triangle_square(a,b,c)

    return ((2 * t_square)/(a + b + c))


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
                        
