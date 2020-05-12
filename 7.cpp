#include <iostream>
#include <cmath>
#include <fstream>
#include <valarray>

using namespace std;

double eps = 0.01;

valarray<double> rightpart(double x, double y1, double y2) {
    valarray<double> right;
    right.resize(2);
    right[0] = y2;
    right[1] = -2 * y2 - 5 / 2 * y1 + x / 2 * exp(-x);
    return right;
}
int main()
{   
    setlocale(LC_ALL, "Russian");
    double a = 0.0, b = 2.0;
    double y1 = 1.0, y2 = 0.0;
    double h = 0.001;
    double q = 1.0;
    valarray<valarray<double>>matrix;
    matrix.resize(5, valarray<double>(5));
    int step = fabs(a-b) / h;
    while (q >= eps) {
        valarray<valarray<double>>back(matrix);
        matrix.resize(step, valarray<double>(2));
        
        matrix[0][0] = y1;
        matrix[0][1] = y2;
    
        double x = a;

        for (int i = 1; i < step; i++) {
            x = x + h;
            matrix[i]=(matrix[i - 1] + rightpart(x,matrix[i - 1][0], matrix[i - 1][1])*h);
            
        }
       
        valarray<valarray<double>>equa;
        equa.resize(int(step / 2),valarray<double>(2));
        int i = 0;
        while ((i) < (int(step / 2))-1) {
            i++;
            equa[i][0] = matrix[2 * i][0];
            equa[i][1] = matrix[2 * i][1];
            
           
            double eq = 0;
            for (int i = 0; i < int(step/2); i++)
            {
                double St = 0;
                for (int j = 0; j < 2;j++)
                    St += fabs(equa[i][j]);
                if (eq < St)
                    St = eq;
            }
            
            double bac = 0;
            for (int i = 0; i < back.size(); i++)
            {
                double St = 0;
                for (int j = 0; j < back[0].size(); j++)
                    St += fabs(back[i][j]);
                if (bac < St)
                    St = bac;
            }
           
            q = fabs(eq - bac) / eq;
            
        }
        h = h / 2;
    }
    valarray<double>xnew;
    xnew.resize(step);
    valarray<double>ynew;
    ynew.resize(step);
    valarray<double>x;
    x.resize(step);
   
    for (int i = 0; i < step; i++) {

        x[i] = x[i - 1] +  2*h;
        xnew[i]=matrix[i][0];
        ynew[i] = matrix[i][1];
 
    }
    cout << "Chislo tochek na grafike: " << step << endl;
    cout << "Solution: " << xnew[1]<< endl;
    cout << "Proizvodnaya: " << ynew[1] << endl;
    
    ofstream one,two,three;
    one.open("x.txt");
    for (int i = 0; i < step; i++) {
        
        one << xnew[i] << " " << ynew[i] << endl;

    }
   
    one.close();
    system("python 7.py");
    return 0;
}
