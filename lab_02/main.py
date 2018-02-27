from tkinter import *
from sympy import *
from math import *
from math_part import *

def draw_circle(center, radius, color):
    '''Рисует окружность'''

    points_array = []
    start = center[0] - radius
    end = center[0] + radius
    y = Symbol('y')
    for i in range(start, end+1, 1):
        root = solve((i-center[0])**2 + (y-center[1])**2 - radius**2, y)
        #print(root)
        if len(root) == 2:
            points_array.append([580 + float(i), 310 - float(root[0])])
            points_array.append([580 + float(i), 310 - float(root[1])])
        else:
            points_array.append([580 + float(i), 310 - float(root[0])])

    canvas.create_polygon(points_array,fill=color, outline=color)


def draw_ellipse(center, a, b, color):
    '''Рисует эллипс'''

    points_array = []
    j = 0

    for i in range(0, 7168, 1):
        j+= 0.05
        x = a * cos(j)
        y = b * sin(j)
        points_array.append([580 + x + center[0], 310 - y + center[1]])

    #print(points_array)
    #canvas.create_polygon(points_array, fill=color, outline=color, smooth=1)

def draw_cross(center, a, b, color):
    '''Рисует перекрестие'''

    cross_points1 = [[580 + center[0] - a, 310 - center[1] + b],[580 + center[0] + a,310 - center[1] - b]]
    cross_points2 = [[580 + center[0] + a, 310 - center[1] + b], [580 + center[0] - a, 310 - center[1] - b]]
    canvas.create_line(cross_points1, fill=color, width=3)
    canvas.create_line(cross_points2, fill=color, width=3)

def draw_triangle(triangle_points, color):
    '''Рисует треугольник'''

    if len(triangle_points) == 3:
        canvas.create_polygon(triangle_points, fill=color)

def create_figure(center_circle1, radius_circle1, center_circle2, radius_circle2, center_circle3,
                  radius_circle3, center_circle4, radius_circle4,
                  center_circle5, radius_circle5,
                  center_outside_ellipse, a_outside_ellipse, b_outside_ellipse,
                  center_inside_ellipse, a_inside_ellipse, b_inside_ellipse,
                  triangle1_points, triangle2_points):
    '''Строит заданную фигуру'''

    # Наружный эллпис
    draw_ellipse(center_outside_ellipse, a_outside_ellipse, b_outside_ellipse, "red")
    # Внутренний эллипс
    draw_ellipse(center_inside_ellipse, a_inside_ellipse, b_inside_ellipse, "white")

    # Четыре окружности в эллипсе
    draw_circle(center_circle1, radius_circle1, "yellow")
    draw_circle(center_circle2, radius_circle2, "yellow")
    draw_circle(center_circle3, radius_circle3, "yellow")
    draw_circle(center_circle4, radius_circle4, "yellow")

    # Окружность посередине
    draw_circle(center_circle5, radius_circle5, "red")

    # Построение перекрестия у боковых окружностей
    draw_cross(center_circle1, radius_circle1-10, radius_circle1-10, "red")
    draw_cross(center_circle2, radius_circle2 - 10, radius_circle2 - 10, "red")
    draw_cross(center_circle3, radius_circle3 - 10, radius_circle3 - 10, "red")
    draw_cross(center_circle4, radius_circle4 - 10, radius_circle4 - 10, "red")

    # Построение перекрестия в центре
    draw_cross(center_inside_ellipse, a_inside_ellipse - 10, b_inside_ellipse - 10, "red")

    # Окружность посередине
    draw_circle(center_circle5, radius_circle5, "red")

    # Построение треугольников
    canvas.create_polygon([580 + 0, 310 - 0],
                          [580 + triangle1_points[1][0], 310 - triangle1_points[1][1]],
                          [580 + triangle1_points[2][0], 310 - triangle1_points[2][1]],
                          fill="black")

    canvas.create_polygon([580 + 0, 310 - 0],
                          [580 + triangle2_points[1][0], 310 - triangle2_points[1][1]],
                          [580 + triangle2_points[2][0], 310 - triangle2_points[2][1]],
                          fill="black")








root = Tk()
root.title('My app')
root.geometry('1320x640')

canvas = Canvas(root, width=1040, height=640, bg='white')
canvas.pack(side='right')

# смещение по x
x = 15
# смещение по y
y = 130

# Меню
btn_rep = Button(root, text='Переместить', width=25)
btn_rep.bind('<Button-1>')
btn_rep.place(x=x, y=y)

label_rep_dx = Label(root, text='dx:')
label_rep_dx.place(x=x, y=y+40)
entry_rep_dx = Entry(root, width=10)
entry_rep_dx.place(x=x+25, y=y+40)

label_rep_dy = Label(root, text='dy:')
label_rep_dy.place(x=x+115, y=y+40)
entry_rep_dy = Entry(root, width=10)
entry_rep_dy.place(x=x+140, y=y+40)


btn_sc = Button(root, text='Масштабировать', width=25)
btn_sc.bind('<Button-1>')
btn_sc.place(x=x, y=y+140)

label_sc_cent = Label(root, text='cent:')
label_sc_cent.place(x=x, y=y+180)
entry_sc_cent = Entry(root, width=5)
entry_sc_cent.place(x=x+35, y=y+180)

label_sc_dx = Label(root, text='dx:')
label_sc_dx.place(x=x+82, y=y+180)
entry_sc_dx = Entry(root, width=5)
entry_sc_dx.place(x=x+107, y=y+180)

label_sc_dy = Label(root, text='dy:')
label_sc_dy.place(x=x+155, y=y+180)
entry_sc_dy = Entry(root, width=5)
entry_sc_dy.place(x=x+180, y=y+180)


btn_sc = Button(root, text='Поворот', width=25)
btn_sc.bind('<Button-1>')
btn_sc.place(x=x, y=y+280)

label_sc_cent = Label(root, text='cent:')
label_sc_cent.place(x=x, y=y+320)
entry_sc_cent = Entry(root, width=5)
entry_sc_cent.place(x=x+35, y=y+320)

label_sc_dx = Label(root, text='dx:')
label_sc_dx.place(x=x+82, y=y+320)
entry_sc_dx = Entry(root, width=5)
entry_sc_dx.place(x=x+107, y=y+320)

label_sc_dy = Label(root, text='dy:')
label_sc_dy.place(x=x+155, y=y+320)
entry_sc_dy = Entry(root, width=5)
entry_sc_dy.place(x=x+180, y=y+320)

zero_points_params_array = [[-145, 0], [0, 85], [145, 0], [0, -85],
              [0, 0], [0, 0], [0, 0], [[0,0],[-180,-180],[-70, -180]],
              [[0, 0], [180, -180], [70, -180]]]

#create_figure([-145, 0], 35, [0, 85], 35, [145, 0], 35, [0, -85], 35,
#              [0, 0], 20, [0, 0], 180, 120, [0, 0], 110, 50, [[0,0],[-180,-180],[-70, -180]],
#              [[0, 0], [180, -180], [70, -180]])

transference_array = transference(zero_points_params_array, 40, 40)

#print(transference_array[1][0])

create_figure(transference_array[0][0], 35, transference_array[1][0], 35, transference_array[2][0], 35,
              transference_array[3][0], 35,
              transference_array[4][0], 20, transference_array[5][0],
              180, 120, transference_array[6][0], 110, 50, transference_array[7][0],
              transference_array[8][0])


root.mainloop()
