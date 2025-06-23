# Shared Condo Partnership

## Cluster Resource Investment and Priority Access Policy

Faculty members who regularly require more resources than the standard allocation may choose to invest in additional resources—either partial or full nodes—thereby contributing to the growth of the cluster. A catalog of available partial node and GPU investment options is provided below. Principal Investigators (PIs) and their associated users will receive higher job priority, up to the amount of resources they have contributed. Please note that jobs may not necessarily run on the specific nodes purchased; instead, the contributed resources will be made available through a floating reservation equivalent to the purchased capacity.

Contributors can also submit jobs using standard SUs and at lower priority beyond their reserved allocation. The university will cover all infrastructure-related costs for these contributed nodes. This floating reservation will remain in effect for **five years**. If the hardware is upgraded or replaced before the end of this period, the job priority will transfer to the closest equivalent resources on the new hardware.

## Full node investment
Please contact [hpc@njit.edu](mailto:hpc@njit.edu) to discuss your specific computational needs.

## Partial Node Investment
You can invest in partial nodes, either on a per-CPU or per-MIG GPU basis. This flexible model allows you to customize and build resources tailored to your research requirements. A sample configuration table can be provided to help you plan your investment.

```python exec="on"
import pandas as pd
df = pd.read_csv('docs/assets/tables/condo.csv')
print(df.to_markdown(index=False))
```

!!! info
    
    MIG (Multi-Instance GPU) allows a single NVIDIA GPU (like the A100) to be split into multiple independent instances, each with dedicated compute and memory resources. This enables multiple users to share a GPU efficiently. It’s ideal for running smaller workloads without needing a full GPU.

**Example:** If your research workflow requires 128 CPU cores with 4 GB RAM per core, one 40 GB MIG, and one 20 GB MIG, you can invest in 128 CPUs at $150 per core ($19,200), plus the MIGs ($5,000 for 40 GB and $2,500 for 20 GB), for a total cost of $26,700.


## Shared Condo Partnership

Faculty who routinely need more resources than the initial allocation may buy nodes and contribute to the cluster. A catalog of select hardware for inclusion in the cluster will be made available. The PI and associated users will be able to submit jobs with a higher priority up to the resources contributed. Note that these jobs may or may not run on the actual nodes purchased. The allocated resources will be available via a floating reservation for the amount of resources purchased. Contributors will be able to additionally submit jobs using SUs as well as lower priority. The university will subsidize all infrastructure costs for these nodes. This floating reservation will be available for five years.

## Private Pool

If the shared condo module does not satisfy the needs of the PI, a private pool may be set up. In addition to the nodes, the PI will be charged for all infrastructure costs, including but not limited to electricity, HVAC, system administration, etc. It is strongly recommended to first try the shared condo model. If the shared condo model does not work, the nodes can be converted to a private pool.
