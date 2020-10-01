import time 
from gsc.single_machine import Single_Machine
from gsc.job_shop import Job_Shop
import cupy as cp
import numpy as np
import matplotlib.pyplot as plt

start_time = time.time()


T_ = cp.expand_dims(cp.array([10,10,13,4,9,4,8,15,7,1,9,3,15,9,11,6,5,14,18,3],dtype=cp.float32),axis=1)
d_ = cp.array([10,10,13,4,9,4,8,15,7,1,9,3,15,9,11,6,5,14,18,3],dtype=cp.float32)
w_ = cp.array([10,10,13,4,9,4,8,15,7,1,9,3,15,9,11,6,5,14,18,3],dtype=cp.float32)
M_ = cp.expand_dims(cp.zeros(20,dtype=cp.float32),axis=1)

p = Single_Machine(n_samples=10000,n_jobs=20,processing_time=T_,machine_sequence=M_,due_date=d_,weights=w_,fitness_type="E_Lw")

fitness = []
fitness2 = []

for i in range(10):

    p.exec_crossA0001()
    p.exec_fitnessSM0001()
    p.exec_sortA0001()
    fitness2.append(p.get_fitness()[0])
    #print("___")
    #print(p.get_fitness()[0:5])
    p.exec_mutationA0001()
    p.exec_fitnessSM0001()
    p.exec_sortA0001()
    fitness2.append(p.get_fitness()[0])
    #print("___")
    #print(p.get_fitness()[0:5])
    p.exec_migrationA0001()
    p.exec_fitnessSM0001()
    p.exec_sortA0001()
    fitness2.append(p.get_fitness()[0])
    fitness.append(p.get_fitness()[0])
    #print("___")
    #print(p.get_fitness()[0:5])
    #print(cp.sum(p.get_population()))
    print(fitness[0]) 
print('the elapsed time:%s'% (time.time() - start_time))



