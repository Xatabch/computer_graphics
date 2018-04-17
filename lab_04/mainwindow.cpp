#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <cmath>
#include <iostream>
#include <time.h>
#define PI 3.14

static QImage image = QImage(598, 598, QImage::Format_RGB32);
static QImage image2 = QImage(598, 598, QImage::Format_RGB32);

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    image.fill(qRgb(255,255,255));
    image2.fill(qRgb(255,255,255));
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
    long double X = 0;
    long double Y = 0;
    //===========

    for (int i = 0; i < (R + 1); i++)
    {
        Y = roundl(sqrt(R * R - i * i));
        image.setPixel(xc + i,yc + Y, pen.color().rgb());
        image.setPixel(xc + i, yc - Y, pen.color().rgb());
        image.setPixel(xc - i, yc + Y, pen.color().rgb());
        image.setPixel(xc - i, yc - Y, pen.color().rgb());
    }

    for (int i = 0; i < (R + 1); i++)
    {
        X = roundl(sqrt(R * R - i * i));
        image.setPixel(xc + X,yc + i, pen.color().rgb());
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
    double l = round(PI * R/2); //length of square
    //===========

    for(int i = 0;i < (l + 1); i++)
    {
        X = round(R * cos(i / R));
        Y = round(R * sin(i / R));
        image.setPixel(xc + X,yc + Y, pen.color().rgb());
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
    double D1;
    double D2;
    //===========

    //Algorithm
    while(Y > 0.0)
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

//CIRCLE MIDDLE POINTS
QImage circle_middle_points(QImage image, QPen pen, double xc, double yc, double R)
{
    //Start params
    //===========
    double X = 0;
    double Y = R;
    double p = 5/4 - R; // (x + 1)^2 + (y - 1/2)^2 - r^2
    //===========

    while(true)
    {
        image.setPixel(xc - X,yc + Y, pen.color().rgb());
        image.setPixel(xc + X,yc - Y, pen.color().rgb());
        image.setPixel(xc - X,yc - Y, pen.color().rgb());
        image.setPixel(xc + X,yc + Y, pen.color().rgb());

        image.setPixel(xc - Y,yc + X, pen.color().rgb());
        image.setPixel(xc + Y,yc - X, pen.color().rgb());
        image.setPixel(xc - Y,yc - X, pen.color().rgb());
        image.setPixel(xc + Y,yc + X, pen.color().rgb());

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

        if(X > Y)
            break;

    }

    return image;
}



//ELLIPSE CANONICH
QImage ellipse_canon(QImage image, QPen pen, double xc, double yc, double a, double b)
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
QImage ellipse_param(QImage image, QPen pen, double xc, double yc, double a, double b)
{
    //Start params
    //===========
    double X = 0;
    double Y = b;
    double max = std::max(a, b);
    double l = round(PI * max / 2);
    //===========

    for(int i = 0;i < (l + 1); i++)
    {
        X = a * cos(i / max);
        Y = b * sin(i / max);
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
    int col, row;
    long a_square,b_square,two_a_square,two_b_square,four_a_square,four_b_square,d;
    b_square=b*b;
    a_square=a*a;
    row=b;
    col=0;
    two_a_square=a_square<<1;
    four_a_square=a_square<<2;
    four_b_square=b_square<<2;
    two_b_square=b_square<<1;
    d=two_a_square*((row-1)*(row))+a_square+two_b_square*(1-a_square);
    //===========

    while(a_square*(row)>b_square*(col))
    {
        //1.First pixel
        image.setPixel(xc + col, yc + row, pen.color().rgb());
        image.setPixel(xc + col, yc - row, pen.color().rgb());
        image.setPixel(xc - col, yc + row, pen.color().rgb());
        image.setPixel(xc - col, yc - row, pen.color().rgb());

        if (d>=0)
        {
            row--;
            d-=four_a_square*(row);
        }
            d+=two_b_square*(3+(col<<1));
            col++;
     }
     d=two_b_square*(col+1)*col+two_a_square*(row*(row-2)+1)+(1-two_a_square)*b_square;

     while ((row) + 1)
     {
         image.setPixel(xc + col, yc + row, pen.color().rgb());
         image.setPixel(xc + col, yc - row, pen.color().rgb());
         image.setPixel(xc - col, yc + row, pen.color().rgb());
         image.setPixel(xc - col, yc - row, pen.color().rgb());

         if (d<=0)
         {
            col++;
            d+=four_b_square*col;
         }

         row--;
         d+=two_a_square*(3-(row <<1));
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
        image.setPixel(xc - X,yc - Y, pen.color().rgb());
        image.setPixel(xc + X,yc + Y, pen.color().rgb());

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
        image.setPixel(xc - X,yc - Y, pen.color().rgb());
        image.setPixel(xc + X,yc + Y, pen.color().rgb());

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


//====================================
//
//             MENU
//
//====================================

void MainWindow::on_pushButton_clicked()
{
    QPen pen = QPen();
    double xc, yc, radius, a, b;
    int R,G,B;

    //line color
    if (ui->radioButton_3->isChecked()) // Black
    {
        R = G = B = 0;
    }
    else if (ui->radioButton_4->isChecked()) // White
    {
        R = G = B = 255;
    }
    else if (ui->radioButton_5->isChecked()) // Red
    {
        R = 255;
        G = 0;
        B = 0;
    }

    pen.setColor(qRgb(R, G, B));

    //Check combobox
    if(ui->comboBox->currentIndex() == 0)
    {
        xc = ui->lineEdit->text().toDouble();
        yc = ui->lineEdit_2->text().toDouble();
        xc += 299;
        yc += 299;

        radius = ui->lineEdit_3->text().toDouble();

        image = canon_circle(image, pen, xc, yc, radius);
    }

    else if(ui->comboBox->currentIndex() == 1)
    {
        xc = ui->lineEdit->text().toDouble();
        yc = ui->lineEdit_2->text().toDouble();
        xc += 299;
        yc += 299;

        radius = ui->lineEdit_3->text().toDouble();

        image = circle_param(image, pen, xc, yc, radius);
    }

    else if(ui->comboBox->currentIndex() == 2)
    {
        xc = ui->lineEdit->text().toDouble();
        yc = ui->lineEdit_2->text().toDouble();
        xc += 299;
        yc += 299;

        radius = ui->lineEdit_3->text().toDouble();

        image = brez_circle(image, pen, xc, yc, radius);
    }

    else if(ui->comboBox->currentIndex() == 3)
    {
        xc = ui->lineEdit->text().toDouble();
        yc = ui->lineEdit_2->text().toDouble();
        xc += 299;
        yc += 299;

        radius = ui->lineEdit_3->text().toDouble();

        image = circle_middle_points(image, pen, xc, yc, radius);
    }

    else if(ui->comboBox->currentIndex() == 4)
    {
        xc = ui->lineEdit_4->text().toDouble();
        yc = ui->lineEdit_5->text().toDouble();
        a = ui->lineEdit_9->text().toDouble();
        b = ui->lineEdit_10->text().toDouble();
        xc += 299;
        yc += 299;

        image = ellipse_canon(image, pen, xc, yc, a, b);
    }

    else if(ui->comboBox->currentIndex() == 5)
    {
        xc = ui->lineEdit_4->text().toDouble();
        yc = ui->lineEdit_5->text().toDouble();
        a = ui->lineEdit_9->text().toDouble();
        b = ui->lineEdit_10->text().toDouble();
        xc += 299;
        yc += 299;

        image = ellipse_param(image, pen, xc, yc, a, b);
    }

    else if(ui->comboBox->currentIndex() == 6)
    {
        xc = ui->lineEdit_4->text().toDouble();
        yc = ui->lineEdit_5->text().toDouble();
        a = ui->lineEdit_9->text().toDouble();
        b = ui->lineEdit_10->text().toDouble();
        xc += 299;
        yc += 299;

        image = brez_ellipse(image, pen, xc, yc, a, b);
    }

    else if(ui->comboBox->currentIndex() == 7)
    {
        xc = ui->lineEdit_4->text().toDouble();
        yc = ui->lineEdit_5->text().toDouble();
        a = ui->lineEdit_9->text().toDouble();
        b = ui->lineEdit_10->text().toDouble();
        xc += 299;
        yc += 299;

        image = ellipse_middle(image, pen, xc, yc, a, b);
    }



    QGraphicsScene *graphic = new QGraphicsScene(this);
    graphic->addPixmap(QPixmap::fromImage(image));
    ui->graphicsView->setScene(graphic);
}

void MainWindow::on_pushButton_2_clicked()
{
    image.fill(qRgb(255,255,255));
    image2.fill(qRgb(255,255,255));

    QGraphicsScene *graphic = new QGraphicsScene(this);
    graphic->addPixmap(QPixmap::fromImage(image));
    ui->graphicsView->setScene(graphic);


}

void MainWindow::on_pushButton_3_clicked()
{
    QPen pen = QPen();
    double radius, a, b;
    int R,G,B;
    int num,step;

    //line color
    if (ui->radioButton_3->isChecked()) // Black
    {
        R = G = B = 0;
    }
    else if (ui->radioButton_4->isChecked()) // White
    {
        R = G = B = 255;
    }
    else if (ui->radioButton_5->isChecked()) // Red
    {
        R = 255;
        G = 0;
        B = 0;
    }

    pen.setColor(qRgb(R, G, B));


    //Check combobox
    if(ui->comboBox->currentIndex() == 0)
    {
        step = ui->lineEdit_6->text().toDouble();
        num = ui->lineEdit_7->text().toDouble();

        radius = ui->lineEdit_3->text().toDouble();

        for(int i = 0; i < num; i++)
        {
            image2 = canon_circle(image2, pen, 299, 299, radius);
            radius += step;
        }
    }

    else if(ui->comboBox->currentIndex() == 1)
    {
        step = ui->lineEdit_6->text().toDouble();
        num = ui->lineEdit_7->text().toDouble();

        radius = ui->lineEdit_3->text().toDouble();

        for(int i = 0; i < num; i++)
        {
            image2 = circle_param(image2, pen, 299, 299, radius);
            radius += step;
        }
    }

    else if(ui->comboBox->currentIndex() == 2)
    {
        step = ui->lineEdit_6->text().toDouble();
        num = ui->lineEdit_7->text().toDouble();

        radius = ui->lineEdit_3->text().toDouble();

        for(int i = 0; i < num; i++)
        {
            image2 = brez_circle(image2, pen, 299, 299, radius);
            radius += step;
        }
    }

    else if(ui->comboBox->currentIndex() == 3)
    {
        step = ui->lineEdit_6->text().toDouble();
        num = ui->lineEdit_7->text().toDouble();

        radius = ui->lineEdit_3->text().toDouble();

        for(int i = 0; i < num; i++)
        {
            image2 = circle_middle_points(image2, pen, 299, 299, radius);
            radius += step;
        };
    }

    else if(ui->comboBox->currentIndex() == 4)
    {
        step = ui->lineEdit_6->text().toDouble();
        num = ui->lineEdit_7->text().toDouble();
        a = ui->lineEdit_9->text().toDouble();
        b = ui->lineEdit_10->text().toDouble();

        for(int i = 0; i < num; i++)
        {
            image2 = ellipse_canon(image2, pen, 299, 299, a, b);
            a += step;
            b += step;
        }
    }

    else if(ui->comboBox->currentIndex() == 5)
    {
        step = ui->lineEdit_6->text().toDouble();
        num = ui->lineEdit_7->text().toDouble();
        a = ui->lineEdit_9->text().toDouble();
        b = ui->lineEdit_10->text().toDouble();

        for(int i = 0; i < num; i++)
        {
            image2 = ellipse_param(image2, pen, 299, 299, a, b);
            a += step;
            b += step;
        }
    }

    else if(ui->comboBox->currentIndex() == 6)
    {
        step = ui->lineEdit_6->text().toDouble();
        num = ui->lineEdit_7->text().toDouble();
        a = ui->lineEdit_9->text().toDouble();
        b = ui->lineEdit_10->text().toDouble();

        for(int i = 0; i < num; i++)
        {
            image2 = brez_ellipse(image2, pen, 299, 299, a, b);
            a += step;
            b += step;
        }
    }

    else if(ui->comboBox->currentIndex() == 7)
    {
        step = ui->lineEdit_6->text().toDouble();
        num = ui->lineEdit_7->text().toDouble();
        a = ui->lineEdit_9->text().toDouble();
        b = ui->lineEdit_10->text().toDouble();

        for(int i = 0; i < num; i++)
        {
            image2 = ellipse_middle(image2, pen, 299, 299, a, b);
            a += step;
            b += step;
        }
    }



    QGraphicsScene *graphic = new QGraphicsScene(this);
    graphic->addPixmap(QPixmap::fromImage(image2));
    ui->graphicsView->setScene(graphic);
}
