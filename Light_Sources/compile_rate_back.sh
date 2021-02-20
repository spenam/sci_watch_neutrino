g++ -fPIC -O2 -c -o Rate_back.o `/astro/group/root_versions/SL7_v5.34.23/bin/root-config --cflags` -I`pwd`/inc Rate_back.cc
g++ -o Rate_back libPMT.so `/astro/group/root_versions/SL7_v5.34.23/bin/root-config --libs` -I`pwd` Rate_back.o
