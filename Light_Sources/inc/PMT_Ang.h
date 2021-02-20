#ifndef PMT_Ang_H_
#define PMT_Ang_H_

#include<iostream>
#include<fstream>

#include "TFile.h"
#include "TGraph.h"

using namespace std;

class PMT_Ang
 {
 public:
 
 PMT_Ang();
 double Get(double);
 
 private:
 TGraph* grAng;
 
 };

#endif
