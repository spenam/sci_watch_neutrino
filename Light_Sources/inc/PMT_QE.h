#ifndef PMT_QE_H_
#define PMT_QE_H_

#include<iostream>
#include<fstream>

#include "TFile.h"
#include "TGraph.h"

using namespace std;

class PMT_QE
 {
 public:
 
 PMT_QE(string);
 double Get(double);
 
 private:
 TGraph* grQE;
 
 };

#endif
