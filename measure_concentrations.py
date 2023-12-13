import random
import numpy as np
def measure(required_concentrations, filename):
    sensor_data = np.genfromtxt(filename,delimiter=' ',dtype=None)
    if len(sensor_data)<13:
        print("The sensors don't give useful information, we will estimate the nutrient concentrations using the triangular distribution.")
        measured = [0]*13 #initialise
        for i in range(0,12): #there are 12 nutrients
            required = required_concentrations[i]
            low = required*0.75
            mode = required * 0.9
            measured[i] = random.triangular(low=low,high=required,mode=mode)
        volume_end = required_concentrations[12]
        low = volume_end * 0.7
        mode = volume_end * 0.9
        measured[12] = random.triangular(low=low,high=volume_end,mode=mode)
    else:
        print("The sensors gave information: the concentrations measured are accurate.")
        measured = sensor_data
    if measured[12]<volume_end * 0.7: #this means almost all water that went to the plants didn't come back
        print("ALARM: there may be a leak in the system, water levels are very low!") 
    return measured