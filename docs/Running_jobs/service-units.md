## Overview 

Service Units (SUs) are the core accounting mechanism used to track and allocate compute usage on Wulver. Each job you run consumes a certain number of SUs based on the resources you request and the duration of your job.

SUs help us ensure fair usage of the HPC system and monitor consumption across different users, departments, or projects.

Since resources are limited, each PI's research account is allocated 300,000 Service Units (SUs) per year upon request at no cost. These SUs can be used via the standard [priority](#priority-use-qos) on the SLURM job scheduler. 
One SU is defined as 1 CPU hour or 4 GB of RAM per hour. 

!!! tip "Important information on SU"
    
    * The SU allocation is per PI account, not per individual student.
    * The allocation resets each fiscal year.
    * Students are expected to use SUs efficiently, as excessive usage may deplete their group's SU balance quickly.

If a group exhausts its SU allocation early, the PI has the option to purchase additional SUs or leverage higher [priority](#priority-use-qos) queues through investment. For more details, refer to the  [Wulver Policies](wulver_policies.md) and [Condo Policies](condo_policies.md).
Check the table below to see how SU will be charged for different partitions. 

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/SU.csv')
# Replace NaN with 'NA'
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

!!! warning "Memory request via job scheduler"
    
    Please note that in the above SU calculation, MAX(CPUs, RAM/4GB) in the `general` and `gpu` partition — this represents the maximum of the number of CPUs requested and the memory requested divided by 4GB. in `bigmem` it's 16 GB.

    * If you do not specify `--mem` in your SLURM job script, the job will be allocated the default 4GB of memory per core (16GB/core in `bigmem`), and you will be charged based on the number of CPUs requested.
    * If you do specify `--mem` to request more memory, the SU charge will be based on the maximum of CPU count and memory/4GB (memory/16GB in `bigmem`).
    Requesting more memory than the default will result in higher SU charges than if you had only specified CPUs.
    
    Therefore, please be mindful of the `--mem` setting. Requesting more memory than necessary can significantly increase your SU usage.

???+ example "Example of SU Charges"

    === "`general` Partition"
        | SLURM Directive            |    SU     |      Explanation |
        |---------------------|:---------:|:---------:|
        | 4 CPUs      |  MAX(4, 4*4G/4G) = 4  |     Since no memory requiremnt is specified, SU is charged based on the same number of CPUs       |
        | 4 CPUs + `--mem=64G`      |  MAX(4, 64G/4G) = 16 |    Since 64G memory is specified, the MAX function the evaluates the maximum of 4 CPUS, and 64G/4G= 16, resulting in a charge of 16 SUs         |
        | 4 CPUs + `--mem=4G`     |  MAX(4, 4G/4G) = 4 |   MAX function the evaluates the maximum of 4 CPUS, and 4G/4G= 1, resulting in a charge of 4 SUs          |
        | 4 CPUs + `--mem-per-cpu=8G`      |  MAX(4, 8G*4/4G) = 8 |  MAX function the evaluates the maximum of 4 CPUS, and 8G*4CPUs/4G = 8 , resulting in a charge of 8 SUs           |
    
    === "`bigmem` Partition"
        | SLURM Directive             |           SU                |                                                             Explanation                             |
        |-----------------------------|:---------------------------:|:----------------------------------------------------------------------------------------------------:|
        | 4 CPUs                      | MAX(4*1.5, 1.5*4*16G/16G) = 6     |                       On `bigmem` partition the usage factor is 1.5                     |
        | 4 CPUs + `--mem=64G`        | MAX(4*1.5, 1.5*64G/16G) = 6     | Since 64G memory is specified, the MAX function the evaluates the maximum of 4*1.5= 6 SUs, and 1.5*64G/16G= 6 SUs, resulting in a charge of 6 SUs |
        | 4 CPUs + `--mem=128G`         |  MAX(4*1.5, 1.5*128G/16G) = 12      |                    MAX function the evaluates the maximum of 4*1.5= 6 SUs, and 1.5*128G/16G= 12 SU, resulting in a charge of 12 SUs                    |
        | 4 CPUs + `--mem-per-cpu=8G` |  MAX(4*1.5, 1.5*8G*4/16G) = 6    |                MAX function the evaluates the maximum of 4*1.5= 6 SUs, and 1.5*8G*4CPUs/16G = 3 SUs , resulting in a charge of 6 SUs                |

    === "`gpu` Partition"
        | SLURM Directive            |    SU     |      Explanation |
        |---------------------|:---------:|:---------:|
        | 4 CPUs + 10MIG     |  MAX(4, 4*4G/4G) + 16 * (10G/80G) = 6  |     Since no memory requiremnt is specified, SU is charged based on the same number of CPUs and 10G of GPU memory      |
        | 4 CPUs + 20MIG      |  MAX(4, 4*4G/4G) + 16 * (20G/80G) = 8 |    SU is charged based on the same number of CPUs and 20G of GPU memory         |
        | 4 CPUs + 40MIG     |  MAX(4, 4*4G/4G) + 16 * (40G/80G) = 12 |   SU is charged based on the same number of CPUs and 40G of GPU memory          |
        | 4 CPUs + Full GPU      |  MAX(4, 4*4G/4G) + 16 * (80G/80G) = 20 |  SU is charged based on the same number of CPUs and 80G of GPU (A full GPU) memory            |
        | 4 CPUs + `--mem=64G` + Full GPU      |  MAX(4, 64G/4G) + 16 * (80G/80G) = 32 |  The MAX function evaluates the maximum of 4 SUs (from CPUs), and 64G/4G= 16 SUs (from memory). In addition, 16 SUs are charged from 80G of GPU (A full GPU) memory, bringing the total SU charge to 32 SUs  |
        | 4 CPUs + `--mem-per-cpu=8G` + Full GPU      |  MAX(4, 4*8G/4G) + 16 * (80G/80G) = 24 |  The MAX function the evaluates the maximum of 4 SUs (from CPUs), and 4*8G/4G= 8 SUs (from memory). In addition, 16 SUs are charged from 80G of GPU (A full GPU) memory, bringing the total SU charge to 24 SUs  |


### Check Quota

Users can check their account(s) SU utilization and storage usage via `quota_info UCID` command.
```bash linenums="1"
[ab1234@login01 ~]$ module load wulver
[ab1234@login01 ~]$ quota_info $LOGNAME
Usage for account: xy1234
   SLURM Service Units (CPU Hours): 277557 (300000 Quota)
     User ab1234 Usage: 1703 CPU Hours (of 277557 CPU Hours)
   PROJECT Storage: 867 GB (of 2048 GB quota)
     User ab1234 Usage: 11 GB (No quota)
   SCRATCH Storage: 791 GB (of 10240 GB quota)
     User ab1234 Usage: 50 GB (No quota)
HOME Storage ab1234 Usage: 0 GB (of 50 GB quota)
```
Here, `xy1234` represents the UCID of the PI, and "SLURM Service Units (CPU Hours): 277557 (300000 Quota)" indicates that members of the PI group have already utilized 277,557 CPU hours out of the allocated 300,000 SUs, and the user `xy1234` utilized 1703 CPU Hours out of 277,557 CPU Hours. This command also displays the storage usage of directories such as `$HOME`, `/project`, and `/scratch`. Users can view both the group usage and individual usage of each storage. In the given example, the group usage from the 2TB project quota is 867 GB, with the user's usage being 11 GB out of that 867 GB. For more details file system quota, see [Wulver Filesystem](get_started_on_Wulver.md#wulver-filesystems).
