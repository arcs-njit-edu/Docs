# Performance Testing Overview

To help users select the appropriate MIG profile for their workloads, we conducted benchmark tests using LLM fine-tuning, PyTorch training, and GROMACS molecular dynamics simulations. Tests were run on the NVIDIA A100 GPUs (full 80 GB and MIG profiles) available on Wulver.

The results below show differences in runtime, accuracy, memory usage, and service unit (SU) cost across profiles. Observations and notes are included to explain unexpected results.

### GROWMACS

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/MIG/gromacs_performance.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

### LLM Fine-Tuning

A minimal QLoRA fine-tuning run was performed on the Qwen/Qwen2.5-1.5B-Instruct model using the public yahma/alpaca-cleaned dataset (1,000 samples, 1 epoch) across different MIG profiles and a full A100 80 GB GPU. Runtime, GPU/CPU memory usage, and service unit (SU) cost were recorded to compare resource efficiency and performance.

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/MIG/llm-finetuning.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

### MNIST Simple CNN

Trains a lightweight convolutional network on the MNIST handwritten digit dataset (grayscale, 28×28) for a small number of epochs. This benchmark measures training time, accuracy, and GPU memory usage to show how smaller MIG profiles handle low-compute, low-memory workloads

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/MIG/pytorch_mnist_simplecnn.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

### CIFAR10 DeepCNN

A custom deep convolutional network with multiple convolution–batch normalization–ReLU blocks was trained on CIFAR-10 (RGB, 32×32). This architecture has a higher parameter count and more convolutional layers than the MNIST test, making it more GPU-compute intensive. It is designed to test how MIG profiles handle deeper feature extraction workloads, where convolutional throughput and memory bandwidth significantly affect performance.

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/MIG/pytorch_cifar10_deepcnn.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```

### CIFAR10 ResNet

A custom ResNet-style architecture with residual connections was trained on CIFAR-10 (RGB, 32×32). Skip connections help preserve gradient flow in deep networks, enabling effective training with more layers. This test emphasizes how MIG partitions perform on workloads with irregular memory access patterns and additional elementwise operations, compared to the sequential convolution-heavy DeepCNN.

```python exec="on"
import pandas as pd 
import numpy as np
df = pd.read_csv('docs/assets/tables/MIG/pytorch_cifar10_resnet.csv')
df.replace(np.nan, 'NA', inplace=True)
print(df.to_markdown(index=False))
```
!!! note
    SU values are calculated as:  
    `SU = (max(CPUs, RAM/4GB) + 16 × (GPU_mem/80)) × hours`  
    
    **Example** (A100_20GB, 70.70 s runtime, 1 CPU, 4 GB RAM, 20 GB GPU):  
    ```
    SU = (max(1, 4/4) + 16 × (20/80)) × (70.70 / 3600)
       = (1 + 4) × 0.01964 ≈ 0.098
    Cost/Performance = SU / Accuracy = 0.098 / 99.20 ≈ 0.00099
    ```

## Key Takeaways

- **Performance scales with MIG size—but not always linearly**: Larger MIG profiles generally train faster and simulate more nanoseconds/day in GROMACS, but the speedup is often less than proportional to the increase in allocated GPU memory or compute units.

- **Memory footprint depends on model size and MIG profile**: CUDA allocators and kernel workspaces scale with available GPU resources, so bigger MIGs may report higher memory usage even when running the same workload. This is expected and not necessarily wasteful.

- **Workload type matters**:

    - Compute-heavy, parallelizable workloads (e.g., deep CNNs, GROMACS) benefit more from larger MIG profiles.

    - Smaller models or short jobs (e.g., MNIST, small LLMs) may see little to no gain in runtime from a full GPU compared to a well-sized MIG.

- **Service Unit (SU) efficiency varies**: In some cases, smaller MIG profiles deliver better SU cost per unit of work (e.g., SU/ns in GROMACS) because they avoid underutilizing unused GPU capacity.

- **Avoid over-provisioning**: Select the smallest MIG profile that meets your workload’s memory and performance requirements—this improves overall cluster utilization and reduces queue wait times.

- **OOM is a real constraint**: Some workloads (e.g., LLM fine-tuning) may simply not fit on smaller MIG profiles, making larger profiles a requirement, not a preference.

- **Parallel isolation benefits**: MIG partitions prevent interference between concurrent users, making performance more predictable in shared environments compared to time-sliced GPUs.