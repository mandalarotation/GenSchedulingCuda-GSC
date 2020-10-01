from __future__ import division
from numba import cuda
import numpy as np
import cupy as cp
import math

from gsc.operations import Operations

class Job_Shop(Operations):
    def __init__(self,n_samples=10,n_jobs=8,n_operations=3,n_machines=3,processing_time,machine_sequence,due_date,weights,percent_cross=0.2,percent_intra_cross=0.5,percent_mutation=0.2,percent_intra_mutation=0.5,percent_migration=0.1,percent_selection=0.1,fitness_type="max_C"):
        self._n_samples = self.set_n_samples(n_samples)
        self._n_jobs = self._set_n_jobs(n_jobs)
        self._n_machines = self._set_n_machines(n_machines)
        self._n_operations = self._set_n_operations(n_operations)
        self._fitness_type = self._set_fitness_type(fitness_type)
        self._processing_time = self._set_processing_time(processing_time)
        self._machine_sequence = self._set_machine_sequence(machine_sequence)   
        self._due_date = self._set_due_date(due_date)
        self._weights = self._set_weights(weights) 
        self._percent_cross = self.set_percent_cross(percent_cross)
        self._percent_intra_cross = self.set_percent_intra_cross(percent_intra_cross)
        self._percent_mutation = self.set_percent_mutation(percent_mutation)
        self._percent_intra_mutation = self.set_percent_intra_mutation(percent_intra_mutation)
        self._percent_migration = self.set_percent_migration(percent_migration)
        self._percent_selection = self.set_percent_selection(percent_selection)
        self._fitness = cp.array([],dtype=cp.float32)
        self._population = cp.array([],dtype=cp.float32)
        self._population = self._set_population()


