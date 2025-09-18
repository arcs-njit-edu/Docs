## Overview 

Wulver, like most shared HPC clusters, enforces certain job limitations to ensure fair and efficient resource usage among all users. These limitations are configured through Slurm and can affect the number of jobs, runtime, memory, GPU usage, and priority of execution. Understanding these limits can help you plan better, reduce job failures, and avoid unintentional misuse.


## General limitations of job scheduling

- **Walltime Limits**: `standard`, `low`, and `high` QoS: maximum 72 hours (3 days); `debug` partition: maximum 8 hours. [More info](../Running_jobs/node-memory-config.md/#priority-use-qos)

- **SUs exhausted**: Once your Service Units are exhausted, you can no longer run your jobs on `standard` or `high` priority but you can still use `low`.

- **Job preemption**: Jobs running on `low` priority can be preempted by `standard` or `high` priority jobs.

- **Maintenance**: During the maintenance downtime, logins will be disabled and all the jobs will be held in scheduler. If you submit your job before maintenance with a walltime overlapping the maintenance period then your job will also be held by scheduler. [More info](../faq/faq.md/#maintenance)

