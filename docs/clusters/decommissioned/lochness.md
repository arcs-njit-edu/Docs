# Lochness

This very heterogeneous cluster is a mix of manufacturers, components, and capacities as it was built up in incremental purchases spanning several years. 

!!! warning "Lochness was decommissioned on March 2024. Many lochness nodes was incorporated into [Wulver cluster](wulver.md) 2Q 2025 for HPC course purposes."

## Specifications:


```python exec="on"
import pandas as pd
df = pd.read_csv('docs/assets/tables/lochness.csv')
#df.loc['Total'] = df.iloc[:,[1,4,6] ].sum(numeric_only=True)
#print(df.astype("string").fillna("").to_markdown(index=False))
df.loc["Total", df.columns[[1, 4, 6]]] = df.iloc[:, [1, 4, 6]].sum(numeric_only=True)

obj_cols = df.select_dtypes(include=["object", "string"]).columns
df[obj_cols] = df[obj_cols].astype("string").fillna("")

print(df.to_markdown(index=False, floatfmt="g"))
```

<!--
* Total Nodes: 224 including GPU nodes
* Total Cores: 28236
* Total GB RAM: 66738104 (mostly 385GB per node but some with as little as 32GB)
* GPU nodes: 28 
* Total GPUs: 64
* Fifteen different GPU models deployed:
* 8x  nodes w/ 2x P100 GPU(s)
* 4x  nodes w/ 2x A100 GPU(s)
* 3x  nodes w/ 4x TitanRtx GPU(s)
* 2x  nodes w/ 2x K20Xm GPU(s)
* 11x nodes with 1x or 2x other models of Nvidia GPUs
* Seventeen different CPU models deployed:
* 52x Intel(R) Xeon(R) Gold 6226R CPU @ 2.90GHz
* 40x Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz
* 20x Intel(R) Xeon(R) Silver 4216 CPU @ 2.10GHz
* 20x Intel(R) Xeon(R) Silver 4214 CPU @ 2.20GHz
* 15x Intel(R) Xeon(R) Gold 6230 CPU @ 2.10GHz
* 11x Intel(R) Xeon(R) Gold 6240R CPU @ 2.40GHz
* 29x nodes with 1x to 4x eleven other CPU models
-->
* All nodes have:
    * Ethernet network interface (1GigE or 10GigE)
    * Infiniband network interface (mix of HDR100, EDR, and FDR speeds)
    * 1TB local storage (mostly SSD but a few HD)
* All nodes have network accessible storage:
    * `/home/`: 26 TB
    * `/research/`: 97 TB
    * `/afs/cad/`: 50 TB 

The cluster also features

* "CentOS Linux 7 (Core)" operating system
* Virtualized login and control nodes
* SLURM job scheduler
* Warewulf stateless node provisioning
* Managed entirely by NJIT personnel

Roughly half under warranty; rest are time and materials
