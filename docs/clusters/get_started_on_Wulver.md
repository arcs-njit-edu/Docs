# Access to Wulver
Wulver is a new cluster which will be available by the end of 2023. To see the specifications of Wulver cluster, please see the [Wulver Documentation](wulver.md).
If you already have access to existing clusters such as Lochness, you can log in to Wulver using `ssh ucid@wulver.njit.edu`. Replace `ucid` with your UCID. If you don't have prior access to NJIT cluster, you need to request for access.
Faculty can obtain a login to NJIT's HPC & BD systems by sending an email to [hpc@njit.edu](mailto:hpc@njit.edu). Students can obtain a login either by taking a class that uses one of the systems or by asking their faculty adviser to [contact](mailto:hpc@njit.edu) on their behalf. Your login and password are the same as for any NJIT AFS system.

## Login to Wulver
Please see the documentation on [cluster access](cluster_access.md) for details.

## General Linux Commands
Since the operating system (OS) HPC cluster is linux based RHEL 8, users need to know linux to use the cluster.
In the table below, you can find the basic linux commands required to use the cluster. For more details on linux commands, please see the [Linux commands cheat sheets](https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet).

```python exec="on"
import pandas as pd

df = pd.read_csv('docs/assets/tables/commands.csv')
print(df.to_markdown(index=False))
```

## Wulver Filesystems

The Wulver environment is quite a bit like Lochness, but there are some key differences, especially in filesystems and SLURM partitions and priorities.

 Wulver Filesystems are deployed with more attention to PI ownership / group efforts:
1. The `$HOME` directory is not intended for primary storage and will have only 50GB quota. To run the simulations, compilations, etc., users need to use a project directory which has 2TB of storage per PI group. Students can store their files under their corresponding PI’s UCID in the `/project` directory.  For example, if PI’s UCID is `doctorx`, then students need to use the `/project/doctorx/` directory. 
2. Users can also store temporary files under the `/scratch` directory, likewise under a PI-group directory. For example, PI’s UCID is `doctorx`, so students need to use the `/scratch/doctorx/` directory.  Please note that the files under `/scratch` will be periodically deleted. To store files for longer than computations, please use the `/project` directory.  Files under `/scratch` are not backed up. For best performance simulations should be performed in the `/scratch` directory. Once the simulation is complete, the results should be copied into the `$HOME` or `/project` directory.  Files are deleted from `/scratch` after they are 30 days old.

## Software Availability
The software can be loaded via `module load` command. You see the following modules are loaded once you log in to the Wulver (Use the `module li`) command to see the modules. 
```bash
   1) easybuild   2) slurm/wulver   3) null
```

## Slurm Configuration

Please see [SLURM](slurm.md) for details in the slurm configuration.  
