import math
import numpy as np
import matplotlib.pyplot as plt
import sys


# RUN: python /Users/MariaGabriela/cellmodeller/Scripts/plot_magdvelocity_distcentro_time.py /Users/MariaGabriela/cellmodeller/data/ex1_simpleGrowth-17-03-27-21-20/
#python .py output-velocity




#Path file 
path = sys.argv[1]



# Read file col  
def plot_dmx_velocity(file, Ra, time, path):
    
    file1  = open(file, 'r')
    lines = file1.readlines()


    # Get Vectors
    dc = []
    mdv = []

    
    for line in lines:
        #if line[0] != 'T':
        if line[0]==time[0] and line[1]==time[1] and line[2]== time[2]:
        
                
            line = line.split()
    
            pos = [float(line[2]), float(line[3]), float(line[4])]
            pos = np.asarray(pos)
            distc = np.linalg.norm(pos)
            
            dc.append(distc)
            
            v = [float(line[5]), float(line[6]), float(line[7])]
            v = np.asarray(v)
            
            v1 = [float(line[9]), float(line[10]), float(line[11])]
            v1 = np.asarray(v1)
    
            u = v - v1 
        
            d = np.linalg.norm(u)
        
            mdv.append(d)
    
    #print dc 
    #print mdv
            
    
    #Plot
    a = max(dc)
    db = a - dc

    
    fig = plt.figure()
    plt.plot(db,mdv, 'c.', markersize=1)
    
    plt.xlabel('Distance to border')
    plt.ylabel('Magnitude diference Velocity')
    plt.title('Mag Diff Vel vs Distance to border;  Time: %s  Radius: %s' %(time, Ra))
    plt.yscale('log')
    #plt.axis([0, 100, 0, 0.25])
    #plt.show()
    Ra2 = str(Ra)
    Ra2 = Ra2[0]+Ra2[2]
    t = time[:3].replace(' ', '')
    plt.savefig('%sMDV_DistCentre/MDVd_R_%s_t_%s_log.png' %(path,Ra2,t))
    plt.close()


for i in range (1,25):
    
    time = str(i*20)
    time = time+'   '
    print time
    
    c = 0.5
    
    while c <= 5 :
        
        Ra = round(c, 1)
        file_velocity = '%sVelocity_%s.csv' %(path,Ra)
        plot_dmx_velocity(file_velocity,Ra,time,path)
        c = c+0.5
    
    
    
    
    