#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <math.h>
#include <time.h>
#include <fstream>
#define PI 3.14


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

int sign(double Val) {
  if (Val == 0.)  return 0;
  if (Val > 0.)  return 1;
  else return -1;
}


//==================================
//
//         DRAW ALGORITHMS
//
//==================================


QImage DDA(QImage image, QPen pen, double xn, double yn, double xk, double yk,double *step_num)
{
    if (xn == xk && yn == yk)
    {
        image.setPixel(xn, yn, pen.color().rgb());
    }
    else
    {
        double xt = xn;
        double yt = yn;

        double dx = xk - xn;
        double dy = yk - yn;
        double L;

        if (fabs(dx) > fabs(dy))
            L = fabs(dx);
        else
            L = fabs(dy);


        dx = dx/L;
        dy = dy/L;

        *step_num = dy * L;

        for (int i = 1; i<(L+1); i++)
        {
            image.setPixel(xt, yt, pen.color().rgb());
            xt += dx;
            yt += dy;
        }
    }

    return image;
}


QImage brez_doub(QImage image, QPen pen, double xn, double yn, double xk, double yk, double *step_num)
{
    if (xn == xk && yn == yk)
        image.setPixel(xn, yn, pen.color().rgb());
    else
    {
        double dx = xk - xn;
        double dy = yk - yn;

        int sx = sign(dx);
        int sy = sign(dy);

        dx = fabs(dx);
        dy = fabs(dy);

        double m = dy/dx;

        int change = 0;
        double temp;

        if (m < 1)
            change = 0;
        else
        {
            temp = dx;
            dx = dy;
            dy = temp;
            change = 1;
            m = 1/m;
        }

        double error = m - 0.5;

        double xt = xn;
        double yt = yn;

        *step_num = dy;

        for (int i = 1; i<(dx+1); i++)
        {
            image.setPixel(xt, yt, pen.color().rgb());
            if (error >= 0)
            {
                if (change == 0)
                    yt += sy;
                else
                    xt += sx;

                error = error - 1;
            }
            if (error < 0)
            {
                if (change == 0)
                    xt += sx;
                else
                    yt += sy;

                error = error + m;
            }
        }
    }

    return image;
}


QImage brez_int(QImage image, QPen pen, double xn, double yn, double xk, double yk, double *step_num)
{
    if (xn == xk && yn == yk)
        image.setPixel(xn, yn,  pen.color().rgb());
    else
    {
        int xt = xn;
        int yt = yn;

        int dx = xk - xn;
        int dy = yk - yn;

        int sx = sign(dx);
        int sy = sign(dy);

        dx = fabs(dx);
        dy = fabs(dy);

        int change = 0;
        int temp;

        if (dx > dy)
            change = 0;
        else
        {
            temp = dy;
            dy = dx;
            dx = temp;
            change = 1;
        }

        int error = 2 * dy - dx;

        *step_num = dy;

        for (int i = 1; i<(dx+1); i++)
        {
            image.setPixel(xt, yt,  pen.color().rgb());
            if (error >= 0)
            {
                if (change == 0)
                    yt += sy;
                else
                    xt += sx;

                error -= 2 * dx;
            }
            if (error < 0)
            {
                if (change == 0)
                    xt += sx;
                else
                    yt += sy;

                error += 2 * dy;
            }
        }
    }

    return image;
}


QImage brez_smooth(QImage image, QPen pen, double xn, double yn, double xk, double yk, int R, int G, int B, double *step_num)
{
    double xt = xn, yt = yn;
    double dx = xk - xn, dy = yk - yn;
    int sx = sign(dx), sy = sign(dy);
    double i_max = 256;
    int change = 0;
    double temp;
    double e;
    double w;
    int i = 1;

    *step_num = dy;

    if (xn == xk && yn == yk)
        image.setPixel(xn, yn, pen.color().rgba());
    else
    {
        dx = fabs(dx);
        dy = fabs(dy);

        double m = dy/dx;

        if (m <= 1)
            change = 0;
        else
        {
            temp = dy;
            dy = dx;
            dx = temp;
            change = 1;
            m = 1/m;
        }

        m *= i_max;
        e = i_max/2;
        w = i_max - m;

        while (i <= dx)
        {
            double C = e/i_max;
            double red, green, blue;
            red = R + C*(255 - R);
            green = G + C*(255 - G);
            blue = B + C*(255 - B);
            pen.setColor(qRgb(red, green, blue));
            image.setPixel(xt, yt, pen.color().rgb());

            if (e <= w)
            {
                if (change == 1)
                {
                    yt += sy;
                }
                else
                {
                    xt += sx;
                }

                e += m;
            }
            else
            {
                xt += sx;
                yt += sy;
                e -= w;
            }

            i += 1;
        }
    }

    return image;
}


//=====================================
//
//              MENU
//
//=====================================

double param_array[8][100];
int count = 0;

void MainWindow::on_pushButton_clicked()
{
    QPen pen = QPen();
    double step_num_DDA;
    double step_num_brez_d;
    double step_num_brez_i;
    double step_num_brez_s;
    QImage image = QImage(398, 398, QImage::Format_RGB32);
    int R, G, B;
    int R_s, G_s, B_s;
    double xn,yn,xk,yk;


    if (ui->radioButton_6->isChecked())
    {
        R = G = B = 0;
    }
    else if (ui->radioButton_7->isChecked())
    {
        R = G = B = 255;
    }
    else if (ui->radioButton_8->isChecked())
    {
        R = 0;
        G = 255;
        B = 0;
    }
    else if (ui->radioButton_9->isChecked())
    {
        R = 255;
        G = 0;
        B = 0;
    }
    else if (ui->radioButton_10->isChecked())
    {
        R = 0;
        G = 0;
        B = 255;
    }


    if (ui->radioButton->isChecked())
    {
        R_s = G_s = B_s = 0;
    }
    else if (ui->radioButton_2->isChecked())
    {
        R_s = G_s = B_s = 255;
    }
    else if (ui->radioButton_3->isChecked())
    {
        R_s = 0;
        G_s = 255;
        B_s = 0;
    }
    else if (ui->radioButton_4->isChecked())
    {
        R_s = 255;
        G_s = 0;
        B_s = 0;
    }
    else if (ui->radioButton_5->isChecked())
    {
        R_s = 0;
        G_s = 0;
        B_s = 255;
    }

    image.fill(qRgb(R_s, G_s, B_s));

    xn = ui->lineEdit->text().toDouble();
    yn = ui->lineEdit_2->text().toDouble();

    xk = ui->lineEdit_3->text().toDouble();
    yk = ui->lineEdit_4->text().toDouble();

    if (ui->radioButton_11->isChecked())
        param_array[count][7] = 1;
    else if (ui->radioButton_12->isChecked())
        param_array[count][7] = 2;
    else if (ui->radioButton_13->isChecked())
        param_array[count][7] = 3;
    else if (ui->radioButton_14->isChecked())
        param_array[count][7] = 4;

    param_array[count][0] = xn;
    param_array[count][1] = yn;
    param_array[count][2] = xk;
    param_array[count][3] = yk;
    param_array[count][4] = R;
    param_array[count][5] = G;
    param_array[count][6] = B;


    for(int i = 0; i<=count; i++)
    {
        if (param_array[i][7] == 1)
        {
            pen.setColor(qRgb(param_array[i][4], param_array[i][5], param_array[i][6]));
            image = DDA(image ,pen, param_array[i][0], param_array[i][1], param_array[i][2],
                    param_array[i][3], &step_num_DDA);
        }
        else if (param_array[i][7] == 2)
        {
            pen.setColor(qRgb(param_array[i][4], param_array[i][5], param_array[i][6]));
            image = brez_doub(image, pen, param_array[i][0], param_array[i][1], param_array[i][2],
                    param_array[i][3], &step_num_brez_d);
        }
        else if (param_array[i][7] == 3)
        {
            pen.setColor(qRgb(param_array[i][4], param_array[i][5], param_array[i][6]));
            image = brez_int(image, pen, param_array[i][0], param_array[i][1], param_array[i][2],
                    param_array[i][3],  &step_num_brez_i);
        }
        else if (param_array[i][7] == 4)
        {
            pen.setColor(qRgb(param_array[i][4], param_array[i][5], param_array[i][6]));
            image = brez_smooth(image, pen, param_array[i][0], param_array[i][1], param_array[i][2],
                    param_array[i][3], param_array[i][4], param_array[i][5], param_array[i][6], &step_num_brez_s);
        }
    }

    count +=1;

    QGraphicsScene *graphic = new QGraphicsScene(this);
    graphic->addPixmap(QPixmap::fromImage(image));
    ui->graphicsView->setScene(graphic);
}

void MainWindow::on_pushButton_2_clicked()
{
    QColor color_screen;
    QPen pen = QPen();
    QImage image = QImage(398, 398, QImage::Format_RGB32);
    int R, G, B;
    double step_num_DDA;
    double step_num_brez_d;
    double step_num_brez_i;
    double step_num_brez_s;

    if (ui->radioButton_6->isChecked())
    {
        R = G = B = 0;
    }
    else if (ui->radioButton_7->isChecked())
    {
        R = G = B = 255;
    }
    else if (ui->radioButton_8->isChecked())
    {
        R = 0;
        G = 255;
        B = 0;
    }
    else if (ui->radioButton_9->isChecked())
    {
        R = 255;
        G = 0;
        B = 0;
    }
    else if (ui->radioButton_10->isChecked())
    {
        R = 0;
        G = 0;
        B = 255;
    }

    pen.setColor(qRgb(R, G, B));

    if (ui->radioButton->isChecked())
        color_screen = QColor(Qt::black);
    else if (ui->radioButton_2->isChecked())
        color_screen = QColor(Qt::white);
    else if (ui->radioButton_3->isChecked())
        color_screen = QColor(Qt::green);
    else if (ui->radioButton_4->isChecked())
        color_screen = QColor(Qt::red);
    else if (ui->radioButton_5->isChecked())
        color_screen = QColor(Qt::blue);

    image.fill(color_screen);

    double xn = 200;
    double yn = 200;

    double angle = ui->lineEdit_5->text().toDouble();
    double d = ui->lineEdit_6->text().toDouble();
    double xk;
    double yk;

    if (ui->radioButton_11->isChecked())
    {
        for(int i = 0; i<360; i += angle)
        {
            xk = cos(i * PI/180) * d + 200;
            yk = sin(i * PI/180) * d + 200;
            image = DDA(image ,pen, xn, yn, xk, yk, &step_num_DDA);
        }
    }
    else if (ui->radioButton_12->isChecked())
    {
        for(int i = 0; i<360; i += angle)
        {
            xk = cos(i * PI/180) * d + 200;
            yk = sin(i * PI/180) * d + 200;
            image = brez_doub(image, pen, xn, yn, xk, yk, &step_num_brez_d);
        }
    }
    else if (ui->radioButton_13->isChecked())
    {
        for(int i = 0; i<360; i += angle)
        {
            xk = cos(i * PI/180) * d + 200;
            yk = sin(i * PI/180) * d + 200;
            image = brez_int(image, pen, xn, yn, xk, yk,  &step_num_brez_i);
        }
    }
    else if (ui->radioButton_14->isChecked())
    {
        for(int i = 0; i<360; i += angle)
        {
            xk = cos(i * PI/180) * d + 200;
            yk = sin(i * PI/180) * d + 200;
            image = brez_smooth(image, pen, xn, yn, xk, yk, R, G, B, &step_num_brez_s);
        }
    }


    QGraphicsScene *graphic = new QGraphicsScene(this);
    graphic->addPixmap(QPixmap::fromImage(image));
    ui->graphicsView->setScene(graphic);

}

void MainWindow::on_pushButton_3_clicked()
{
    QColor color_screen;
    QPen pen = QPen();
    QImage image = QImage(398, 398, QImage::Format_RGB32);
    QCPBars *fossil;
    int R, G, B;
    double step_num_DDA;
    double step_num_brez_d;
    double step_num_brez_i;
    double step_num_brez_s;

    if (ui->radioButton_6->isChecked())
    {
        R = G = B = 0;
    }
    else if (ui->radioButton_7->isChecked())
    {
        R = G = B = 255;
    }
    else if (ui->radioButton_8->isChecked())
    {
        R = 0;
        G = 255;
        B = 0;
    }
    else if (ui->radioButton_9->isChecked())
    {
        R = 255;
        G = 0;
        B = 0;
    }
    else if (ui->radioButton_10->isChecked())
    {
        R = 0;
        G = 0;
        B = 255;
    }

    pen.setColor(qRgb(R, G, B));

    if (ui->radioButton->isChecked())
        color_screen = QColor(Qt::black);
    else if (ui->radioButton_2->isChecked())
        color_screen = QColor(Qt::white);
    else if (ui->radioButton_3->isChecked())
        color_screen = QColor(Qt::green);
    else if (ui->radioButton_4->isChecked())
        color_screen = QColor(Qt::red);
    else if (ui->radioButton_5->isChecked())
        color_screen = QColor(Qt::blue);

    image.fill(color_screen);

    double xn = 50;
    double yn = 30;

    double xk = 200;
    double yk = 100;
    float fTimeStart;
    float fTimeStop;

    fTimeStart = clock()/(float)CLOCKS_PER_SEC;
    image = DDA(image ,pen, xn, yn, xk, yk, &step_num_DDA);
    fTimeStop = clock()/(float)CLOCKS_PER_SEC;

    int N=4;
    QVector<double> x(N), y(N);

    x[0] = 1.0; y[0] = fTimeStop - fTimeStart;

    fTimeStart = clock()/(float)CLOCKS_PER_SEC;
    image = brez_doub(image, pen, xn, yn, xk, yk, &step_num_brez_d);
    fTimeStop = clock()/(float)CLOCKS_PER_SEC;

    x[1] = 2.0; y[1] = fTimeStop - fTimeStart;

    fTimeStart = clock()/(float)CLOCKS_PER_SEC;
    image = brez_int(image, pen, xn, yn, xk, yk,  &step_num_brez_i);
    fTimeStop = clock()/(float)CLOCKS_PER_SEC;

    x[2] = 3.0; y[2] = fTimeStop - fTimeStart;

    fTimeStart = clock()/(float)CLOCKS_PER_SEC;
    image = brez_smooth(image, pen, xn, yn, xk, yk, R, G, B, &step_num_brez_s);
    fTimeStop = clock()/(float)CLOCKS_PER_SEC;

    x[3] = 4.0; y[3] = fTimeStop - fTimeStart;

    double middle = (y[0] + y[1] + y[2] + y[3])/4.0;
    double min = 10000, max = -10000;

    for(int i = 0; i<4; i++)
    {
        if (y[i] > max)
            max = y[i];
        if (y[i] < min)
            min = y[i];
    }

    fossil = new QCPBars(ui->widget->xAxis, ui->widget->yAxis);

    ui->widget->hasPlottable(fossil);
    pen.setWidthF(1.5);
    fossil->setName(QString::fromUtf8("Гистограмма"));
    pen.setColor(QColor(50, 50, 100));// Цвет контура столбца
    fossil->setPen(pen);
    // Цвет самого столбца, четвертый параметр - прозрачность
    fossil->setBrush(QColor(50, 50, 250, 70));

    // Установки значений оси X:
    ui->widget->xAxis->setTickLength(0, 5);
    ui->widget->xAxis->grid()->setVisible(true);
    ui->widget->xAxis->setRange(0, 5);

    // Установки значений оси Y:
    ui->widget->yAxis->setRange(0, max + middle);
    ui->widget->yAxis->setPadding(5);
    ui->widget->yAxis->grid()->setSubGridVisible(true);
    QPen gridPen;
    gridPen.setStyle(Qt::SolidLine);
    gridPen.setColor(QColor(0, 0, 0, 25));
    ui->widget->yAxis->grid()->setPen(gridPen);
    gridPen.setStyle(Qt::DotLine);
    ui->widget->yAxis->grid()->setSubGridPen(gridPen);

    fossil->setData(x, y);

    ui->widget->replot();

    ui->widget->removePlottable(fossil);
}

void MainWindow::on_pushButton_4_clicked()
{
    QColor color_screen;
    QPen pen = QPen();
    QImage image = QImage(398, 398, QImage::Format_RGB32);

    int R, G, B;
    double step_num;

    if (ui->radioButton_6->isChecked())
    {
        R = G = B = 0;
    }
    else if (ui->radioButton_7->isChecked())
    {
        R = G = B = 255;
    }
    else if (ui->radioButton_8->isChecked())
    {
        R = 0;
        G = 255;
        B = 0;
    }
    else if (ui->radioButton_9->isChecked())
    {
        R = 255;
        G = 0;
        B = 0;
    }
    else if (ui->radioButton_10->isChecked())
    {
        R = 0;
        G = 0;
        B = 255;
    }

    pen.setColor(qRgb(R, G, B));

    if (ui->radioButton->isChecked())
        color_screen = QColor(Qt::black);
    else if (ui->radioButton_2->isChecked())
        color_screen = QColor(Qt::white);
    else if (ui->radioButton_3->isChecked())
        color_screen = QColor(Qt::green);
    else if (ui->radioButton_4->isChecked())
        color_screen = QColor(Qt::red);
    else if (ui->radioButton_5->isChecked())
        color_screen = QColor(Qt::blue);

    image.fill(color_screen);

    double xn = 200;
    double yn = 200;

    double angle = 20;
    double d = 150;
    double xk;
    double yk;
    int N=4;
    int j = 0;
    QVector<double> x(N), y(N);

    if (ui->radioButton_11->isChecked())
    {
        for(int i = 20; i<=80; i += angle)
        {
            xk = cos(i * PI/180) * d + 200;
            yk = sin(i * PI/180) * d + 200;
            image = DDA(image ,pen, xn, yn, xk, yk, &step_num);
            x[j] = j; y[j] = (yk-yn)/step_num;
            j += 1;
        }
    }
    else if (ui->radioButton_12->isChecked())
    {
        for(int i = 20; i<=80; i += angle)
        {
            xk = cos(i * PI/180) * d + 200;
            yk = sin(i * PI/180) * d + 200;
            image = brez_doub(image, pen, xn, yn, xk, yk, &step_num);
            x[j] = j; y[j] = 1;
            j += 1;
        }
    }
    else if (ui->radioButton_13->isChecked())
    {
        for(int i = 20; i<=80; i += angle)
        {
            xk = cos(i * PI/180) * d + 200;
            yk = sin(i * PI/180) * d + 200;
            image = brez_int(image, pen, xn, yn, xk, yk,  &step_num);
            x[j] = j; y[j] = 1;
            j += 1;
        }
    }
    else if (ui->radioButton_14->isChecked())
    {
        for(int i = 20; i<=80; i += angle)
        {
            xk = cos(i * PI/180) * d + 200;
            yk = sin(i * PI/180) * d + 200;
            image = brez_smooth(image, pen, xn, yn, xk, yk, R, G, B, &step_num);
            x[j] = j; y[j] = (yk-yn)/step_num;
            j += 1;
        }
    }

    ui->widget->clearGraphs();
    ui->widget->addGraph();
    ui->widget->graph(0)->setData(x, y);
    ui->widget->graph(0)->setPen(QColor(50, 50, 50, 255));

    ui->widget->xAxis->setLabel("x");
    ui->widget->yAxis->setLabel("y");

    ui->widget->xAxis->setRange(0, 5);

    double max=-100000;
    for(int i = 1; i<(j-1);i++)
    {
        if(y[i] > max)
            max = y[i];
    }

    ui->widget->yAxis->setRange(0, max);
    ui->widget->replot();



}

void MainWindow::on_pushButton_5_clicked()
{
    QImage image = QImage(398, 398, QImage::Format_RGB32);

    for(int i = 0; i<count; i++)
    {
        for(int j = 0; j<count; j++)
            param_array[i][j] = 0;
    }

    image.fill(Qt::white);
    QGraphicsScene *graphic = new QGraphicsScene(this);
    graphic->addPixmap(QPixmap::fromImage(image));
    ui->graphicsView->setScene(graphic);


}
