#ifndef HORSE_3_H
#define HORSE_3_H

#include <iostream>
#include <fstream>

double horse_3(int n, int x, int y);

double horse_3(int n, int x, int y)
{
    std::ofstream nfile;
    nfile.open("horse_3.txt");
    nfile << n << x << y;
    nfile.close();
    return 3.3;
}

#endif