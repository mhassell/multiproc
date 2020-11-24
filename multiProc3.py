# Next step: loading data from multiple processes and writing to an np array

import multiprocessing as mp
import numpy as np
import glob
import time

def fileWriter(path):
    with open(path,'w') as f:
        f.write('{}'.format(np.random.randn()))
        
def fileReader(path,array):
    with open(path,'r') as f:
        data = f.read()
        vals = data.split()
        array[:,-1] = vals;
    
files = glob.glob('./testFiles/*txt');

array = np.zeros([5,])

##
start = time.time()
with mp.Pool(4) as p:
    p.map(fileReader,[files,array])
s
stop = time.time()
##

# multiproc time
print(stop-start)

# now single process
start2 = time.time()
for file in files:
    fileWriter(file)

stop2 = time.time()

# single proc time
print(stop2 - start2)