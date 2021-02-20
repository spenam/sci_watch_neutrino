for i in 100 150 200 250 300 350
do
	echo Doing integral for distance=$i m
	python setups1.py --distance $i
done
python plots_1.py
