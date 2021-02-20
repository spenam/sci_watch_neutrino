#ifndef W_Abs_H_
#define W_Abs_H_

#include<iostream>
#include<fstream>

#include "TFile.h"
#include "TGraph.h"

using namespace std;

class W_Abs
 {
 public:
 
 W_Abs(string);
 double Get(double);
 
 private:
 TGraph* grAbs;
 
 };

#endif
