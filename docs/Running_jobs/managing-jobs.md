## Overview

Managing and monitoring your jobs effectively helps ensure efficient use of resources and enables quicker debugging when things go wrong. Slurm provides several built-in commands to track job status, usage, and troubleshoot issues.

SLURM has numerous tools for monitoring jobs. Below are a few to get started. More documentation is available on the [SLURM website](https://slurm.schedmd.com/man_index.html).

The most common commands are: 

- List all current jobs: `squeue`
- Job deletion: `scancel [job_id]`
- Run a job: `sbatch [submit script]`
- Run a command: `srun <slurm options> <command name>`

### SLURM User Commands 

| Task                |              Command              | 
|---------------------|:---------------------------------:|
| Job submission:     |      `sbatch [script_file]`       |
| Job deletion:       |        `scancel [job_id]`         |
| Job status by job:  |         `squeue [job_id]`         |
| Job status by user: |      `squeue -u [user_name]`      |
| Job hold:           |     `scontrol hold [job_id]`      |
| Job release:        |    `scontrol release [job_id]`    |
| List enqueued jobs: |             `squeue`              |
| List nodes:         | `sinfo -N OR scontrol show nodes` |
| Cluster status:     |              `sinfo`              |
 

## Use these commands to manage and monitor your jobs

=== "seff"

       - The `seff` command is a handy tool to assess how efficiently your job used the requested resources **after it has completed**. 
       - Using `seff` can help you adjust your future job scripts to **request only as much memory/time as truly needed**, improving scheduler fairness and reducing wasted resources.


       ```shell
       $ seff
       Usage: seff [Options] <Jobid>
              Options:
              -h    Help menu
              -v    Version
              -d    Debug mode: display raw Slurm data
       ```
       **Example output**

       ```shell
       $ seff 575079
       Job ID: 575079
       Cluster: wulver
       User/Group: ls565/ls565
       State: COMPLETED (exit code 0)
       Cores: 1
       CPU Utilized: 00:00:19
       CPU Efficiency: 67.86% of 00:00:28 core-walltime
       Job Wall-clock time: 00:00:28
       Memory Utilized: 4.21 MB
       Memory Efficiency: 0.11% of 3.91 GB
       ```

=== "squeue"

       - The `squeue` command lets you check all the jobs currently running/pending/queued in the Wulver.
       - You can use `squeue -u $LOGNAME` to check your your jobs in the queue.

       ```shell
       $ squeue
       JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
       586871   general start_se    bb474 PD       0:00      1 (ReqNodeNotAvail, Reserved for maintenance)
       587618   general NF2300_G    km876  R      40:02      1 n0072
       587004   general     ens1    sh784  R   18:20:27      1 n0012
       586894   general 13a+H-E1   ab2757  R   23:57:52      1 n0042
       586893   general 13a+H-E1   ab2757  R   23:57:59      1 n0042
       586892   general 13a+H-E1   ab2757  R   23:58:04      1 n0042
       586891   general 13a+H-E1   ab2757  R   23:58:10      1 n0042
       586638   general TS_CPC-c   ab2757  R 1-19:40:55      1 n0097
       585445   general SN4A6CL0   sm3557  R 5-14:51:47      1 n0055
       585442   general SN4A6CL0   sm3557  R 5-14:51:56      1 n0055
       587554   general  dpptest    ea442  R    1:18:59      1 n0094
       587619   general Metionin     zr76  R      40:01      7 n[0071-0076,0094]
       586867   general  AU_mod1     zr76  R 1-00:20:18      9 n[0012,0030,0032,0034,0037,0040,0042,0060-0061]
       586713   general Au_mod3_     zr76  R 1-15:39:10      8 n[0093,0099,0102-0103,0109,0113,0118-0119]
       586615   general Au_mod3_     zr76  R 1-20:57:38     14 n[0022,0034,0044,0050-0051,0055,0084,0096,0113,0116-0119,0121]
       586493   general Au_mod2_     zr76  R 2-00:56:11      5 n[0013-0014,0018-0020]
       586492   general Au_mod2_     zr76  R 2-00:56:41      5 n[0006,0013,0114,0120-0121]
       586432   general     DlPC     pst4  R 2-02:16:21      9 n[0087,0094,0097,0101,0110,0113,0116-0118]
       586290   general     DsPE     pst4  R 2-17:36:10      9 n[0015,0017,0022,0030-0031,0034,0037,0041,0043]
       587612   general     DsPC     pst4  R      50:32      5 n[0065,0070-0071,0094,0113]
       ```                     

=== "scancel" 

       - The `scancel` command lets you cancel your job. 
       - It take your JobID as argument `scancel [job_id]`       

=== "quota_info"

       - The `quota_info` command lets you check your storage space and SUs consumed. [More info](../Running_jobs/service-units.md#check-quota)

       ```shell
       $ quota_info
       Usage for account: 2025-summer-wksp-612-kjc59-ls565
              SLURM Service Units: 42 CPU Hours (of 2500 CPU Hour quota)
                     User ls565 Usage: 42 CPU Hours (of 42 CPU Hours)
              PROJECT Storage: 0 GB (No quota)
                     User ls565 Usage: 0 GB (No quota)
              SCRATCH Storage: 0 GB (No quota) 
                     User ls565 Usage: 0 GB (No quota)
       Usage for account: kjc59
              SLURM Service Units: 4162 CPU Hours (of 304719 CPU Hour quota)
                     User ls565 Usage: 2802 CPU Hours (of 4162 CPU Hours)
              PROJECT Storage: 223 GB (of 2048 GB quota)
                     User ls565 Usage: 19 GB (No quota)
              SCRATCH Storage: 0 GB (of 10240 GB quota) 
                     User ls565 Usage: 0 GB (No quota)
       Usage for account: walsh
              SLURM Service Units: 1917 CPU Hours (of 302709 CPU Hour quota)
                     User ls565 Usage: 0 CPU Hours (of 1917 CPU Hours)
              PROJECT Storage: 81 GB (of 2048 GB quota)
                     User ls565 Usage: 0 GB (No quota)
              SCRATCH Storage: 0 GB (of 10240 GB quota) 
                     User ls565 Usage: 0 GB (No quota)
       HOME Storage ls565 Usage: 37 GB (of 50 GB quota)

       ```

!!! info
       Please keep checking your job's status using `squeue -u $LOGNAME` so that it doesn't stay pending due to incorrect job submission parameters.

!!! warning
       You can only cancel your jobs. Please don't try to cancel other users jobs.