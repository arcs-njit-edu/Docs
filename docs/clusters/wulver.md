# Wulver

Wulver is a new cluster anticipated to be available at the end of 2023. To get started with Wulver, please check the details in [get started on Wulver](get_started_on_Wulver.md)

## Specifications:

```python exec="on"
import pandas as pd
df = pd.read_csv('docs/assets/tables/wulver.csv')
print(df.to_markdown(index=False))
```

<!--
* 100 x Dell R6525 CPU Nodes
* 2 x AMD 7753 2.45 GHz, 64C128T - Total cores: 12,800
* Memory 512 GB/node - Total memory: 51.2 TB
* Theoretical Performance: 501.760TFlops
* 2 x Dell R6525 High Memory Nodes
* 2 x AMD 7753 2.45 GHz, 64C128T - 256 Total Cores
* Memory - 2 TB/node - Total Memory 4TB
* Theoretical Performance: 10.035TFlops
* 25 x Dell XE8545 GPU Nodes
* 2 x AMD EPYC 7713 2.0GHz,64C/128T - Total cores: 3200
* Memory 512 GB/node - Total memory: 1 TB
* 4 x NVIDIA HGX A100 - 4x A100 SXM4 80GB - total GPUs: 100
* Theoretical Performance: 102.4TFlops (cpu) + 970TFlops (gpu)
* Totals 127 Nodes, 16,256 Cores, 56.2 TB RAM
* Theoretical Performance: 1.584PFlops
-->

* 100 GB High throughput/low latency Infiniband network
* Arcastream Storage
    * Parallel filesystem allowing multiple read/write operations
    * Max performance 20 GB/s
    * Hierarchical storage; NVME scratch, SAS, Cloud
    * User transparent transfer from high-speed to medium to archive storage
    * 1 PB total storage
* Virtualized Support and login nodes
* Management and deployment overseen by NJIT:
    * Nvidia Bright Cluster Manager
    * X-ISS system administration
    * SLURM scheduler with full support
    * InfiniBand support via Dell or directly from Mellanox
    * Will be deployed in the Databank data center in Piscataway

