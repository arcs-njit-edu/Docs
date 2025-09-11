## Overview

In many workflows, one job must start only after another has successfully completed. For example, you might want to:

- Preprocess data in one job and then analyze it in another
- Run a simulation, then run a visualization job
- Compile a program, and then run the executable

Slurm allows you to chain jobs together using job dependencies, so that one job begins only when the specified condition on another job is met.

This avoids manual tracking and reduces errors in job sequencing.

## Job Dependency Options

| Dependency Type                       | Description |
|---------------------------------------|-------------|
| `after:job_id[:job_id...]`            | This job can begin execution **after the specified jobs have started**. |
| `afterany:job_id[:job_id...]`         | This job can begin execution **after the specified jobs have terminated**, regardless of state. |
| `afterburstbuffer:job_id[:job_id...]` | This job starts **after the specified jobs have terminated** and any associated **burst buffer stage-out operations** are complete. |
| `afternotok:job_id[:job_id...]`       | This job starts **only if the specified jobs fail** (non-zero exit code, node failure, timeout, etc). |
| `afterok:job_id[:job_id...]`          | This job starts **only if the specified jobs succeed** (exit code 0). |
| `aftercorr:job_id`                    | Each task in this job array will start **after the corresponding task ID** in the specified job has completed successfully. |
| `singleton`                           | This job will only start **after any previous jobs with the same name and user have finished**. |

## Job Dependency Examples

**Run Second Job After First Job Completes Successfully**

```shell
# Submit first job
$ sbatch preprocess.sh
Submitted batch job 12345
```

```shell
# Submit dependent job (afterok = only if first job succeeds)
$ sbatch --dependency=afterok:12345 analyze.sh
Submitted batch job 12346
```

In this example:

- `12345` is the job ID of the first job.
- The second job will start only if preprocess.sh exits with code 0 (success).

**Chaining Multiple Jobs**

```shell
# Submit step 1
$ sbatch step1.sh          # returns JobID 11111

# Submit step 2 to run after step 1
$ sbatch --dependency=afterok:11111 step2.sh   # returns JobID 11112

# Submit step 3 to run after step 2
$ sbatch --dependency=afterok:11112 step3.sh
```
