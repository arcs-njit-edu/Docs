# Wulver Policies

## Computing Policy

Faculty PIs are allocated 300,000 Service Units (SU) per year on request at no cost. For more details on calculating SUs, see [Service Units](service-units.md). All users working as part of the PIs project will use this allocation. The SUs are renewed at the beginning of fiscal year. Additional SUs may be purchased at a cost of $0.005/SU. The minimum purchase is 50,000 SU (250 USD). 
!!! note

    The 300,000 SUs are available on `--qos=standard` only. If PI does not want to buy more SUs, PI's group members can use `--qos=low` which does not have any SU charges. For more details, see [SLURM QOS](node-memory-config.md).

Additionally, PI can request for more SUs by submitting the proposal. For more details, see [Allocation Policies](allocation_policies/index.md).

## Storage Policy

Users will be provided with 50GB of `$HOME` directories. Home directories are backed up. PIs are additionally provided 2TB project directories. These project directories are backed up. Very fast NVME scratch is available to users. 

This scratch space is for temporary files generated during a run and will be deleted after 30 days. Before deletion, users will receive an email from us specifying which files will be deleted, so that important files can be transferred to `/project` if necessary.

Additional project storage can be purchased if needed. This additional project space will also be backed up. Users need to manage data so that backed-up data fits in the project directory space. Transient, or rapidly changing data should be stored in the scratch directory. Long-term storage with backups or archival storage for research data will be stored in a yet to be determined campus wide storage resource. See [Wulver Filesystems](Wulver_filesystems.md) for details.

!!! warning

    Scratch space must not be used for long-term storage. Users should not use any commands to modify or manipulate files to alter timestamps, move files between directories within scratch, or take any similar actions to circumvent scratch purge policies. Users who violate this policy risk losing access to Wulver until the affected files have been cleaned up.

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