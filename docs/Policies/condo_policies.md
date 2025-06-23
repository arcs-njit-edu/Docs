# Shared Condo Partnership

## Cluster Resource Investment and Priority Access Policy

Faculty members who regularly require more resources than the standard allocation may choose to invest in additional resources—either partial or full nodes—thereby contributing to the growth of the cluster. A catalog of available partial node and GPU investment options is provided below. Principal Investigators (PIs) and their associated users will receive higher job priority, up to the amount of resources they have contributed. Please note that jobs may not necessarily run on the specific nodes purchased; instead, the contributed resources will be made available through a floating reservation equivalent to the purchased capacity.

Contributors can also submit jobs using standard SUs and at lower priority beyond their reserved allocation. The university will cover all infrastructure-related costs for these contributed nodes. This floating reservation will remain in effect for **five years**. If the hardware is upgraded or replaced before the end of this period, the job priority will transfer to the closest equivalent resources on the new hardware.

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