using DelimitedFiles

function searchsortednearest(a,x)
   idx = searchsortedfirst(a,x)
   if (idx==1); return idx; end
   if (idx>length(a)); return length(a); end
   if (a[idx]==x); return idx; end
   if (abs(a[idx]-x) < abs(a[idx-1]-x))
      return idx
   else
      return idx-1
   end
end

ang = readdlm("../pmt_ang_interp.txt",skipstart=1); # angular acceptance data
qe = readdlm("../pmt_qe_interp.txt",skipstart=1); # quantum efficiency data
qe[:,2]=qe[:,2]*0.01;
wabs = readdlm("../water_abs_interp.txt",skipstart=1); # absorption length data
wscatt = readdlm("../water_scatt_rayleight.txt",skipstart=1); # scattering length data

function main(ang,qe,wabs,wscatt)

b=Float64(0.835); # parameter b of the scattering
lam = Float64(446); #Wavelength (nm)
xa = wabs[searchsortednearest(wabs[1:end,1],lam),2]; # absorption length
xs = wscatt[searchsortednearest(wscatt[1:end,1],lam),2]; # scattering length
Pq = qe[searchsortednearest(qe[1:end,1],lam),2]; # quantum efficiency
f=Float64((1. /(4. *pi))*(3. /(3. +b)))
human = Float64(1); # Human eye conversion factor
lum = Float64(1); # Brightness (lm)
dist = Float64(400); # Distance

Aeff3inch = Float64(0.004536); # Effective area 3inch PMT [m^2]
ratdef = Float64(4.11e15); #photon rate 1 lumen
#ratdef = 8e17; # photon rate for the ROV
#ratdef = 9*10^18; # photon rate for the ROV

ctmin = Float64(-1.);
ctmax = Float64(-cos(pi/6));#0;
Nbct = Int32(100);
delct=Float64((ctmax-ctmin)/Nbct);

#light source azimuth
Nazim = Int32(100);
AzimStep =Float64(2.0 *pi/Float32(Nazim));
circ = Float64(2.0 *pi);

ndist = Float64(1000); # steps over 500m
nmet  = Float64(5); # step width (m)
rate = Float64(0);

ratesum = Float64(0); # sum of individual rates 
#loop over distance bins
ndist = Float64(1000); # steps over 500m
nmet = Float64(5); #step width
pmtsteps=Int32(1);#100 #number of steps to average the value
sector=[0.,1.,2.,3.,4.,5.] # what part of the hemisphere you are looking
AngPMTStep = Float64(pi/(pmtsteps*1.0));
for kk = 1:6
	ratesum = 0; # sum of individual rates 
	for ii =1:pmtsteps
	#angPMT = (sector[kk]+ii/pmtsteps)*pi/6;
	angPMT = (sector[kk]+0.5)*pi/6;
	azimPMT = 0.5;
	angPMTDeg = angPMT*180.0/pi;

	xPMT = cos(azimPMT)*sin(angPMT);
	yPMT = sin(azimPMT)*sin(angPMT);
	zPMT = cos(angPMT);
		rate = 0;
		#loop over light source azimuth
		for m = 0:Nazim-1
			azim=(m+0.5)/AzimStep;
		for j = 0:ndist-1
			xm = (j+0.05)*nmet; # mean distance of bin
			#Here
			Psca = nmet/xs*exp(-xm/xs); # probability of scattering inside the bin
		for l=0:Nbct-1
			ct= ctmin + (l+0.5)*delct;
			y=sqrt(dist*dist+xm*xm-2. *dist*xm*ct); # distance from scattering to PMT
			#Here
			Pabs = exp(-(y+xm)/xa); # probability of non-absorption on full photon path
			cosa = (-dist*dist + xm*xm + y*y)/(2. *xm*y); # scattering angle
			cosb = (-xm*xm + y*y + dist*dist)/(2. *y*dist); # PMT-photon angle
			sinb = sqrt(1.0 -cosb*cosb);
			ihx = dist*sinb/cosb
			xphot = sqrt(1.0-cosb*cosb)*cos(azim);
			yphot = sqrt(1.0-cosb*cosb)*sin(azim);
			zphot = cosb;
			cosx = xPMT*xphot+yPMT*yphot+zPMT*zphot;
			# included sanity check in angles
			if (abs((acos(ct)+acos(cosa)+acos(cosb))/pi-1)>1e-6) 
			println(ct, " ", cosa, " ", cosb)
			end
			PSAng = f*(1. +b*(cosa)^2.) # probability for angular scattering
			#a = @allocated begin
			#Here
			PxAng = ang[searchsortednearest(@view(ang[1:end,1]),cosx),2] # probability for photon on PMT
			#end; a > 0 && println(a) # prints a if the blocks allocates
			rate += ratdef * human * lum * Aeff3inch/y/y * Pabs * Psca * PSAng * PxAng * Pq / Nbct / Nazim;
			#part += 0;
			end
			end
		end
		#println(rate,"\t",pmtcosb[jj])
		ratesum += rate
	end
	println("For the sector= ", sector[kk], ", Rate ", ratesum/pmtsteps, "Hz")  
	ratesum = 0
end
end
@time main(ang,qe,wabs,wscatt)
@time main(ang,qe,wabs,wscatt)
