from required_nutrients import required
from measure_concentrations import measure
from C_TO_PYTHON import py_c_balance
import matplotlib.pyplot as plt
import numpy as np

req = [0.0]*13
req = required('data_lettuce.txt')
req_tomato = required('data_tomato.txt')
Ca_meas = [0]*17
N_meas = [0]*17
N_added = [0]*17
time = np.arange(1,18,1)
for e in range(0,17): #laten we zeggen da het water elk uur ververst wordt en de plant heeft 16 lichturen nodig, dees is dus het verloop van 1 dag (zonder nacht)
    meas = [0.0]*13
    meas = measure(req,'measured_concentrations.txt')
    masses_add = [0.0]*13
    masses = [0.0]*13
    masses = list(py_c_balance(meas,req,masses_add)) #convert to list so we can use it in python, otherwise it's a c_double
    Ca_meas[e] = meas[3]
    N_meas[e] = meas[0]
    N_added[e] = masses[0]
#plt.plot(time,Ca_meas,label="Ca-concentration")
#plt.plot(time,N_meas,label="N-concentration")
plt.plot(time,N_added)
plt.title("Evolution of Ca and N  concentrations")
plt.xlabel("Time [h]")
plt.ylabel("Concentration [mg/L]")
#plt.legend(loc="best")
plt.show()

