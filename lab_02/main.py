from tkinter import *
from sympy import *
from math import *
from math_part import *

def draw_ellipse(center, a, b, phi, color):
    '''Рисует эллипс'''

    points_array = []
    j = 0

    for i in range(0, 7168, 1):
        j+= 0.05
        x = a * cos(j)
        y = b * sin(j)
        points_array.append([(520 + (x * cos(radians(phi)) + y * sin(radians(phi)))
                              + center[0]), 317 - (x * (-sin(radians(phi))) + y * cos(radians(phi))) + center[1]])

    canvas.create_polygon(points_array, fill=color, outline=color, smooth=1)

def draw_cross(center, a, b, phi, color):
    '''Рисует перекрестие'''

    x1 = (center[0] - a*(sqrt(2)/2))
    y1 = (center[1] + b*(sqrt(2)/2))
    x2 = (center[0] + a*(sqrt(2)/2))
    y2 = (center[1] - b*(sqrt(2)/2))
    x3 = (center[0] + a*(sqrt(2)/2))
    y3 = (center[1] + b*(sqrt(2)/2))
    x4 = (center[0] - a*(sqrt(2)/2))
    y4 = (center[1] - b*(sqrt(2)/2))

    if center[0] == 0 and center[1] == 0:
        x5 = 520 + (x1 * cos(radians(phi)) + y1 * (-sin(radians(phi))))
        y5 = 317 + (x1 * sin(radians(phi)) + y1 * cos(radians(phi)))
        x6 = 520 + (x2 * cos(radians(phi)) + y2 * (-sin(radians(phi))))
        y6 = 317 + (x2 * sin(radians(phi)) + y2 * cos(radians(phi)))
        x7 = 520 + (x3 * cos(radians(phi)) + y3 * (-sin(radians(phi))))
        y7 = 317 + (x3 * sin(radians(phi)) + y3 * cos(radians(phi)))
        x8 = 520 + (x4 * cos(radians(phi)) + y4 * (-sin(radians(phi))))
        y8 = 317 + (x4 * sin(radians(phi)) + y4 * cos(radians(phi)))
    else:
        x5 = 520 + center[0] + (-a*(sqrt(2)/2) * cos(radians(phi)) + b * (sqrt(2)/2) * (-sin(radians(phi))))
        y5 = 317 + center[1] + (-a*(sqrt(2)/2) * sin(radians(phi)) +b*(sqrt(2)/2) * cos(radians(phi)))
        x6 = 520 + center[0] + (a*(sqrt(2)/2) * cos(radians(phi)) - b * (sqrt(2)/2) * (-sin(radians(phi))))
        y6 = 317 + center[1] + (a*(sqrt(2)/2) * sin(radians(phi)) - b*(sqrt(2)/2) * cos(radians(phi)))
        x7 = 520 + center[0] + (a*(sqrt(2)/2) * cos(radians(phi)) + b * (sqrt(2)/2) * (-sin(radians(phi))))
        y7 = 317 + center[1] + (a*(sqrt(2)/2) * sin(radians(phi)) + b*(sqrt(2)/2) * cos(radians(phi)))
        x8 = 520 + center[0] + (-a*(sqrt(2)/2) * cos(radians(phi)) - b * (sqrt(2)/2) * (-sin(radians(phi))))
        y8 = 317 + center[1] + (-a*(sqrt(2)/2) * sin(radians(phi)) - b*(sqrt(2)/2) * cos(radians(phi)))

    cross_points1 = [[x5, y5],[x6, y6]]
    cross_points2 = [[x7, y7], [x8, y8]]
    canvas.create_line(cross_points1, fill=color, width=3)
    canvas.create_line(cross_points2, fill=color, width=3)

def create_figure(center_circle1, radius_circle1, center_circle2, radius_circle2, center_circle3,
                  radius_circle3, center_circle4, radius_circle4,
                  center_circle5, radius_circle5,
                  center_outside_ellipse, ab_outside_ellipse,
                  center_inside_ellipse, ab_inside_ellipse,
                  triangle1_points, triangle2_points, phi):
    '''Строит заданную фигуру'''

    # Наружный эллпис
    draw_ellipse(center_outside_ellipse, ab_outside_ellipse[0], ab_outside_ellipse[1], phi, "green")
    # Внутренний эллипс
    draw_ellipse(center_inside_ellipse, ab_inside_ellipse[0], ab_inside_ellipse[1], phi, "white")

    # Четыре окружности в эллипсе
    draw_ellipse(center_circle1, radius_circle1[0],radius_circle1[1], phi, "yellow")
    draw_ellipse(center_circle2, radius_circle2[0], radius_circle2[1], phi, "yellow")
    draw_ellipse(center_circle3, radius_circle3[0], radius_circle3[1], phi, "yellow")
    draw_ellipse(center_circle4, radius_circle4[0], radius_circle4[1], phi, "yellow")

    # Окружность посередине
    draw_ellipse(center_circle5, radius_circle5[0], radius_circle5[1], phi, "red")

    # Построение перекрестия у боковых окружностей
    draw_cross(center_circle1, radius_circle1[0], radius_circle1[1], phi, "red")
    draw_cross(center_circle2, radius_circle2[0], radius_circle2[1], phi, "red")
    draw_cross(center_circle3, radius_circle3[0], radius_circle3[1], phi, "red")
    draw_cross(center_circle4, radius_circle4[0], radius_circle4[1], phi, "red")

    # Построение перекрестия в центре
    draw_cross(center_inside_ellipse, ab_inside_ellipse[0], ab_inside_ellipse[1], phi, "red")


    # Построение треугольников
    canvas.create_polygon([520 + triangle1_points[0][0], 317 + triangle1_points[0][1]],
                          [520 + triangle1_points[1][0], 317 + triangle1_points[1][1]],
                          [520 + triangle1_points[2][0], 317 + triangle1_points[2][1]],
                          fill="black")

    canvas.create_polygon([520 + triangle2_points[0][0], 317 + triangle2_points[0][1]],
                          [520 + triangle2_points[1][0], 317 + triangle2_points[1][1]],
                          [520 + triangle2_points[2][0], 317 + triangle2_points[2][1]],
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

# начальная кофигурация расположиения фигуры (0, 0)
zero_params_array = [[-145, 0, 1], [35, 35, 1], [0, 85, 1], [35, 35, 1], [145, 0, 1], [35, 35, 1],
                     [0, -85, 1], [35, 35, 1], [0, 0, 1], [20, 20, 1], [0, 0, 1],
                     [180, 120, 1], [0, 0, 1], [110, 50, 1], [[0, 0, 1], [-180, 180, 1], [-70, 180, 1]],
                    [[0, 0, 1], [180, 180, 1], [70, 180, 1]],0]

# отрисовка фигуры с начальными параметрами
#create_figure([-145, 0], [35,35], [0, 85], [35,35], [145, 0], [35,35], [0, -85], [35,35],
#              [0, 0], [20,20], [0, 0], [180, 120], [0, 0], [110, 50], [[0,0],[-180, 180],[-70, 180]],
#              [[0, 0], [180, 180], [70, 180]],0)







'''Демонстрация функции перемещения
    Вход:матрица параметров фигуры, перемещение по x (dx), 
    перемещение по y (dy)
    Выход:матрица обновленных параметров'''

# новые координаты после перемещения
#transference_array = transference(zero_params_array, 100, 40)

# отрисовка фигуры с новыми координатами
#create_figure(transference_array[0], transference_array[1],
#              transference_array[2], transference_array[3],
#              transference_array[4], transference_array[5],
#              transference_array[6], transference_array[7],
#              transference_array[8], transference_array[9],
#              transference_array[10], transference_array[11],
#              transference_array[12], transference_array[13],
#              transference_array[14], transference_array[15], 0)


'''Демонтрация функции масштабирования
    Вход: матрица параметров фигуры, центр масштабировния(x, y), 
    коэффциенты масштабирования(kx, ky);
    Выход: матрица обновленных параметров'''

# ДОБАВИТЬ ФУНКЦИОНАЛ С ЦЕНТРОМ МАСШТАБИРОВАНИЯ (xm, ym)

# новые каоординаты после масштабирования
#scaling_array = scaling(zero_params_array, 0, 0, 2, 2)

# отрисовка фигуры с новыми координатами
#create_figure(scaling_array[0], scaling_array[1],
#              scaling_array[2], scaling_array[3],
#              scaling_array[4], scaling_array[5],
#              scaling_array[6], scaling_array[7],
#              scaling_array[8], scaling_array[9],
#              scaling_array[10],scaling_array[11],
#              scaling_array[12], scaling_array[13],
#              scaling_array[14], scaling_array[15], 0)


'''Демонстрация функции поворота
    Вход: матрица параметров фигуры, центр поворота (x, y),
    угол поворота(phi);
    Выход: матрица обновленных параметров'''

# новые координаты после масштабирования
phi = 10
center = [72.5, -85]

rotate_array = rotate(zero_params_array, center[0], -center[1], phi)

# отрисовка фигуры с новыми координатами
create_figure(rotate_array[0], rotate_array[1],
              rotate_array[2], rotate_array[3],
              rotate_array[4], rotate_array[5],
              rotate_array[6], rotate_array[7],
              rotate_array[8], rotate_array[9],
              rotate_array[10],rotate_array[11],
              rotate_array[12], rotate_array[13],
              rotate_array[14], rotate_array[15], phi)

draw_ellipse(center, 5, 5, 0, "blue")

canvas.create_line(520,20,520,620,width=1,arrow=FIRST,fill='black') #ось У
canvas.create_line(20, 320, 1020, 320,width=1,arrow=LAST, fill='black') #ось X


root.mainloop()
