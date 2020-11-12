for i in 350 400 450 500 525 550 600
do
	echo Doing integral for lambda=$i nm
	python setups2.py --wavelength $i
done
