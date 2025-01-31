# FAQs

Welcome to our most frequently asked questions. If you cannot find an entry related to your question, please [contact us](contact.md), and we will add it.

## Login Issues / Access

??? question "How do I get access to the Wulver HPC cluster?"
    * If you are a student or researcher, your research/faculty advisor will need to request an account on your behalf. 
    * If you are a faculty member, then you can directly email us at hpc@njit.edu for an account.
    * For individuals non affiliated with NJIT have to contact a faculty member in NJIT to sponsor you a guest account
    * If you are taking a course that requires computation on Wulver please ask your course instructor to email hpc@njit.edu to request access for the students.
    * For detail information please click [here](cluster_access.md).

??? question "How do I connect to the Wulver HPC cluster?"
    * For detail information please click [here](cluster_access.md).

??? question "Why can’t I log in to the HPC?"
    - It’s possible that your account is not activated on Wulver. Make sure to follow the instructions in [How do I get access to the Wulver HPC cluster?](). Once your account is created, you will receive a confirmation in your NJIT email.
    - Ensure that your UCID and password are correct.
    - If you are working off-campus, make sure to connect to NJIT VPN before logging into Wulver. Visit https://ist.njit.edu/vpn for more information on VPN installation.

??? question "Why is my password not showing in the terminal when I type?"
    - The Command Line Interface hides passwords as you type to protect against visual exposure and enhance security.

??? question "Why am I getting “permission denied” ?"
    - You might not have access to the HPC yet. For requesting access, please check our [user access](cluster_access.md).
    - Your instructor/PI might not have added you into the group yet.
    - Cluster might be having downtime due to maintenance or other reasons.

??? question "How do I transfer data to and from the HPC cluster?"
    - Detailed instructions are given  [here](cluster_access.md#transfer-the-data-from-the-local-machine-to-clusters-or-vice-versa).

??? question "What security measures should I be aware of when using the HPC cluster?"
    - Do not share your login information with anyone else or allow anyone to login with your account.

??? question "Which directory will I land on when I login?"
    - You will enter into your home directory named under your UCID.
    - Please note that you are on the login node of Wulver. Do not run any computations on the login nodes, as CPU and memory usage are limited per user on these nodes. To perform computations, you need to request resources from the compute nodes via [SLURM](slurm.md).

## File Systems / Storage

??? question "What are the different file storage systems available on Wulver?"
    - Please visit our [file system](Wulver_filesystems.md) page for detailed information. 

??? question "How can I get more storage?"
    - When your account is active on Wulver, you will have access to following file systems
        - **$HOME** directory - Default quota of 50GB per user and cannot be increased
        - **/project** - Default quota of 2TB per PI group and can be increased by purchasing additional storage at $200/TB for 5 years.
        - **/scratch** - No quota but files will be deleted after 30 days or sooner if the directory reaches 80% capacity. Users will be notified prior to deletion so they can review and move important files to `/project` if necessary.
    - For more details, visit [file system](Wulver_filesystems.md).

??? question "I have an error “disk quota exceeded” while running a job, how can I solve this error?"
    - First, check which filesystem is causing the error. If it’s in `$HOME`, it means the 50GB quota has been exceeded. You can either delete files, compress them, or move them to `/project`. If the error is in `/project`, you need to compress or delete some files. Alternatively, you can ask your PI to purchase an increase  in the `/project` quota by emailing us at hpc@njit.edu. You can also run your code in `/scratch` and, after the simulation, transfer the important files to `/project`. 
    - Use `quota_info` command to check the filesystem quota. 
    - If you are encountering this error while running Python or Jupyter Notebook via Conda, the issue is likely due to Conda packages or cache files stored in `$HOME`. Use the ```sn p $HOME``` command to view a detailed breakdown of each directory in $HOME, showing how much space it is consuming. If you notice that the `.cache` directory is consuming a significant amount of space, you should remove it. If the `.conda` directory is taking up too much space, you need to move the Conda environment to `/project`. Refer to [this guide](conda.md#importing-to-a-different-location) for detailed steps. 

??? question "What is `/scratch` used for?"
    - Run your code in `/scratch` and, after the simulation, transfer the important files to `/project`. 
    - **NB** : This space is not backed up; files will be deleted after 30 days.

## Jobs and scheduling

??? question "How do I submit and manage jobs on the Wulver HPC cluster?"
    - We use the SLURM resource manager and scheduler on Wulver for submitting and managing jobs on the compute nodes. 
    - Check our [SLURM page](slurm.md) on the website for more detailed guidance.

??? question "What is Walltime?"
    - Walltime refers to the maximum amount of real-world time a job is allowed to run on the cluster. The actual job may finish earlier. 
    - To set the walltime, you'll typically specify it in the job submission script: 
    ```bash
    #SBATCH --time=01:00:00      # Request 1 hour of walltime
    ```

??? question "How can I monitor the status of my jobs?"
    - For checking and monitoring the status of your job please use [this](slurm.md#managing-and-monitoring-jobs) guide for detailed information.

??? question "Where does my output will appear after I submit a job?"
    - Your output will appear in the file which you initialized in your job script which look like below:
    ```bash
    #SBATCH --output=file_name.%j.out # %j expands to slurm JobID
    ```
    - By default, this file is in the same directory as the job script, unless you specify the working directory via `sbatch`

??? question "How can I see the status of the cluster?"
    - For checking the cluster load use this [link](https://hpc.njit.edu/Monitor/load.html)

## Maintenance

??? question "When does maintenance occur?"
    - Second Tuesday 9AM - 9PM monthly.

??? question "I submitted my job before maintenance, but why did it go to pending status as *"ReqNodeNotAvail, Reserved for maintenance"* ?"
    - If your job walltime request indicates the job will not finish before the maintenance starts then the scheduler will hold the job.  
    - If you resubmit the job with a shorter walltime, it will not be held. 
    - For example: If you submit a job on Monday with a walltime of 2 days and maintenance is scheduled on Tuesday then your job overlaps with the maintenance schedule. Hence, SLURM will immediately put it on hold until the maintenance is completed and start it later.

??? question "How will maintenance affect me?"
    - During the maintenance downtime, logins will be disabled, users will not have access to their stored data in `/project`, `/home` and `/scratch`.
    - All jobs that do not end **before 9AM** will be held by the scheduler until the downtime is complete and the systems are returned to service.

??? question "Will I receive a notification before maintenance?"
    - Our regular monthly maintenance cycle is every 2nd Tuesday. If there is a change to this cycle, all users will receive notification.

??? question "What happens to my jobs during maintenance?"
    - Jobs queued just before the maintenance will be held in **Pending State** and then later gets continued.

## Software and Hardware Specifications

??? question "Is there any installed software?"
    - We have a variety of software packages already installed on Wulver.
    - For more information, please visit our [Software guide](../Software/index.md).

??? question "I want to install new software?"
    - Please first check our already installed [software list](../Software/index.md#software-list), and if you still don’t find it then visit our [guide](../Software/index.md) for detailed guidance on software installation.

??? question "What are the hardware specifications of the Wulver HPC cluster?"
    - Please check out our [Wulver](wulver.md) page for complete details on hardware specifications.

??? question "What programming languages are commonly used on the HPC cluster?"
    - Most common ones are C, C++, Fortran, Python, R

??? question "What are the tools and compilers available on HPC cluster?"
    - Common programming tools include Intel and GNU compilers as well as MPI for multi-node jobs.
    - For GPU acceleration we have CUDA and OpenACC.
    - Details on these resources are available [here](compilers.md).

??? question "How can I optimize my code for parallel processing?"
    - To optimize your code, you can use different parallelization techniques depending on your setup:
        - **MPI** and **OpenMP** for parallelizing code and then specifying the cores.
        - **CUDA** and **OpenACC** for GPU acceleration, especially for compute-heavy tasks.
    - Focus on optimizing **CPU**, **I/O**, **memory**, and **parallelism**.
    - If you have specific questions about this, please email HPC Help at [hpc@njit.edu](mailto:hpc@njit.edu) to request support.

??? question "Can I request additional resources or customization for my projects?"
    - Please see [Wulver Usage and Condo Policy](wulver_policies.md) for resource allocation details. 
    - The Research Computing Advisory Board is working on establishing policies and procedures for requesting additional computing time beyond the standard **300K SU/year**.

??? question "My software requires a license, how should I proceed?"
    - License is purchased by the user and his/her department.
    - Please visit the software’s documentation for your specific software.

## Miscellaneous

??? question "What documentation and support resources are available for Wulver users?"
    - Please visit the [Education and Training tab](../HPC Events and Workshops/Calendar/index.md) on our website.
    - If you have any specific questions which are not covered, please contact us at [hpc@njit.edu](mailto:hpc@njit.edu)





    