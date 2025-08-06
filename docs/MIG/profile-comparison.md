# MIG Profile Comparison

MIG profiles represent different partitions of a physical NVIDIA A100 80GB GPU. Each profile gives users a slice of compute and memory resources while maintaining full isolation from other workloads running on the same GPU.

On Wulver, the following MIG profiles are supported:

- `1g.10gb` – 10 GB memory ; 14 compute units
- `2g.20gb` – 20 GB memory ; 28 compute units
- `3g.40gb` – 40 GB memory ; 42 compute units
- `Full 80GB GPU` – No MIG (for jobs that require complete GPU access)

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/mig-profile-comparison.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

## What does `Xg.Ygb` mean?

- `Xg` = X GPU slice (partition of compute cores)
- `Ygb` = Y GB of dedicated GPU memory (slightly less is usable)
- Each larger profile uses more compute slices and memory, giving higher performance at higher SU cost.

## What is the difference between `3g.40gb` and `1g.10gb:3`?

Here is an overview of how one `3g.40gb` instance compares to three instances of `1g.10gb`.

**Parallel overhead**:<br>
With `1g.10gb:3`, you are likely running 3 independent processes (or jobs). You have to manage:

- Scheduling
- Data sharding
- Process startup overhead
- Aggregation (if needed)
- This introduces coordination overhead compared to a single job on 3g.40gb.

**Memory bandwidth and cache**:<br>

- `3g.40gb` will likely have higher peak memory bandwidth, since it's allocated as one larger slice.
- It can share L2 cache and copy engines more efficiently within the slice.

**Context Switching and Isolation**:<br>

- With `1g.10gb:3`, the slices are completely isolated, each with its own context and scheduler.
- With `3g.40gb`, there’s less context switching overhead, and you get better intra-GPC utilization.

**When 1g.10gb × 3 is better**:<br>

- You're running independent batch inference jobs
- You’re maximizing utilization across many users
- You don’t need cross-slice communication

**When 3g.40gb is better**:<br>

- You're training or fine-tuning a model that benefits from larger memory/cache
- You're running a single larger model or data batch
- You want simpler code and fewer moving parts
