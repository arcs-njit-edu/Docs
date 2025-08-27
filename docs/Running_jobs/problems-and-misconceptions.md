# Overview

New HPC users often assume that requesting more resources (CPUs, GPUs, memory) will automatically make their jobs run faster. In reality, performance depends on how the software is written and configured. Submitting jobs with incorrect resource requests can result in wasted allocations, slower performance, and unnecessary load on shared compute nodes. Below are some common mistakes and their solutions.

### **Misconception:** “If I allocate more CPUs, my software will automatically use them”

Many applications are not parallelized by default. Requesting multiple CPUs (--ntasks > 1) will not speed up execution unless your software is explicitly written to take advantage of parallelism (e.g., via MPI, OpenMP, or job arrays). Otherwise, the job may simply run the program multiple times in parallel instead of speeding it up.

**Example of incorrect job script:**

```shell
#!/bin/bash -l
#SBATCH --job-name=python
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err
#SBATCH --partition=general
#SBATCH --ntasks=4
#SBATCH --qos=standard
#SBATCH --time=30:00
#################################################################################
module load foss/2023b Python
srun python test.py
```

**Problem:** This script launches test.py 4 times since no parallelism is enabled in the code.

**Solution:** If your code is serial, request only 1 task: `srun -n1 python test.py` or `python test.py`

To truly leverage multiple CPUs, use parallel programming libraries such as [mpi4py](https://mpi4py.readthedocs.io/en/stable/tutorial.html) and [Parsl](https://parsl.readthedocs.io/en/stable/quickstart.html)
 

### **Misconception:** “My jobs run slower when I request more resources”

Requesting excessive resources can actually degrade performance. For example, oversubscribing CPUs (assigning more threads than available cores) leads to CPU contention, slowing down computations.

**Example of problematic job script:**

```shell
#!/bin/bash -l
#SBATCH -J gmx-test
#SBATCH -o %x.%j.out
#SBATCH -e %x.%j.err
#SBATCH --partition=gpu
#SBATCH --qos=standard
#SBATCH --time 72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=128
#SBATCH --gres=gpu:4
#################################################################################
module purge
module load wulver
module load foss/2021b GROMACS/2021.5-CUDA-11.4.1
gmx grompp -f run.mdp -c npt2.gro -r npt2.gro -p topol.top -o run.tpr
srun gmx_mpi mdrun -deffnm run -cpi run.cpt -v -ntomp 2 -pin on -tunepme -dlb yes -noappend
```

**Problem:** With `--ntasks-per-node=128` and `-ntomp 2`, the job requests **256** CPUs, but the node only has 128. This overloads the node and slows down execution.

**Solution:** Match resource requests to the available hardware. For example:

This job will launch using 64 cores with 2 threads per core.

```shell
#!/bin/bash -l
#SBATCH -J gmx-test
#SBATCH -o %x.%j.out
#SBATCH -e %x.%j.err
#SBATCH --partition=gpu
#SBATCH --qos=standard
#SBATCH --time=72:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=64
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:4
#################################################################################
module purge
module load wulver
module load foss/2021b GROMACS/2021.5-CUDA-11.4.1
gmx grompp -f run.mdp -c npt2.gro -r npt2.gro -p topol.top -o run.tpr
srun gmx_mpi mdrun -deffnm run -cpi run.cpt -v -ntomp 2 -pin on -tunepme -dlb yes -noappend
```

!!! tips
    - Use the checkload command to monitor CPU usage.
    - Cancel jobs that overload nodes and adjust scripts accordingly.
    - Align --ntasks, --cpus-per-task, and application threading flags (-ntomp, OMP_NUM_THREADS, etc.) with actual node architecture.