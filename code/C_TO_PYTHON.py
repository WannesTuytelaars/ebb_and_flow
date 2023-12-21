from ctypes import c_double, CDLL
import sys

lib_path = f'./balance_{sys.platform}.so'
c_lib = CDLL(lib_path)
c_balance = c_lib.balance_nut
c_balance.restype = None # return type is 'void'

def py_c_balance(measured,required,masses_add): #the purpose of this whole document is so we can use the function balance_nut written in C in our Main python script
    meas = c_double * 13
    meas_array = meas(*measured)
    req_array = meas(*required)
    masses_array = meas(*masses_add)
    c_balance(meas_array,req_array,masses_array)
    return masses_array

#source: https://stakahama.gitlab.io/sie-eng270/C_intro.html