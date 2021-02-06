BASE_DIR  = `pwd`
ROOTLIBS  = `${ROOTSYS}/bin/root-config --libs`
ROOTINCL  = `${ROOTSYS}/bin/root-config --cflags`
OPT = -fPIC -O2
INC_PMT = ${BASE_DIR}/inc

default: libPMT.so

all: libPMT.so
PMT_QE.o : PMT_QE.cc
	g++ ${OPT} -c -o $@ ${ROOTINCL} -I${INC_PMT} $<

PMT_Ang.o : PMT_Ang.cc
	g++ ${OPT} -c -o $@ ${ROOTINCL} -I${INC_PMT} $<

W_Abs.o : W_Abs.cc
	g++ ${OPT} -c -o $@ ${ROOTINCL} -I${INC_PMT} $<

W_Sca.o : W_Sca.cc
	g++ ${OPT} -c -o $@ ${ROOTINCL} -I${INC_PMT} $<

Rate_head.o : Rate_head.cc
	g++ ${OPT} -c -o $@ ${ROOTINCL} -I${INC_PMT} $<

Rate_head : Rate_head.o
	g++ -o $@ libPMT.so ${ROOTLIBS} $<

Rate.o : Rate.cc
	g++ ${OPT} -c -o $@ ${ROOTINCL} -I${INC_PMT} $<

Rate : Rate.o
	g++ -o $@ libPMT.so ${ROOTLIBS} $<

Rate_back.o : Rate_back.cc
	g++ ${OPT} -c -o $@ ${ROOTINCL} -I${INC_PMT} $<


Rate_back : Rate_back.o
	g++ -o $@ libPMT.so ${ROOTLIBS} $<

libPMT.so : PMT_QE.o PMT_Ang.o W_Abs.o W_Sca.o
	g++ -shared -o $@ $^


clean: 
	rm *.o

#======================================================================
