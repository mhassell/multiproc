# next idea: look at assigning tons of work and letting the computer figure out what to do.
# lets make a directory with lots of little files that the process needs to open,
# write to, and close.

import multiprocessing as mp
import numpy as np
import glob
import time

def fileWriter(path):
    with open(path,'w') as f:
        f.write('{}'.format(np.random.randn()))
    
files = glob.glob('./testFiles/*txt');

queue = mp.Queue()

#processes = [mp.Process(target=fileWriter, args=(file,)) for file in files]

start = time.time()
with mp.Pool(4) as p:
    p.map(fileWriter,files)

# for p in processes:   
#     p.start()
    
# for p in processes:
#     p.join()

stop = time.time()

# multiproc time
print(stop-start)

# now single process
start2 = time.time()
for file in files:
    fileWriter(file)

stop2 = time.time()

# single proc time
print(stop2 - start2)