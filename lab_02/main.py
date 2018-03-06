from tkinter import *
from sympy import *
from math import *
from math_part import *

def read_array(file):
    f = open(file, 'r')
    params_array = []
    tmp = []
    tmp = f.read().split('\n')
    mask = [14, 15, 17]


    for i in range(len(tmp)):
        if i not in mask:
            params_array.append(tmp[i].split(' '))
        elif i in mask and tmp[i] != '':
            a = tmp[i].split(',')
            b = []
            for j in range(len(a)):
                b.append(a[j].split(' '))
            params_array.append(b)

    for i in range(len(params_array)):
        for j in range(len(params_array[i])):
            if i not in mask:
                params_array[i][j] = float(params_array[i][j])
            else:
                for k in range(len(params_array[i][j])):
                    params_array[i][j][k] = float(params_array[i][j][k])

    params_array[16] = params_array[16][0]

    return params_array

def write_array(file, param_array):
    f = open(file, "w")
    mask = [14, 15, 16]
    for i in range(len(param_array)):
        if i not in mask:
            for j in range(len(param_array[i])):
                f.write(str(param_array[i][j]))
                if j != len(param_array[i]) - 1:
                    f.write(' ')
            f.write('\n')
        elif i in mask and i != 16:
            for z in range(len(param_array[i])):
                for k in range(len(param_array[i][z])):
                    f.write(str(param_array[i][z][k]))
                    if k != len(param_array[i][z]) - 1:
                        f.write(' ')
                if z != len(param_array[i]) - 1:
                    f.write(',')
            f.write('\n')
    f.write(str(param_array[16]))

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

    x = (-a*(sqrt(2)/2))
    y = (b*(sqrt(2)/2))

    x1 = 520 + center[0] + (-x * cos(radians(phi)) + y * (-sin(radians(phi))))
    y1 = 317 + center[1] + (-x * sin(radians(phi)) + y * cos(radians(phi)))
    x2 = 520 + center[0] + (x * cos(radians(phi)) - y * (-sin(radians(phi))))
    y2 = 317 + center[1] + (x * sin(radians(phi)) - y * cos(radians(phi)))
    x3 = 520 + center[0] + (x * cos(radians(phi)) + y * (-sin(radians(phi))))
    y3 = 317 + center[1] + (x * sin(radians(phi)) + y * cos(radians(phi)))
    x4 = 520 + center[0] + (-x * cos(radians(phi)) - y * (-sin(radians(phi))))
    y4 = 317 + center[1] + (-x * sin(radians(phi)) - y * cos(radians(phi)))

    cross_points1 = [[x1, y1],[x2, y2]]
    cross_points2 = [[x3, y3], [x4, y4]]
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

def transf(dx, dy):

    clean()

    params_array = read_array("array")
    write_array("step_back", params_array)

    transference_array = transference(params_array, dx, dy)

    # отрисовка фигуры с новыми координатами
    create_figure(transference_array[0], transference_array[1],
              transference_array[2], transference_array[3],
              transference_array[4], transference_array[5],
              transference_array[6], transference_array[7],
              transference_array[8], transference_array[9],
              transference_array[10], transference_array[11],
              transference_array[12], transference_array[13],
              transference_array[14], transference_array[15], transference_array[16])

    canvas.create_line(520, 20, 520, 620, width=1, arrow=FIRST, fill='black')  # ось У
    canvas.create_line(20, 320, 1020, 320, width=1, arrow=LAST, fill='black')  # ось X

    write_array("array", transference_array)

def scale(xm, ym, kx, ky):

    clean()

    params_array = read_array("array")
    write_array("step_back", params_array)

    # новые каоординаты после масштабирования
    scaling_array = scaling(params_array, xm, ym, kx, ky)

    # отрисовка фигуры с новыми координатами
    create_figure(scaling_array[0], scaling_array[1],
                   scaling_array[2], scaling_array[3],
                   scaling_array[4], scaling_array[5],
                   scaling_array[6], scaling_array[7],
                   scaling_array[8], scaling_array[9],
                   scaling_array[10], scaling_array[11],
                   scaling_array[12], scaling_array[13],
                   scaling_array[14], scaling_array[15], scaling_array[16])

    canvas.create_line(520, 20, 520, 620, width=1, arrow=FIRST, fill='black')  # ось У
    canvas.create_line(20, 320, 1020, 320, width=1, arrow=LAST, fill='black')  # ось X

    write_array("array", scaling_array)

def rot(xm, ym, phi):

    clean()

    params_array = read_array("array")
    write_array("step_back", params_array)

    rotate_array = rotate(params_array, xm, ym, phi)

    # отрисовка фигуры с новыми координатами
    create_figure(rotate_array[0], rotate_array[1],
                  rotate_array[2], rotate_array[3],
                  rotate_array[4], rotate_array[5],
                  rotate_array[6], rotate_array[7],
                  rotate_array[8], rotate_array[9],
                  rotate_array[10],rotate_array[11],
                  rotate_array[12], rotate_array[13],
                  rotate_array[14], rotate_array[15], rotate_array[16])

    canvas.create_line(520, 20, 520, 620, width=1, arrow=FIRST, fill='black')  # ось У
    canvas.create_line(20, 320, 1020, 320, width=1, arrow=LAST, fill='black')  # ось X

    write_array("array", rotate_array)


def clean():
    canvas.delete('all')

def reset():

    clean()

    zero_params_array = [[-145, 0, 1], [35, 35, 1], [0, 85, 1], [35, 35, 1], [145, 0, 1], [35, 35, 1],
                         [0, -85, 1], [35, 35, 1], [0, 0, 1], [20, 20, 1], [0, 0, 1],
                         [180, 120, 1], [0, 0, 1], [110, 50, 1], [[0, 0, 1], [-180, 180, 1], [-70, 180, 1]],
                         [[0, 0, 1], [180, 180, 1], [70, 180, 1]], 0]

    write_array("array", zero_params_array)

    create_figure([-145, 0], [35, 35], [0, 85], [35, 35], [145, 0], [35, 35], [0, -85], [35, 35],
                                [0, 0], [20, 20], [0, 0], [180, 120], [0, 0], [110, 50],
                                [[0, 0], [-180, 180], [-70, 180]],
                                [[0, 0], [180, 180], [70, 180]], 0)

    canvas.create_line(520, 20, 520, 620, width=1, arrow=FIRST, fill='black')  # ось У
    canvas.create_line(20, 320, 1020, 320, width=1, arrow=LAST, fill='black')  # ось X

def step_back():

    clean()

    params_array = read_array("step_back")

    create_figure(params_array[0], params_array[1],
                  params_array[2], params_array[3],
                  params_array[4], params_array[5],
                  params_array[6], params_array[7],
                  params_array[8], params_array[9],
                  params_array[10], params_array[11],
                  params_array[12], params_array[13],
                  params_array[14], params_array[15], params_array[16])

    write_array("array", params_array)

    canvas.create_line(520, 20, 520, 620, width=1, arrow=FIRST, fill='black')  # ось У
    canvas.create_line(20, 320, 1020, 320, width=1, arrow=LAST, fill='black')  # ось X

root = Tk()
root.title('My app')
root.geometry('1320x640')

canvas = Canvas(root, width=1040, height=640, bg='white')
canvas.pack(side='right')

# смещение по x
x = 15
# смещение по y
y = 80

# начальная кофигурация расположиения фигуры (0, 0)

zero_params_array = [[-145, 0, 1], [35, 35, 1], [0, 85, 1], [35, 35, 1], [145, 0, 1], [35, 35, 1],
                     [0, -85, 1], [35, 35, 1], [0, 0, 1], [20, 20, 1], [0, 0, 1],
                     [180, 120, 1], [0, 0, 1], [110, 50, 1], [[0, 0, 1], [-180, 180, 1], [-70, 180, 1]],
                    [[0, 0, 1], [180, 180, 1], [70, 180, 1]], 0]

write_array("array",zero_params_array)

# отрисовка фигуры с начальными параметрами
zero_figure = create_figure([-145, 0], [35,35], [0, 85], [35,35], [145, 0], [35,35], [0, -85], [35,35],
              [0, 0], [20,20], [0, 0], [180, 120], [0, 0], [110, 50], [[0,0],[-180, 180],[-70, 180]],
              [[0, 0], [180, 180], [70, 180]],0)

# Меню
label_rep_dx = Label(root, text='dx:')
label_rep_dx.place(x=x, y=y)
entry_rep_dx = Entry(root, width=25)
entry_rep_dx.place(x=x+25, y=y)

label_rep_dy = Label(root, text='dy:')
label_rep_dy.place(x=x, y=y+30)
entry_rep_dy = Entry(root, width=25)
entry_rep_dy.place(x=x+25, y=y+30)

btn_rep = Button(root, text='Переместить', width=25)
btn_rep.bind('<Button-1>', lambda event: transf(float(entry_rep_dx.get()),
                                                     float(entry_rep_dy.get())))
btn_rep.place(x=x, y=y+70)

label_sc_cent_x = Label(root, text='xm:')
label_sc_cent_x.place(x=x, y=y+140)
entry_sc_cent_x = Entry(root, width=25)
entry_sc_cent_x.place(x=x+25, y=y+140)

label_sc_cent_y = Label(root, text='ym:')
label_sc_cent_y.place(x=x, y=y+170)
entry_sc_cent_y = Entry(root, width=25)
entry_sc_cent_y.place(x=x+25, y=y+170)

label_sc_kx = Label(root, text='kx:')
label_sc_kx.place(x=x, y=y+200)
entry_sc_kx = Entry(root, width=25)
entry_sc_kx.place(x=x+25, y=y+200)

label_sc_ky = Label(root, text='ky:')
label_sc_ky.place(x=x, y=y+230)
entry_sc_ky = Entry(root, width=25)
entry_sc_ky.place(x=x+25, y=y+230)

btn_sc = Button(root, text='Масштабировать', width=25)
btn_sc.bind('<Button-1>', lambda event: scale(float(entry_sc_cent_x.get()), float(entry_sc_cent_y.get()),
                                              float(entry_sc_kx.get()), float(entry_sc_ky.get())))
btn_sc.place(x=x, y=y+270)

label_rt_cent_x = Label(root, text='xm:')
label_rt_cent_x.place(x=x, y=y+340)
entry_rt_cent_x = Entry(root, width=25)
entry_rt_cent_x.place(x=x+25, y=y+340)

label_rt_cent_y = Label(root, text='ym:')
label_rt_cent_y.place(x=x, y=y+370)
entry_rt_cent_y = Entry(root, width=25)
entry_rt_cent_y.place(x=x+25, y=y+370)

label_rt_ang = Label(root, text='ang:')
label_rt_ang.place(x=x, y=y+400)
entry_rt_ang = Entry(root, width=24)
entry_rt_ang.place(x=x+28, y=y+400)

btn_res = Button(root, text='Поворот', width=25)
btn_res.bind('<Button-1>', lambda event: rot(float(entry_rt_cent_x.get()), float(entry_rt_cent_y.get()),
                                              float(entry_rt_ang.get())))
btn_res.place(x=x, y=y+440)

btn_res = Button(root, text='Сброс', width=25)
btn_res.bind('<Button-1>', lambda event: reset())
btn_res.place(x=x, y=y+470)

btn_res = Button(root, text='Шаг назад', width=25)
btn_res.bind('<Button-1>', lambda event: step_back())
btn_res.place(x=x, y=y+500)



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
#              transference_array[14], transference_array[15],
#              transference_array[16])


'''Демонтрация функции масштабирования
    Вход: матрица параметров фигуры, центр масштабировния(x, y), 
    коэффциенты масштабирования(kx, ky);
    Выход: матрица обновленных параметров'''

# новые каоординаты после масштабирования
#scaling_array = scaling(zero_params_array, 0, 0, 1.5, 2.5)

# отрисовка фигуры с новыми координатами
#create_figure(scaling_array[0], scaling_array[1],
#              scaling_array[2], scaling_array[3],
#              scaling_array[4], scaling_array[5],
#              scaling_array[6], scaling_array[7],
#              scaling_array[8], scaling_array[9],
#              scaling_array[10], scaling_array[11],
#              scaling_array[12], scaling_array[13],
#              scaling_array[14], scaling_array[15], 0)


'''Демонстрация функции поворота
    Вход: матрица параметров фигуры, центр поворота (x, y),
    угол поворота(phi);
    Выход: матрица обновленных параметров'''

# новые координаты после масштабирования
#phi = 90
#center = [145, 0]

#rotate_array = rotate(zero_params_array, center[0], center[1], phi)

# отрисовка фигуры с новыми координатами
#create_figure(rotate_array[0], rotate_array[1],
#              rotate_array[2], rotate_array[3],
#              rotate_array[4], rotate_array[5],
#              rotate_array[6], rotate_array[7],
#              rotate_array[8], rotate_array[9],
#              rotate_array[10],rotate_array[11],
#              rotate_array[12], rotate_array[13],
#              rotate_array[14], rotate_array[15], phi)

#draw_ellipse(center, 5, 5, 0, "blue")

canvas.create_line(520,20,520,620,width=1,arrow=FIRST,fill='black') #ось У
canvas.create_line(20, 320, 1020, 320,width=1,arrow=LAST, fill='black') #ось X


root.mainloop()
