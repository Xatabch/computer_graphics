import math as mt
import numpy as np


def size_length(point1, point2, point3):
    '''Возвращает длины трех сторон(a,b,c), проходящих через
       заданные вершины'''

    a = mt.sqrt((point2[1] - point1[1])**2 + (point2[0] - point1[0])**2)
    b = mt.sqrt((point3[1] - point2[1])**2 + (point3[0] - point2[0])**2)
    c = mt.sqrt((point1[1] - point3[1])**2 + (point1[0] - point3[0])**2)

    return a, b, c


def triangle_square(a, b, c):
    '''Возращает площадь треугольника'''
    
    p = (a + b + c)/2 #полупериметр треугольника
    
    return ((p*(p - a)*(p - b)*(p - c))**(1/2))


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

    a,b,c = size_length(points_array[0],points_array[1],
                        points_array[2])


    xa = points_array[0][0]
    ya = points_array[0][1]
    xb = points_array[1][0]
    yb = points_array[1][1]
    xc = points_array[2][0]
    yc = points_array[2][1]

    v_ab = [xb-xa,yb-ya]
    v_ac = [xc-xa,yc-ya]

    v_a = [v_ab[0]/a,v_ab[1]/a]
    v_b = [v_ac[0]/c,v_ac[1]/c]

    v_ak = [v_a[0]+v_b[0],v_a[1]+v_b[1]]

    v_bc = [xc-xb,yc-yb]
    v_ba = [xa-xb,ya-yb]

    v_a = [v_bc[0]/b,v_bc[1]/b]
    v_b = [v_ba[0]/a,v_ba[1]/a]

    v_bk = [v_a[0]+v_b[0],v_a[1]+v_b[1]]

    M1 = np.array([[v_ak[1], -v_ak[0]],
                   [v_bk[1], -v_bk[0]]])

    v1 = np.array([[v_ak[1]*xa-v_ak[0]*ya],[v_bk[1]*xb-v_bk[0]*yb]])

    res = np.linalg.solve(M1,v1)

    return res

    
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


    return points_of_minimum
                        
