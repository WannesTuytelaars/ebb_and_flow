from required_nutrients import required #import all the functions we've written and use them 
from measure_concentrations import measure
from C_TO_PYTHON import py_c_balance

req = required('data_lettuce.txt') #use another file if you are cultivating another plant species
req_tomato = required('data_tomato.txt') #lettuce and tomato are used to show the output in the report
meas = measure(req,'measured_concentrations.txt')
masses_add = [0.0]*13
masses_add = list(py_c_balance(meas,req,masses_add))
print('These masses have to be added in mg, the last value is the volume of water that should be added in L. '+ str(masses_add)) #you can only concatenate str to str
#these values change everytime you run the code because every time you run the code, you initiate a new ebb and flow cycle
#and the nutrient uptake differs from cycle to cycle
#the strength of this program is that it can always go back to the required nutrient solution, no matter how much nutrients are gone
#it is assumed that masses_add is given as input to the nutrient dispensers to bring the nutrient solution back to optimal