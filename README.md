# transmission-analysis

This code is used for getting the doable data from ESKM's ouput

ESKM is C++ codes that use lattice dynamics and the elastic scattering kernel method to calcualte phonon tranmisssion. 

firstly, we need to grep some data from output file: transmission_part_0.dat

- grep T12 transmission_part_0 | awk '{print $2, $4}' > total-trans.dat

- grep "Reservoir 0 new outgoing channel" transmission_part_0 | awk '{print $1 " " $10 " " $11 " " $12}' > channel.dat

- awk '{if ($1~/r_0/ && $2=="|") print $1 " " $3 " " $7}' transmission_part_0  > trans.dat

then we use python codes to clean data and prepare data for next step's analysis 
