from typing import Optional, Union
from __future__ import division
from numba import cuda
import numpy as np
import cupy as cp
import math

from gsc.operations import Operations


class Single_Machine(Operations):
    def __init__(
        self,
        processing_time: Optional[Union[list, np.ndarray, cp.core.core.ndarray]],
        due_date: Optional[Union[list, np.ndarray, cp.core.core.ndarray]],
        weights: Optional[Union[list, np.ndarray, cp.core.core.ndarray]],
        n_samples: int,
        n_jobs: int,
        percent_cross: float = 0.5,
        percent_intra_cross: float = 0.5,
        percent_mutation: float = 0.5,
        percent_intra_mutation: float = 0.1,
        percent_migration: float = 0.5,
        percent_selection: float = 0.1,
        fitness_type: str = "E_Lw",
    ):
        self._n_samples = self.set_n_samples(n_samples)
        self._n_jobs = self._set_n_jobs(n_jobs)
        self._n_machines = 1
        self._n_operations = 1
        self._fitness_type = self._set_fitness_type(fitness_type)
        self._processing_time = cp.expand_dims(
            self._set_processing_time(processing_time), axis=1
        )
        self._machine_sequence = cp.expand_dims(
            cp.zeros(n_jobs, dtype=cp.float32), axis=1
        )
        self._due_date = self._set_due_date(due_date)
        self._weights = self._set_weights(weights)
        self._percent_cross = self.set_percent_cross(percent_cross)
        self._percent_intra_cross = self.set_percent_intra_cross(percent_intra_cross)
        self._percent_mutation = self.set_percent_mutation(percent_mutation)
        self._percent_intra_mutation = self.set_percent_intra_mutation(
            percent_intra_mutation
        )
        self._percent_migration = self.set_percent_migration(percent_migration)
        self._percent_selection = self.set_percent_selection(percent_selection)
        self._fitness = cp.array([], dtype=cp.float32)
        self._population = cp.array([], dtype=cp.float32)
        self._population = self._set_population()
