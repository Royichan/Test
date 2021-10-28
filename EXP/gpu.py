from numba import cuda,jit
import numpy as np

@cuda.jit
def f(i):
    for _ in range(3000): 
        i[0]=i[0]+10
        i[1]=i[1]+10
        i[2]=i[2]+10
        print(i[0])

#gpu = cuda.get_current_device()
#print("name = %s" % gpu.name)
#print("multiProcessorCount = %s" % str(gpu.MULTIPROCESSOR_COUNT))
#print("maxThreadsPerBlock = %s" % str(gpu.MAX_THREADS_PER_BLOCK))
#print("maxSharedMemoryPerBlock = %s" % str(gpu.MAX_SHARED_MEMORY_PER_BLOCK))
k=[2,8,9]
a=np.array(k)
f(a)
#threadsperblock = 4
#blockspergrid = (a.size + (threadsperblock - 1))
f[blockspergrid, threadsperblock](a)
#cuda.synchronize()