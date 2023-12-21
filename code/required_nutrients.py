import numpy as np
from tabulate import tabulate
def required(filename):
    data = np.genfromtxt(filename,delimiter=' ',dtype=None)
    requ = [0.0]*13 #initialize
    for i in range(0,12):
        requ[i] = data[i]
    length_bench = data[12] #in m
    width_bench = data[13] # in m
    water_height = data[14] # in mm
    requ[12] = length_bench * width_bench * water_height * 3 #times 3 to leave some volume in the reservoir, arbitrarily chosen
    col_names = ["Nutrient","Required concentration (mg/L)"]
    data= [["N",requ[0]],
           ["P",requ[1]],
           ["K",requ[2]],
           ["Ca",requ[3]],
           ["Mg",requ[4]],
           ["S",requ[5]],
           ["Fe",requ[6]],
           ["Mn",requ[7]],
           ["Cu",requ[8]],
           ["Zn",requ[9]],
           ["B",requ[10]],
           ["Mo",requ[11]],
            ["Water (L)",requ[12]]] #water is not measured in mg/L but in L
    print(tabulate(data,col_names,tablefmt="fancy_grid"))
    return requ
req = [0.0]*13
req = required('data_lettuce.txt')
print(req)

#source: https://towardsdatascience.com/how-to-easily-create-tables-in-python-2eaea447d8fd



