import multiprocessing as mp
import numpy as np

queue = mp.Queue()

def exampleFunction(queue):
    vec = np.random.random([50,1])
    print(vec)
    queue.put(vec)
    
    
processes = [mp.Process(target=exampleFunction, args=(queue,)) for x in range(50)]

for p in processes:
    p.start()

for p in processes:
    p.join()

results = np.array([queue.get() for p in processes])
# results = results.resize([5,5])

bb = np.random.random([5,1])

print(results)