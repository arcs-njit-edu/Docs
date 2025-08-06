## Overview
Before submitting your job to the scheduler, it's important to know how many cores and memory your task requires and all this will be assigned based on the number of nodes you request.

### Partition (Use `--partition`)
Wulver has three partitions, differing in GPUs or RAM available:

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/partitions.csv')
# Replace NaN with 'NA'
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

### Priority (Use `--qos`)
Wulver has three levels of “priority”, utilized under SLURM as Quality of Service (QoS):
```python exec="on"
import pandas as pd
import numpy as np
df = pd.read_csv('docs/assets/tables/slurm_qos.csv')
df.replace(np.nan, 'NA', inplace=True)
df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: f"<code>{str(x).strip()}</code>")
# Apply style to prevent wrapping, hide the index, and convert to HTML
html_output = df.style.set_properties(**{'white-space': 'nowrap', 'text-align': 'left'}, subset=df.columns[0]).hide(axis='index').to_html()
print(html_output)
```

## How many cores and memory do I need?
There is no deterministic method of finding the exact amount of memory needed by a job in advance. A general rule of thumb is to overestimate it slightly and then scale down based on previous runs. Significant overestimation, however, can lead to inefficiency of system resources and unnecessary expenditure of CPU time allocations.

We have tool `seff` in Slurm which you can use to check how much resources your job consumed and based on that re-adjust the configurations.

Understanding where your code is spending time or memory is key to efficient resource usage. Profiling helps you answer questions like:

- Am I using too many CPU cores without benefit?
- Is my job memory-bound or I/O-bound?
- Are there inefficient loops, repeated operations, or unused computations?

### Tips for optimization
- Use multi-threaded or parallel libraries (OpenMP, MPI, NumPy with MKL).
- Avoid unnecessary data copying or large in-memory objects.
- Stream large files instead of loading entire datasets into memory.
- Use job arrays for independent jobs instead of looping in one script.


## Be careful about invalid configuration
Misconfigured job submissions can lead to job failures, wasted compute time, or inefficient resource usage.<br> 
Below are some common mistakes and conflicts to watch out for when submitting jobs to SLURM:

- Asking for more CPUs, memory, or GPUs than any node in the cluster can offer. Job stays in pending state indefinitely with reason like `ReqNodeNotAvail or Resources`
- Mismatch Between CPUs and Tasks. For example: Using `--ntasks=4` and `--cpus-per-task=8` but your script is single-threaded. You're blocking 32 cores but using only 1 effectively — leads to very low CPU efficiency.
- Specifying walltime of more then 3 days is not allowed. 
- Submitting to a partition that doesn’t match your job type. For eg. Requesting a GPU with a non-GPU partition: `--partition=standard --gres=gpu:1`. Job will fail immediately or be held forever.


