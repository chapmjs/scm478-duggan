import numpy as np
import pandas as pd


# define the function. For teh numerical solution, the function runs the
# entire simulation

def sim_advertising_impact_euler(init, time, DT, loss_fraction):
    sim_out = np.zeros(len(time))
    sim_out[0] = init
    print(sim_out)
    for i in range(1,len(time)):
        net_flow = -sim_out[i-1]*loss_fraction
        sim_out[i] = sim_out[i-1] + net_flow*DT
        print("index",i,"time",time[i],"sim_out",sim_out[i])
    
    return sim_out



DT = 0.25
time = np.arange(0,25,DT)
print(time)
sim_advertising_impact_euler(100,time,DT,0.1)
