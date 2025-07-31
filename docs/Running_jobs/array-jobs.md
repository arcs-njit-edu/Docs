## Overview

Array jobs allow you to submit many similar jobs (like simulations or data processing tasks) with a single sbatch command. Each job in the array runs the same script but can process different input parameters.

**Analogy:** Imagine you're baking cookies in multiple batches. Each tray (array job) uses the same recipe (your script), but maybe with a different flavor (input). Instead of submitting each tray separately, you give the oven a list and it bakes them one by one or in parallel!

### Why use Array jobs?
Array jobs are powerful and efficient for batch-processing many similar tasks. They save time, simplify management, and optimize cluster usage.

If you’re running `50` experiments with the same script — don’t submit `50` jobs. Use an array job instead!

- Simplifies the submission of multiple similar jobs with a single script
- Reduces scheduler overhead by bundling related tasks into one job
- Keeps your job queue cleaner and more organized
- Makes it easier to monitor, debug, and manage large-scale workflows
- Ideal for training machine learning models on multiple datasets
- Useful for running simulations across a range of input parameters
- Efficient for processing large datasets by splitting them into manageable chunks

## Special Variables in Array Jobs

| Variable                  | Description                                      |
|---------------------------|--------------------------------------------------|
| `SLURM_JOB_ID`           | Unique ID for each job element (individual task) |
| `SLURM_ARRAY_JOB_ID`     | Shared job ID for the entire job array           |
| `SLURM_ARRAY_TASK_ID`    | The task ID for the current job in the array     |
| `SLURM_ARRAY_TASK_MIN`   | The lowest task ID in this job array             |
| `SLURM_ARRAY_TASK_MAX`   | The highest task ID in this job array            |
| `SLURM_ARRAY_TASK_COUNT` | Total number of tasks in the job array           |


## Array Job Examples
```slurm
#!/bin/bash -l
#SBATCH -J myprogram
#SBATCH --partition=general
#SBATCH --qos=standard
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --array=1-30
#SBATCH --output=myprogram%A_%a.out
#SBATCH --error=myprogram%A_%a.err  
#SBATCH --time=71:59:59

./myprogram input$SLURM_ARRAY_TASK_ID.dat
sleep 10
```

This example demonstrates how to use SLURM job arrays to run the same program multiple times with varying inputs. Here's what each part of the script does:

- `#SBATCH --array=1-30`: This line creates a job array with 30 tasks. Each task in the array gets a unique `SLURM_ARRAY_TASK_ID` from 1 to 30.

- `#SBATCH --output=myprogram%A_%a.out`
`#SBATCH --error=myprogram%A_%a.err`: These lines set up output and error file names for each array task. %A is replaced with the array job ID. %a is replaced with the task index (from 1 to 30). This prevents files from different tasks from overwriting each other.

- `./myprogram input$SLURM_ARRAY_TASK_ID.dat`: This runs the program using different input files for each task. For example:
    - Task 1 runs: `./myprogram input1.dat`
    - Task 2 runs: `./myprogram input2.dat`
    - …and so on up to `input30.dat`


- `sleep 10`: This is just a placeholder command to simulate a small wait time. You can remove or replace it as needed.


## Job Array Use Case

I have an application, app, that needs to be run against every line of my dataset. Every line changes how app runs slightly, but I need to compare the runs against each other.

Older, slower way of homogenous batch submission:

```shell
#!/bin/bash
DATASET=dataset.txt
scriptnum = 0
while read LINE; do
echo "app $LINE" > ${scriptnum}.sh
sbatch ${scriptnum}.sh
scriptnum=$(( scriptnum + 1 ))
done < $DATASET
```

Not only is this needlessly complex, it is also slow, as sbatch has to verify each job as it is submitted. This can be done easily with array jobs, as long as you know the number of lines in the dataset. This number can be obtained like so: `wc -l` dataset.txt in this case lets call it `100`.

Better way:

```slurm
#!/bin/bash
#SBATCH - - array=1-100
srun app `sed - n "${SLURM_ARRAY_TASK_ID}"` dataset.txt
```