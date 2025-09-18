# Overview

Wulver is a shared resource among researchers, faculty and students. It is important to use it efficiently so that everyone can complete their tasks without delay. Therefore, running jobs on Wulver, you should follow certain norms which ensures that your work is done on time and also lets others run their task without any conflict. We use Slurm on Wulver to schedule and manage jobs.


## What is SLURM?

Slurm (Simple Linux Utility for Resource Management) is an open-source workload manager and job scheduler designed for high-performance computing clusters. It is widely used in research, academia, and industry to efficiently manage and allocate computing resources such as CPUs, GPUs, memory, and storage for running various types of jobs and tasks. Slurm helps optimize resource utilization, minimizes job conflicts, and provides a flexible framework for distributing workloads across a cluster of machines. It offers features like job prioritization, fair sharing of resources, job dependencies, and real-time monitoring, making it an essential tool for orchestrating complex computational workflows in diverse fields.


## Some best practices to follow:

- **Request Only the Resources You Need :**  
    Be precise when requesting CPUs, memory, GPUs, and runtime.<br> 
    Avoid overestimating job time (`--time`) and memory (`--mem`) as it reduces scheduler efficiency.<br>
    Use monitoring tools to understand your typical usage patterns and adjust accordingly.<br>

- **Do not run jobs on Login Node :**  
    Login node is the entry point for Wulver and has limited memory and resources.<br>
    Please avoid directly running jobs on the login node as it can slow down the system for everyone.<br> 
    Always submit jobs to compute nodes via slurm script or start an interactive session.

- **Use Appropriate Partitions :**  
    Submit jobs to the correct partition based on resource needs (e.g., GPU, high-memory).<br>
  
- **Test and Debug with Small Jobs First :**  
    Use short test runs or dedicated debug partitions for code testing or troubleshooting.<br>
    This helps prevent long-running failures and wasted compute hours.<br>

- **Monitor Your Jobs :**  
    Please use commands like `squeue`, `slurm_jobid $jobid`, `seff $jobid` to check your job status <br>
    You can also use our [Ondemand Tools](../OnDemand/4_tools.md).<br>

- **Respect Fair Usage Policies :**  
    Do not monopolize shared resources by submitting excessive large jobs.<br>
    Be mindful of Wulver's [usage policy](../Policies/wulver_policies.md).<br>

- **Leverage MIGs for Efficient GPU Utilization :**  
    Our Nvidia A100 GPUs have MIG implementation which allows a single GPU to be split into multiple isolated instances.<br>
    Use MIG-compatible partitions when your task doesn’t require the full GPU power<br>
    More info about [MIG](../MIG/index.md).<br>
  
