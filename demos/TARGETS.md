## CUDA Quantum `target` 
A `target` is a specification of the desired platform and simulator / QPU. It can be specified in C++ as a compile time flag in C++ and in Python as a runtime flag. Alteratively, it can also be specified within the application code. 

### Simulation backends
- state-vector (`cuStateVec`) 
- density-matrix (`dm`) 
- tensor-network (`cuTensorNet`)

### Hardware backends
- CPU only   \
- Single GPU   \
- Multi-GPU \
- Multi-QPU \
- Multi-node \

### Targets
- `default` \
- `nvidia` \
	- custatevec with single-GPU
        - `nvq++ --target nvidia ghz_state.cpp -o a.out`
        - `python3 --target nvidia ghz_state.py`  
- `nvidia-mqpu` \
	- custatevec with multi-QPU
        ```
        $ nvq++ --target nvidia-mqpu ghz_state.cpp -o a.out
        $ mpiexec -np 2 ./a.out
        ```
- `cuquantum_mgpu` \
	- custatevec with multi-GPU
        - `--target cuquantum_mgpu`
        - Not covered in this workshop
- `density-matrix-cpu` \
	- CPU-only multithreaded density matrix emulation
- `quantinuum` \
        - `--target quantinuum`
- `ionq` \
- more!

To print a list of all the targets and use, see 

```
import cudaq

targets = cudaq.get_targets()

for t in targets:
     print(t)
```



Note: Some of these targets are not be available for this workshop. 



