import numpy as np
import pandas as pd

# This function needs: the initial value, the current time, and the decay rate,
def sim_advertising_impact(init_value, time,loss_fraction):
    return init_value*np.exp(-loss_fraction*time)

# Create a time vector. The number of elements for this model is arbitrary.
time=np.arange(25)

# Create the simulation output array
sim=np.zeros(25)
# print("Time",time)
# print("Sim",sim)

# Set the initial condition for advertising impact = 100 (Percent)
init = 100

# Set the decay rate of 10% per time unit
lf = .1

# Run the model.
for i,t in enumerate(time):
    sim[i] = sim_advertising_impact(init,t,lf)

# print("Sim",sim)

# Plot the results
s = pd.Series(sim, index=time);
s.plot(style="ko--",title="Advertising Impact",grid=True);
