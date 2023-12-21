# ebb_and_flow
project for ENG-270: computational methods and tools

This program will regulate an ebb and flow system. It will calculate how much nutrients should be added to optimize the nutrient solution.

Project structure
-
1) "data/" contains input data
   The 2 documents with input data are: data_lettuce.txt and data_tomato.txt
   Also the document measured_concentrations.txt is in this folder.
2) "code/" contains program code
    It contains the following documents:
     - required_nutrients.py
     - measure_concentrations.py
     - balance_nut.c
     - C_TO_PYTHON.py
     - MAIN.py
  
How the program works
-
First the file with input data is read by the funtion 'required'. Python makes a table with an overview of all the nutrients that need to be added to the nutrient solution. These input files should all only include numbers and should be in this exact form:

required concentration N in mg/L   
required concentration P in mg/L   
required concentration K in mg/L   
required concentration Ca in mg/L   
required concentration Mg in mg/L    
required concentration S in mg/L   
required concentration Fe in mg/L   
required concentration Mn in mg/L   
required concentration Cu in mg/L   
required concentration Zn in mg/L   
required concentration B in mg/L   
required concentration Mo in mg/L   
length cultivating bench in m  
width cultivating bench in m  
water height in mm  

So in fact, the input file are just 15 values. Rhe files data_lettuce.txt and data_tomato.txt are realistic examples of input files. The code for the function 'required' is in the Python file 'required_nutrients.py'. The output of this function is a list of length 13 with the required nutrient concentrations (in mg/L) and the required water volume (in L). Data_lettuce.txt and data_tomato.txt are examples of input files with realistic values.

The second function is named 'measure' and it's coded in the file 'measure_concentrations.py'. The goal of this function is the measure the nutrient concentrations and water volume after every drainage of the cultivating bench. It also prints an alarm statement when there is a big loss of water, signaling a leak. This function requires an input file with the measured concentrations. The concentrations are measured by sensors in the reservoir. I assumed these sensors make an input file 'measured_concentrations.txt'. If the sensors don't make this file, the program will estimate the nutrient concentrations by using the triangular distribution. The output of this function is a list with the same dimensions as the output of the 'required' function, but with smaller values since some nutrients will have been taken up by the plants.

When the program has the required and the measured concentrations, it calculates the masses (in mg) of nutrients and the volume of water (in L) that should be added to the reservoir. This is done by the function 'balance_nut' coded in the file 'balance_nut.c'. These values should be given to nutrient dispensing devices so that they can make the nutrient solution optimal again. These dispensing devices are not included in the code, but you can imagine that they can dispense the exact mass of nutrient calculated by 'balance_nut'.

The function 'balance_nut' is written in C, but the rest of the program is in Python. The C program is compiled to a shared library, which is called by Python in the file 'C_TO_PYTHON' by using the ctypes module. The equivalent Python function is named 'py_c_balance'.

You can find more information about the significance and the result of this program in the seperate report.

How to use the program
-
Version 13.2.0 of gcc was used  
version 3.11.5 of python was used

You should compile the program 'balance_nut' in your gcc compiler with the following command:  
$gcc -o balance_win.so -shared -fPIC -O2 balance_nut.c
This will only work on a windows computer, on other computers the command line is different.  
After you did this, you can run the python file 'C_TO_PYTHON.py'. When you now open a new terminal, you should be able to run 'MAIN.py'.  
For different plant species you can make new data files yourself. 

If there are any problems while using this program, please contact me at: wannes.tuytelaars@epfl.ch
