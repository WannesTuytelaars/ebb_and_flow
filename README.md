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
required concentration P mg/L
required concentration K mg/L
required concentration Ca mg/L
required concentration Mg mg/L
required concentration S mg/L
required concentration Fe mg/L
required concentration Mn mg/L
required concentration Cu mg/L
required concentration Zn mg/L
required concentration B mg/L
required concentration Mo mg/L
length cultivating bench in m
width cultivating bench in m
water height in mm

So in fact, the input file are just 15 values. The code for the function 'required' is in the Python file 'required_nutrients.py'. The output of this function is a list of length 13 with the required nutrient concentrations (in mg/L) and the required water volume (in L).

The second function is named 'measure' and it's coded in the file 'measure_concentrations.py'. The goal of this function is the measure the nutrient concentrations and water volume after every drainage of the cultivating bench. It also prints an alarm statement when there is a big loss of water, signaling a leak. This function requires an input file with the measured concentrations. The concentrations are measured by sensors in the reservoir. I assumed these sensors make an input file 'measured_concentrations.txt'. If the sensors don't make this file, the program will estimate the nutrient concentrations by using the triangular distribution. The output of this function is a list with the same dimensions as the output of the 'required' function, but with smaller values since some nutrients will have been taken up by the plants.

When the program has the required and the measured concentrations, it calculates the masses (in mg) of nutrients and the volume of water (in L) that should be added to the reservoir. This is done by the function 'balance_nut' coded in the file 'balance_nut.c'. These values should be given to nutrient dispensing devices so that they can make the nutrient solution optimal again. These dispensing devices are not included in the code, but you can imagine that they can dispense the exact mass of nutrient calculated by 'balance_nut'.
