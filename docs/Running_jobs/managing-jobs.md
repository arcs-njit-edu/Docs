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

       **Example Output** 

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
       ...
       ```                     

=== "scancel" 

       - The `scancel` command lets you cancel your job. 
       - It take your JobID as argument `scancel [job_id]`       

=== "quota_info"

       - The `quota_info` command lets you check your storage space and SUs consumed. [More info](../Running_jobs/service-units.md#check-quota)

       **Example Output** 

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

=== "checkq"

       The `checkq` command gives same output as `squeue` with extra details.

       **Example Output** 

       ```shell
       $ checkq

       JOBID    PARTITION     NAME     USER         ACCOUNT      STATE       TIME           START_TIME          SUBMIT_TIME   TIME_LIMIT CPUS NODE     NODELIST(REASON)     PRIORITY                  QOS
       586637      general TS_CPC-t   ab2757        champagn    PENDING       0:00                  N/A  2025-08-25T16:47:24   5-00:00:00   16    1 (ReqNodeNotAvail, Re        11419        high_champagn
       586636      general TS_CPC-c   ab2757        champagn    PENDING       0:00                  N/A  2025-08-25T16:47:19   5-00:00:00   16    1 (ReqNodeNotAvail, Re        11419        high_champagn
       587559      general   DLPE_8     pst4             cld    RUNNING 1-03:34:02  2025-08-27T11:11:51  2025-08-27T11:11:35   1-18:00:00  128    2         n[0020-0021]        10205                  low
       587560      general   DLPE_9     pst4             cld    RUNNING 1-03:34:02  2025-08-27T11:11:51  2025-08-27T11:11:49   1-18:00:00  128    4 n[0021,0031-0032,0035]        10205                  low
       587557      general   DLPE_6     pst4             cld    RUNNING 1-03:34:32  2025-08-27T11:11:21  2025-08-27T11:11:02   1-18:00:00  128    4    n[0057,0060-0062]        10205                  low
       587558      general   DLPE_7     pst4             cld    RUNNING 1-03:34:32  2025-08-27T11:11:21  2025-08-27T11:11:14   1-18:00:00  128    6 n[0007,0012,0015,0017,0020,0062]        10205                  low
       587556      general   DLPE_5     pst4             cld    RUNNING 1-03:35:02  2025-08-27T11:10:51  2025-08-27T11:10:34   1-18:00:00  128    3    n[0051,0055,0057]        10205                  low
       587555      general   DLPE_4     pst4             cld    RUNNING 1-03:35:32  2025-08-27T11:10:21  2025-08-27T11:10:19   1-18:00:00  128    2         n[0050-0051]        10205                  low
       587533      general   DLPE_3     pst4             cld    RUNNING 1-03:57:47  2025-08-27T10:48:06  2025-08-27T10:47:49   1-18:00:00  128    2         n[0012,0015]        10205                  low
       587532      general   DLPE_2     pst4             cld    RUNNING 1-03:58:17  2025-08-27T10:47:36  2025-08-27T10:47:34   1-18:00:00  128    2         n[0011-0012]        10205                  low
       587528      general   DLPE_1     pst4             cld    RUNNING 1-04:00:19  2025-08-27T10:45:34  2025-08-27T10:45:23   1-18:00:00  128    2         n[0007,0011]        10205                  low
       586819      general   DSPC_c     pst4             cld    RUNNING 2-04:38:34  2025-08-26T10:07:19  2025-08-26T10:07:18   2-20:00:00  128    6 n[0087,0096-0097,0100-0102]        10205                  low
       586720      general  Rstudio     hf78          zhiwei    RUNNING 2-17:32:06  2025-08-25T21:13:47  2025-08-25T21:08:18   3-00:00:00  128    1                n0033        10205                  low
       587945      general  vs-code    au252          amr239    RUNNING    3:25:42  2025-08-28T11:20:11  2025-08-28T11:19:41     13:00:00   32    1                n0062        10203                  low
       586248          gpu      dif   jl2356           wangj    PENDING       0:00                  N/A  2025-08-24T17:04:29  10-00:00:00   64    1 (ReqNodeNotAvail, Re        11561           high_wangj
       586839          gpu    sim_t     zw37           wangj    PENDING       0:00                  N/A  2025-08-26T10:46:29   3-00:00:00    1    1 (ReqNodeNotAvail, Re        10911             standard
       587851          gpu  gmx2023   ks2297             vak    PENDING       0:00                  N/A  2025-08-27T21:00:03   3-00:00:00    2    1 (ReqNodeNotAvail, Re        10708             standard
       587856          gpu  gmx2023   ks2297             vak    PENDING       0:00                  N/A  2025-08-27T21:43:31   3-00:00:00    2    1 (ReqNodeNotAvail, Re        10703             standard
       587912          gpu ::app=Ju    aad94           tyson    PENDING       0:00                  N/A  2025-08-28T02:04:23   3-00:00:00    4    1 (ReqNodeNotAvail, Re        10678             standard
       587964          gpu ::app=Ju    tb439          geller    PENDING       0:00                  N/A  2025-08-28T12:34:36   1-00:00:00   16    1 (ReqNodeNotAvail, Re        10615             standard
       588002          gpu ::app=Sp   ap2934             mx6    PENDING       0:00                  N/A  2025-08-28T14:12:43     20:00:00   10    1 (ReqNodeNotAvail, Re        10605             standard
       586249          gpu      dif   jl2356           wangj    RUNNING 3-21:41:09  2025-08-24T17:04:44  2025-08-24T17:04:44   4-04:00:00   66    1                n0046        11004           high_wangj
       587881          gpu ::app=Ju   jc2687           bs644    RUNNING   15:40:15  2025-08-27T23:05:38  2025-08-27T23:05:24   1-00:00:00   48    1                n0089        11003           high_bs644
       587985          gpu     bash    nk569            phan    RUNNING      42:50  2025-08-28T14:03:03  2025-08-28T14:03:03     10:00:00    5    1                n0048        11002            high_phan
       ...
       ```

=== "checkload"

       The `checkload` command gives you the cpu load on each node. 

       **Example Output** 

       ```shell
       $ checkload

       NODELIST   NODES PARTITION       STATE CPUS    S:C:T   MEMORY   CPU_LOAD    TIMELIMIT
          n0001       1       gpu       mixed  128   2:64:1   514000       6.08     infinite
          n0002       1       gpu   allocated  128   2:64:1   514000       3.97     infinite
          n0003       1       gpu       idle~  128   2:64:1   514000       0.00     infinite
          n0004       1       gpu       idle~  128   2:64:1   514000       0.00     infinite
          n0005       1       gpu       idle~  128   2:64:1   514000       0.00     infinite
          n0006       1  general*       idle~  128   2:64:1   514000       0.00     infinite
          n0007       1  general*   allocated  128   2:64:1   514000     128.08     infinite
          n0008       1  general*   allocated  128   2:64:1   514000     128.02     infinite
          n0009       1  general*   allocated  128   2:64:1   514000     128.06     infinite
          n0010       1  general*   allocated  128   2:64:1   514000     128.01     infinite
          n0011       1  general*   allocated  128   2:64:1   514000     128.06     infinite
          ...
       ```


=== "slurm_jobid"

       The `slurm_jobid [job_id]` command lets you check detailed info about your job. It requires your job_id as parameter.

       **Example Output** 

       ```shell
       $ slurm_jobid 588032


       ********************************************************************************************************************************************************************************************************************
                                                                      _   _      _  ___  _____      _     ____    ____  ____    _   _  ____    ____ 
                                                                      | \ | |    | ||_ _||_   _|    / \   |  _ \  / ___|/ ___|  | | | ||  _ \  / ___|
                                                                      |  \| | _  | | | |   | |     / _ \  | |_) || |    \___ \  | |_| || |_) || |    
                                                                      | |\  || |_| | | |   | |    / ___ \ |  _ < | |___  ___) | |  _  ||  __/ | |___ 
                                                                      |_| \_| \___/ |___|  |_|   /_/   \_\|_| \_\ \____||____/  |_| |_||_|     \____|
                                                                                                                                                   
                                                                      
       ********************************************************************************************************************************************************************************************************************

       Job ID is: 588032

       Total SU consumed: 0.0
       ╒═══════╤═════════╤═══════════╤══════════╤══════════╤═════════╤═════╤══════════╤═══════╤════════════════╤═════════╤═══════════╤════════════════╤════════════════╤════════════════╕
       │ User  │ Account │ Partition │   QOS    │ Elapsed  │  State  │ SU  │ NodeList │ NCPUS │     Start      │   End   │ Timelimit │    ReqTRES     │    WorkDir     │   SubmitLine   │
       ├───────┼─────────┼───────────┼──────────┼──────────┼─────────┼─────┼──────────┼───────┼────────────────┼─────────┼───────────┼────────────────┼────────────────┼────────────────┤
       │ ls565 │  kjc59  │  general  │ standard │ 00:00:05 │ RUNNING │ 0.0 │  n0061   │   1   │ 2025-08-28T14: │ Unknown │ 00:59:00  │ billing=1,cpu= │ /mmfs1/home/ls │ sbatch test.sh │
       │       │         │           │          │          │         │     │          │       │     41:07      │         │           │ 1,mem=4000M,no │      565       │                │
       │       │         │           │          │          │         │     │          │       │                │         │           │      de=1      │                │                │
       ╘═══════╧═════════╧═══════════╧══════════╧══════════╧═════════╧═════╧══════════╧═══════╧════════════════╧═════════╧═══════════╧════════════════╧════════════════╧════════════════╛
       ```


!!! info
       Please keep checking your job's status using `squeue -u $LOGNAME` so that it doesn't stay pending due to incorrect job submission parameters.

!!! warning
       You can only cancel your jobs. Please don't try to cancel other users jobs.