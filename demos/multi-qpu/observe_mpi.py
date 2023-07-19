import cudaq, os, random, timeit
from cudaq import spin
import numpy as np

cudaq.mpi.initialize()
cudaq.set_target('nvidia-mqpu')

target = cudaq.get_target()
numQpus = target.num_qpus()

kernel, theta = cudaq.make_kernel(float)
qreg = kernel.qalloc(2)
kernel.x(qreg[0])
kernel.ry(theta, qreg[1])
kernel.cx(qreg[1], qreg[0])
# Define its spin Hamiltonian.
hamiltonian = 5.907 - 2.1433 * spin.x(0) * spin.x(1) - 2.1433 * spin.y(
    0) * spin.y(1) + .21829 * spin.z(0) - 6.125 * spin.z(1)

# Confirmed expectation value for this system when `theta=0.59`.
want_expectation_value = -1.7487948611472093

# Get the `cudaq.ObserveResult` back from `cudaq.observe()`.
# No shots provided.
result_no_shots = cudaq.observe(kernel,
                                hamiltonian,
                                0.59,
                                execution=cudaq.par.mpi)
expectation_value_no_shots = result_no_shots.expectation_z()
assert np.isclose(want_expectation_value, expectation_value_no_shots)

cudaq.mpi.finalize()
