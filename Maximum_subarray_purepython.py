import ctypes
#from timeit import default_timer as timer
from ctypes import *
import random
import sys

import time


#This function will identifies the subarray with maximum sum and return that maximum sum.
def maximum_subarraysum(arr,length):
    best=float('-inf')
    sumarr=0
    for i in range(0,length):
        if(sumarr+arr[i]>arr[i]):
            sumarr+=sumarr+arr[i]
        else:
            sumarr=arr[i]
        if(sumarr>best):
            best=sumarr
    return best

sample_size=15000

#generates the list of randomly generated numbers with provided sample_size  
# We changed the sample_size in both the ctype_python and pure_python and calculated the results. 
random_list= random.sample(range(sample_size),sample_size)


#S_time represents the start_time
s_time = time.time()
maximum_subarraysum(random_list,len(random_list))

#e_time represents the end_time
e_time = time.time()

#total_time_taken represents the total time taken with pure python for the given algorithm with given sample size.
total_time_taken=e_time-s_time

print('pure python required time in microseconds is %s',total_time_taken*1000000)
#print('Total Time Taken with Pure Python is {:.3f} secs'.format(total_time_taken))


