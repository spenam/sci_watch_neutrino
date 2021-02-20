using DelimitedFiles;

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
qe[:,2]=qe[:,2]*0.01
wabs = readdlm("../water_abs_interp.txt",skipstart=1); # absorption length data
wscatt = readdlm("../water_scatt_rayleight.txt",skipstart=1); # scattering length data
b=0.835 # parameter b of the scattering
lam = 550; #Wavelength (nm)
xa = wabs[searchsortednearest(wabs[1:end,1],lam),2]; # absorption length
xs = wscatt[searchsortednearest(wscatt[1:end,1],lam),2]; # scattering length
Pq = qe[searchsortednearest(qe[1:end,1],lam),2]; # quantum efficiency
f=(1. /(4. *pi))*(3. /(3. +b))
human = 1; # Human eye conversion factor
lum = 1; # Brightness (lm)
dist = 486; # Distance

#one Lumen at 555 nm = 4,11·10^15 Photons per second  
Aeff3inch = 0.004536; # Effective area 3inch PMT [m^2]
ratdef = 4.11e15; #photon rate 1 lumen

ctmin = -1.;
ctmax = cos(pi/6);#0;
Nbct = 1000;
delct=(ctmax-ctmin)/Nbct;

ndist = 500; # steps over 500m
nmet  = 1; # step width (m)
rate = 0;
part = 0;

ratesum = 0; # sum of individual rates
#loop over distance bins
ndist = 500 # steps over 500m
nmet = 1 #step width
pmtsteps=100
sector=0.
pmtcosb=zeros(pmtsteps)
for ii =1:pmtsteps
    pmtcosb[ii] = cos((ii/pmtsteps+sector)*pi/6.) # PMT rotation angle
end
for jj =1:pmtsteps
    rate = 0;
    for j = 0:ndist-1
        xm = (j+0.05)*nmet; # mean distance of bin
        Psca = nmet/xs*exp(-xm/xs); # probability of scattering inside the bin
        for l=0:Nbct-1
            ct = ctmin + (l+0.5)*delct;
            y=sqrt(dist*dist+xm*xm-2. *dist*xm*ct); # distance from scattering to PMT
            Pabs = exp(-(y+xm)/xa); # probability of non-absorption on full photon path
            cosa = (-dist*dist + xm*xm + y*y)/(2. *xm*y); # scattering angle
            cosb = (-xm*xm + y*y + dist*dist)/(2. *y*dist); # PMT-photon angle
            pmtcos = pmtcosb[jj] # PMT rotation angle
            domcos = cosb*pmtcos+sqrt(1-cosb^2.)*sqrt(1-pmtcos^2.) # angle sum of rotation and arrival
            # included sanity check in angles
            if (abs((acos(ct)+acos(cosa)+acos(cosb))/pi-1)>1e-6) 
                println(ct, " ", cosa, " ", cosb)
            end
            PSAng = f*(1. +b*(cosa)^2.) # probability for angular scattering
            PxAng = ang[searchsortednearest(ang[1:end,1],cosb),2] # probability for photon on PMT
            rate += ratdef * human * lum * Aeff3inch/y/y * Pabs * Psca * PSAng * PxAng * Pq / Nbct;
        end
    end
    println(jj)
    ratesum += rate
end

println("Rate ", ratesum/pmtsteps, "Hz")        

