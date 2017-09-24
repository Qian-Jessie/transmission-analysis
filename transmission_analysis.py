# this code is used for getting the doable data from ESKM's ouput
# grep the needed data first
"""
    grep T12 transmission_part_0 | awk '{print $2, $4}' > total-trans.dat
    
    grep "Reservoir 0 new outgoing channel" transmission_part_0 | awk '{print $1 " " $10 " " $11 " " $12}' > channel.dat
    
    awk '{if ($1~/r_0/ && $2=="|") print $1 " " $3 " " $7}' transmission_part_0  > trans.dat
    """

import numpy as np

fx = open('xtrans.dat','w')
fy = open('ytrans.dat','w')
fz = open('ztrans.dat','w')

# compare x, y, z values and define the polarization of channels with the biggest value.
# replace channel's name with x, y or z.
def identify():
    f = open('channel.dat')
    data1 = []
    for line in f:
        line = line.split()
        x = float(line[1])
        y = float(line[2])
        z = float(line[3])
        amp = np.array([x, y, z])
        data1.append([line[0], amp.argmax()])
        #print line[0], amp.argmax()
    return data1


f11 = 'trans.dat'

# find the same channel and put the energy and transmisison together
def newtrans(f11):
  data = []
  f1 = open(f11,'r')
  f11 = f1.readlines()
  f1.close()
  for line3 in identify():
      #print line3[0],line3[1]
      for line1 in f1l:
          line1 = line1.split()
          if line3[0] == line1[0]:
              #return(line3[1], line1[1],line1[2])
              data.append([line3[1],line1[1],line1[2]])
  return data


f2 = open('freq.dat','r')

#sum transmission at the same energy and the same chanel for each polarization 
for line2 in f2:
    #line2 = line2.split()
    x_direction = 0.0
    y_direction = 0.0
    z_direction = 0.0
   
    for line1 in newtrans(f11):
       
        if int(line1[0]) == 0 and abs(float(line1[1]) - float(line2)) < 1e-8:
           x_direction += float(line1[2])
           #print x_direction
       
        if int(line1[0]) == 1 and abs(float(line1[1]) - float(line2)) < 1e-8:
            y_direction += float(line1[2])

        if int(line1[0]) == 2 and abs(float(line1[1]) - float(line2)) < 1e-8:
           z_direction += float(line1[2])
               
    fx.write("%.10f %.12f\n" % (float(line2), x_direction))
    fy.write("%.10f %.12f\n" % (float(line2), y_direction))
    fz.write("%.10f %.12f\n" % (float(line2), z_direction))








