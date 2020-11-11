for i in 350 400 450 500 550 600
do
	echo Doing integral for lambda=$i nm
	python setups3.py --wavelength $i
done
