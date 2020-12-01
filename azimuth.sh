for i in 100 150 200 250 300 350
do
	echo Doing integral for distance=$i m
	python test_azimuth.py --distance $i
done
python plots_azimuth.py
