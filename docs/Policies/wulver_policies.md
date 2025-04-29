# Wulver Usage and Condo Policies

Proposed Wulver Usage and Condo Policies

## Faculty Computing Allowance

Faculty PIs are allocated 300,000 Service Units (SU) per year on request at no cost. An SU is equal to 1 core hour on a standard node. For more details on calculating SUs for GPUs, see [Wulver SLURM](slurm.md). All users working as part of the PIs project will use this allocation. Multiple PIs working on the same project may pool SUs. The SUs can be renewed annually by providing a brief report describing how the SUs were used and a list of publications, presentations, and awards generated from research conducted. Additional SUs may be purchased at a cost of $0.005/SU. The minimum purchase is 50,000 SU (250 USD). 
!!! note

    The 300,000 SUs are available on `--qos=standard` only. If PI does not want to buy more SUs, PI's group members can use `--qos=low` which does not have any SU charges. For more details, see [SLURM QOS](slurm.md#using-slurm-on-wulver) 

## User Storage Allowance

Users will be provided with 50GB of `$HOME` directories. Home directories are backed up. PIs are additionally provided 2TB project directories. These project directories are backed up. Very fast NVME scratch is available to users. This scratch space is for temporary files generated during a run and will be deleted after 30 days. Additional project storage can be purchased if needed. This additional project space will also be backed up. Users need to manage data so that backed-up data fits in the project directory space. Transient, or rapidly changing data should be stored in the scratch directory. Long-term storage with backups or archival storage for research data will be stored in a yet to be determined campus wide storage resource.

## Shared Condo Partnership

Faculty who routinely need more resources than the initial allocation may buy nodes and contribute to the cluster. A catalog of select hardware for inclusion in the cluster will be made available. The PI and associated users will be able to submit jobs with a higher priority up to the resources contributed. Note that these jobs may or may not run on the actual nodes purchased. The allocated resources will be available via a floating reservation for the amount of resources purchased. Contributors will be able to additionally submit jobs using SUs as well as lower priority. The university will subsidize all infrastructure costs for these nodes. This floating reservation will be available for five years.

## Private Pool

If the shared condo module does not satisfy the needs of the PI, a private pool may be set up. In addition to the nodes, the PI will be charged for all infrastructure costs, including but not limited to electricity, HVAC, system administration, etc. It is strongly recommended to first try the shared condo model. If the shared condo model does not work, the nodes can be converted to a private pool.

## Job Priorities

* Standard Priority
    * Faculty PIs are allocated 300,000 Service Units (SU) per year on request at no cost
    * Wall time maximum - 72 hours
    * Additional SUs may be purchased at a cost of $0.005/SU
    * The minimum purchase is 50,000 SU ($250)
    * Jobs can be superseded by those with higher priority jobs

* Low Priority
    * Not charged against SU allocation
    * Wall time maximum - 72 hours
    * Jobs can be preempted by those with higher and standard priority jobs when they are in the queue

* High Priority
    * Not charged against SU allocation
    * Wall time: 72 hours (default), PI can request longer walltimes up to 30 days. ARCS HPC reserves the right to reboot nodes once a month for maintenance — the second Tuesday of each month. See [Cluster Maintenance Updates and News](../news/index.md) for details
    * Only available to contributors