import ctypes
import time

#from timeit import default_timer as timer
from ctypes import *
import random
import sys




#This function will convert the python list to c_type array.

def convert_pythonlist_to_c_array(lst):

        type_int_array=c_int*len(lst)
        array_int=type_int_array
        j=0
        for l in lst:
                array_int[int(j)]=int(l)
                j=j+1
        return array_int

sample_size=20000
#we increase the sample_size 

#this will generate a random list of number with sample size.
random_gen_list= random.sample(range(sample_size),sample_size)


#this will convert the random_gen_list to c_array data type
c_array = convert_pythonlist_to_c_array(random_gen_list)

#CDLL is the Dynamic Linking library

c_link_library=ctypes.CDLL("/Users/ravishankerthadishetti/Downloads/bolters/project/shared_lib.so")

s_time = time.time()
csort=c_link_library.maxSubArraySum
csort.argtypes=[c_void_p,c_int]
csort(c_array,len(random_gen_list))

e_time = time.time()
ctype_time=e_time-s_time
print('C with python required time in microseconds is %s',ctype_time*1000000)


