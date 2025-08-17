# Performance Testing Overview

To help users select the appropriate MIG profile for their workloads, we conducted benchmark tests using LLM fine-tuning, PyTorch training, and GROMACS molecular dynamics simulations. Tests were run on the NVIDIA A100 GPUs (full 80 GB and MIG profiles) available on Wulver.

The results below show differences in runtime, accuracy, memory usage, and service unit (SU) cost across profiles. Observations and notes are included to explain results.

### GROMACS

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/MIG/gromacs_performance.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

### LLM Fine-Tuning

The benchmark script fine-tunes the Qwen 1.5B Instruct model on the Alpaca-cleaned dataset using QLoRA. Training is done with 4-bit quantization to save memory and LoRA adapters so that only a small set of parameters are updated. The Hugging Face TRL `SFTTrainer` handles training, while the script also logs runtime, GPU/CPU memory, and tokens processed per second. The setup runs consistently on both full NVIDIA's A100 80GB GPU and different MIG slices (10 GB, 20 GB, 40 GB), making it useful for comparing speed and cost across profiles.

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/MIG/llm-finetuning.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

- **Peak Allocated ≈ 5.7 GB across all runs**: The model + LoRA fine-tune has a fixed memory demand, regardless of MIG size.
    
- **Peak Reserved varies** (8.9 → 23.5 GB): PyTorch’s caching allocator grabs bigger chunks when more GPU memory is available, but this doesn’t change training feasibility.
    
- **SU efficiency (SUs / 1M tokens)** is best on **20 GB MIG (16.39)**: Lowest cost per unit of work.

- **Full 80 GB GPU** is fastest but least efficient (27 SU / 1M tokens).

!!! note
    SU values are calculated as:  
    `SU = (max(#CPUs, #RAM/4GB) + 16 × (GPU_mem/80)) × hours`  
    
    **Example** (A100_20GB, 0.556 hr walltime, 1 CPU, 4 GB RAM, 20 GB GPU):  
    ```
    SU = (max(1, 4/4) + 16 × (20/80)) × 0.556
       = (1 + 4) * 0.556 = 2.78
    ```
    
### Matrix Multiplication Benchmarks

We ran a **matrix multiplication benchmark** on different NVIDIA A100 MIG profiles and the full GPU. The test multiplies large square matrices (sizes like 4096×4096 up to 49k×49k) using PyTorch and CUDA.

Matrix multiplication is the **core operation in deep learning** — it’s what neural networks spend most of their time doing. Measuring how many **TFLOPs (trillion floating point operations per second)** each MIG slice achieves gives a good picture of its raw compute power.

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/MIG/matrix_multiplication.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

- **Peak FP16 performance** (fast half-precision mode used in AI training).
- **Peak FP32 performance** (single precision with TF32 tensor cores, higher accuracy but slower).
- **Largest tested matrix size (n)** where peak performance was observed.
- **Peak GPU memory usage**, to see whether memory or compute was the bottleneck.
- **SU usage factor**, to tie performance back to billing.

The results show that **performance scales almost linearly with MIG size (number of SMs)**, while memory never became the limiting factor. This means compute capacity is the main driver of speed, and users can choose between smaller slices (cheaper, slower) or larger slices (faster, higher SU rate) depending on their workload needs.

