#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <cmath>
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


//=========================
//
//       ALGORITHMS
//
//=========================

//CIRCLE CANONICH
QImage canon_circle(QImage image, QPen pen, double xc, double yc, double R)
{
    //Start params
    //===========
    double X = 0;
    double Y = 0;
    //===========

    for (int i = 0; i < R + 1; i++)
    {
        Y = round(sqrt(R * R - i * i));
        image.setPixel(xc + i, yc + Y, pen.color().rgb());
        image.setPixel(xc + i, yc - Y, pen.color().rgb());
        image.setPixel(xc - i, yc + Y, pen.color().rgb());
        image.setPixel(xc - i, yc - Y, pen.color().rgb());
    }

    for (int i = 0; i < R + 1; i++)
    {
        X = round(sqrt(R * R - i * i));
        image.setPixel(xc + X, yc + i, pen.color().rgb());
        image.setPixel(xc + X, yc - i, pen.color().rgb());
        image.setPixel(xc - X, yc + i, pen.color().rgb());
        image.setPixel(xc - X, yc - i, pen.color().rgb());
    }


    return image;
}


//CIRCLE PARAMS
QImage circle_param(QImage image, QPen pen, double xc, double yc, double R)
{
    //Start params
    //===========
    double X = 0;
    double Y = 0;
    double l = round(PI * R/2); // square size of circle
    //===========

    for(int i = 0; l + 1; i++)
    {
        X = round(R * cos(i / R));
        Y = round(R * sin(i / R));
        image.setPixel(xc + X, yc + Y, pen.color().rgb());
        image.setPixel(xc + X, yc - Y, pen.color().rgb());
        image.setPixel(xc - X, yc + Y, pen.color().rgb());
        image.setPixel(xc - X, yc - Y, pen.color().rgb());

    }

    return image;
}


//CIRCLE BREZENHEM
QImage brez_circle(QImage image, QPen pen, double xc, double yc, double R)
{
    //Start params
    //===========
    double X = 0;
    double Y = R;
    double D = 2 * (1 - R);
    double YE = 0;
    double D1;
    double D2;
    //===========

    //Algorithm
    while(Y > YE)
    {
        //1.First pixel
        image.setPixel(xc + X, yc + Y, pen.color().rgb());
        image.setPixel(xc + X, yc - Y, pen.color().rgb());
        image.setPixel(xc - X, yc + Y, pen.color().rgb());
        image.setPixel(xc - X, yc - Y, pen.color().rgb());

        //2.Analize D
        if(D < 0)
        {
            D1 = 2 * D + 2 * Y - 1;
            //Horizontal step
            if(D1 <= 0)
            {
                X++;
                D = D + 2 * X + 1;
            }
            //Diagonal step
            else if(D1 > 0)
            {
                X++;
                Y--;
                D = D + 2 * (X - Y + 1);
            }
        }
        //Horizontal step
        else if(D == 0)
        {
            X++;
            Y--;
            D = D + 2 * (X - Y + 1);
        }
        else if(D > 0)
        {
            D2 = 2 * D - 2 * X - 1;
            //Diagonal step
            if(D2 <= 0)
            {
                X++;
                Y--;
                D = D + 2 * (X - Y + 1);
            }
            //Vertical step
            else if(D2 > 0)
            {
                Y--;
                D = D - 2 * Y + 1;
            }
        }
    }

    //Result
    return image;
}


//ELLIPSE MIDDLE POINT
QImage ellipse_middle(QImage image, QPen pen, double xc, double yc, double a, double b)
{
    //Start params
    //===========
    double X = 0;
    double Y = b;
    double p = b * b - a * a + 0.25 * a * a;
    //===========

    while((2 * b * b * X) < (2 * a * a * Y))
    {
        image.setPixel(xc - X,yc + Y, pen.color().rgb());
        image.setPixel(xc + X,yc - Y, pen.color().rgb());
        image.setPixel(xc - X,yc + Y, pen.color().rgb());
        image.setPixel(xc + X,yc - Y, pen.color().rgb());

        X++;

        if(p < 0)
        {
            p += 2 * b * b * X + b * b;
        }
        else
        {
            Y--;
            p += 2 * b * b * X - 2 * a * a * Y + b * b;
        }
    }

    p = b * b * (X + 0.5) * (X + 0.5) + a * a * (Y - 1) * (Y - 1) - a * a * b * b;

    while(Y >= 0)
    {
        image.setPixel(xc - X,yc + Y, pen.color().rgb());
        image.setPixel(xc + X,yc - Y, pen.color().rgb());
        image.setPixel(xc - X,yc + Y, pen.color().rgb());
        image.setPixel(xc + X,yc - Y, pen.color().rgb());

        Y--;

        if(p > 0)
        {
            p -= 2 * a * a * Y + a * a;
        }
        else
        {
            X++;
            p += 2 * b * b * X - 2 * a * a * Y + a * a;
        }
    }


    return image;

}


//CIRCLE MIDDLE POINTS
QImage circle_middle_points(QImage image, QPen pen, double xc, double yc, double R)
{
    //Start params
    //===========
    double X = 0;
    double Y = R;
    double p = 5/4 - R; // (x + 1)^2 + (y - 1/2)^2 - r^2
    //===========

    while(X > Y)
    {
        image.setPixel(xc - X,yc + Y, pen.color().rgb());
        image.setPixel(xc + X,yc - Y, pen.color().rgb());
        image.setPixel(xc - X,yc + Y, pen.color().rgb());
        image.setPixel(xc + X,yc - Y, pen.color().rgb());

        image.setPixel(xc - Y,yc + X, pen.color().rgb());
        image.setPixel(xc + Y,yc - X, pen.color().rgb());
        image.setPixel(xc - Y,yc + X, pen.color().rgb());
        image.setPixel(xc + Y,yc - X, pen.color().rgb());

        X++;

        if(p < 0)
        {
            p += 2 * X + 1;
        }
        else
        {
            p += 2 * X - 2 * Y + 5;
            Y--;
        }

    }

    return image;
}


//ELLIPSE CANONICH
QImage ellipse_circle(QImage image, QPen pen, double xc, double yc, double a, double b)
{
    //Start params
    //===========
    double X = 0;
    double Y = 0;
    //===========

    for (int i = 0; i < a + 1; i++)
    {
        Y = round(b * sqrt(1.0 - (i * i)/(a*a)));
        image.setPixel(xc + i, yc + Y, pen.color().rgb());
        image.setPixel(xc + i, yc - Y, pen.color().rgb());
        image.setPixel(xc - i, yc + Y, pen.color().rgb());
        image.setPixel(xc - i, yc - Y, pen.color().rgb());
    }

    for (int i = 0; i < b + 1; i++)
    {
        X = round(a * sqrt(1.0 - (i * i)/(b * b)));
        image.setPixel(xc + X, yc + i, pen.color().rgb());
        image.setPixel(xc + X, yc - i, pen.color().rgb());
        image.setPixel(xc - X, yc + i, pen.color().rgb());
        image.setPixel(xc - X, yc - i, pen.color().rgb());
    }


    return image;
}


//ELLIPSE PARAMS
QImage circle_param(QImage image, QPen pen, double xc, double yc, double a, double b)
{
    //Start params
    //===========
    double X = 0;
    double Y = b;
    double max = std::max(a, b);
    double l = round(PI * max / 2);
    //===========

    for(int i = 0; l + 1; i++)
    {
        X = round(a * cos(i / max));
        Y = round(b * sin(i / max));
        image.setPixel(xc + X, yc + Y, pen.color().rgb());
        image.setPixel(xc + X, yc - Y, pen.color().rgb());
        image.setPixel(xc - X, yc + Y, pen.color().rgb());
        image.setPixel(xc - X, yc - Y, pen.color().rgb());

    }

    return image;
}


//ELLIPSE BREZENHEM
QImage brez_ellipse(QImage image, QPen pen, double xc, double yc, double a, double b)
{
    //Start params
    //===========
    double X = 0;
    double Y = b;
    double D = round(b * b / 2 - a * b * 2 + a / 2);
    double D1;
    double D2;
    b = b * b;
    //===========

    while(Y >= 0)
    {
        image.setPixel(xc + X, yc + Y, pen.color().rgb());
        image.setPixel(xc + X, yc - Y, pen.color().rgb());
        image.setPixel(xc - X, yc + Y, pen.color().rgb());
        image.setPixel(xc - X, yc - Y, pen.color().rgb());

        if (D < 0)
        {
            D1 = 2 * D + 2 * a * Y - a;
            X++;
            if(D1 <= 0)
            {
                D = D + 2 * b * X + b;
            }
            else
            {
                Y--;
                D = D + 2 * b * X - 2 * a * Y + a + b;
            }
        }

        if (D > 0)
        {
            D2 = 2 * D - 2 * b * X - b;
            Y--;

            if(D2 > 0)
            {
                D = D - 2 * Y * a + a;
            }
            else
            {
                X++;
                D = D + 2 * X * b - 2 * Y * a + a + b;
            }
        }

        if (D == 0.0)
        {
            X++;
            Y--;
            D = D + 2 * X * b - 2 * Y * a + a + b;
        }
    }

    return image;

}


//====================================
//
//             MENU
//
//====================================


