# Use MATLAB on NJIT HPC

!!! warning
    
    Please note that the following instructions are applicatible for Lochness only. We will soon update the instructions for Wulver.

## Installation steps of MATLAB on local machine
* Go to [Mathworks Download](https://www.mathworks.com/downloads/) and register with your NJIT email address.
* Select the **R2022a** version to download. 
* User needs to select the correct installer based on the OS (Mac or Windows). 
* Run the installer.

   ![matlab_install1](img/matlab_installation_1.png){ width=50% height=50%}
   ![matlab_install1](img/matlab_installation_2.png){ width=50% height=50%}

* Make sure to check **Parallel Computing Toolbox** option.
   
   ![matlab_install3](img/matlab_installation_3.png){width=50% height=50%}

* Continue by selecting **Next** and MATLAB will be installed on your computer.

## Setup Slurm profile to run MATLAB on Lochness
Following this procedure a user will be able to submit jobs to lochness or stheno from Matlab running locally on the user's computer.

### Installing the Add-On

From the Matlab window, click on "Add-ons" and select "Get Add-Ons."

   ![matlab_addon1](img/ClickOnAddons.png){ width=70% height=70%}

In the search box enter "slurm" and click on the magnifying glass icon. Select "Parallel Computing Toolbox plugin for MATLAB Parallel Server with Slurm". Alternatively, this Add-On can be downloaded directly from the [Mathworks](https://www.mathworks.com/matlabcentral/fileexchange/52807-parallel-computing-toolbox-plugin-for-matlab-parallel-server-with-slurm) site.
   
   ![matlab_slurm](img/SlurmAddOn.png){ width=70% height 70%}

Click on "Install."

![matlab_addons_install](img/ClickOnInstall.png){ width=70% height 70%}

### Creating a Profile for Lochness or Stheno

The following steps will create a profile for lochness (or stheno). Click <kbd>Next</kbd> to begin.

![matlab_profile1](img/GenericProfile1.png){ width=50% height 50%}

In the "Operating System" screen `Unix` is already selected. Click <kbd>Next</kbd> to continue.

![matlab_profile2](img/GenericProfile2.png){ width=50% height 50%}

This "Submission Mode" screen determines whether or not to use a `shared` or `nonshared` submission mode. Since Matlab installed on your personal computer or laptop does not use a shared job location storage, select "No" where indicated and click <kbd>Next</kbd> to continue.

![matlab_profile3](img/GenericProfile3.png){ width=50% height 50%}

Click <kbd>Next</kbd> to continue.

![matlab_profile4](img/GenericProfile4.png){ width=50% height 50%}

In the "Connection Details" screen, enter the cluster host, either "lochness.njit.edu" or "stheno.njit.edu." Enter your UCID for the username. Select "No" for the "Do you want to use an identity file to log in to the cluster" option and click next to continue.

![matlab_profile5](img/GenericProfile5.png){ width=50% height 50%}

In the "Cluster Details" screen enter the full path to the directory on lochness to store the Matlab job files. In the case the directory is $HOME/MDCS. MDCS stands for Matlab Distributed Computing Server. It is not necessary to name this directory MDCS. This directory can be named anything you wish. To determine the value of $HOME, logon to lochness. For details on how to log on to Lochness from local computer please see [Cluster Access](cluster_access.md). Once connected to Lochness run the following:

```
  login-1-45 ~ >: echo $HOME
  /home/g/guest24
```

Make sure to check the box <kbd>Use unique subfolders</kbd> . Click <kbd>Next</kbd> to continue.

![matlab_profile6](img/GenericProfile6.png){ width=50% height 50%}

In the "Workers" screen enter `512` for the number of workers and `/opt/site/easybuild/software/MATLAB/2022a` for `MATLAB installation folders for workers`. Click <kbd>Next</kbd> to continue.

![matlab_profile7](img/GenericProfile7.png){ width=50% height 50%}

In the "License" screen make sure to select "Network license manager" and click <kbd>Next</kbd> to continue.

![matlab_profile8](img/GenericProfile8.png){ width=50% height 50%}

In the "Profile Details" screen enter either "Lochness" or "Stheno" depending on which cluster you are making a profile for. The "Cluster description" is optional and may be left blank. Click <kbd>Next</kbd> to continue.

![](https://wiki.hpc.arcs.njit.edu/images/4/4d/GenericProfile9.png){ width=50% height 50%}

In the "Summary" screen make sure everything is correct and click "Create."

![matlab_profile10](img/GenericProfile10.png){ width=50% height 50%}

In the "Profile Created Successfully" screen, check the "Set the new profile as default" box and click on "Finish."

![](https://wiki.hpc.arcs.njit.edu/images/b/b8/GenericProfile11.png){ width=50% height 50%}

## Submitting a Serial Job
This section will demonstrate how to create a cluster object and submit a simple job to the cluster. The job will run the 'hostname' command on the node assigned to the job. The output will indicate clearly that the job ran on the cluster and not on the local computer.

The hostname.m file used in this demonstration can be downloaded [here](https://www.mathworks.com/matlabcentral/fileexchange/24096-hostname-m).

```
 >> c=parcluster 
```
 ![](https://wiki.hpc.arcs.njit.edu/images/2/22/C%3Dparcluster_1.png){ width=70% height 70%}

Certain arguments need to be passed to SLURM in order for the job to run properly. Here we will set values for partion, mem-per-cpu and time. In the Matlab window enter:
```
 >> c.AdditionalProperties.AdditionalSubmitArgs=['--partition=public --mem-per-cpu=10G --time=2-00:00:00'] 
```
To make this persistent between Matlab sessions these arguments need to be saved to the profile. In the Matlab window enter:
```
 >> c.saveProfile 
```
 ![](https://wiki.hpc.arcs.njit.edu/images/5/51/AdditionalArguments.png){ width=70% height 70%}
 
We will now submit the hostname.m function to the cluster. In the Matlab window enter the following:
```
>> j=c.batch(@hostname, 1, {}, 'AutoAddClientPath', false); 
```
@: Submitting a function.\
1: The number of output arguments from the evaluated function.\
{}: Cell array of input arguments to the function. In this case empty.\
'AutoAddClientPath', false: The client path is not available on the cluster.


When the job is submitted, you will be prompted for your password.

For more information see the Mathworks page: [batch](https://www.mathworks.com/help/parallel-computing/batch.html) 

![](https://wiki.hpc.arcs.njit.edu/images/6/6a/BatchEnterPasswd.png){ width=70% height 70%}

To wait for the job to finish, enter the following in the Matlab window:
```
 >>j.wait
```
Finally, to get the results:
```
 >>fetchOutputs(j)
```
As can be seen, this job ran on node720

![](https://wiki.hpc.arcs.njit.edu/images/e/e5/BatchHostname.png){ align=left, width=70% height 70%}

### Submitting a Parallel Function
The "Job Monitor" is a convenient way to monitor jobs submitted to the cluster. In the Matlab window select "Parallel" and then "Monitor Jobs."

For more information see the Mathworks page: [Job Monitor](https://www.mathworks.com/help/parallel-computing/job-monitor.html)

![](https://wiki.hpc.arcs.njit.edu/images/c/c4/MonitorJobs.png){ width=70% height 70%}

Here we will submit a simple function using a "parfor" loop. The code for this example is as follows:
```
function t = parallel_example

t0 = tic;
parfor idx = 1:16
        A(idx) = idx;
        pause (2)
end

t=toc(t0);
```
To submit this job:
```
 >> j=c.batch(@parallel_example, 1, {}, 'AutoAddClientPath', false, 'Pool', 7)
```
Since this is a parallel job a 'Pool' must be started. The actual number of tasks started will be one more than requested in the pool. I this case, the batch command calls for a pool of seven. Eight tasks will be started on the cluster.

Also see that the state of the job in the "Job Monitor" is "running."
![](https://wiki.hpc.arcs.njit.edu/images/d/db/SubmitParallel.png){ width=70% height 70%}

The job takes a few minutes to run and the state of the job changes to "finished."
![](https://wiki.hpc.arcs.njit.edu/images/0/0f/JobFinished.png){ width=70% height 70%}

Once again to get the results enter:
```
 >> fetchOutputs(j) 
```
As can be seen the parfor loop was completed in 6.7591 seconds.
![](https://wiki.hpc.arcs.njit.edu/images/7/7d/FetchOutputs.png){ width=70% height 70%}

## Submitting a Script Requiring a GPU
In this section we will submit a matlab script using a GPU. The results will be written to the job diary. The code for this example is as follows:
```
% MATLAB script that defines a random matrix and does FFT
%
% The first FFT is without a GPU
% The second is with the GPU
%
% MATLAB knows to use the GPU the second time because it
%   is passed a type gpuArray as an argument to FFT
% We do the FFT a bunch of times to make using the GPU worth it,
%   or else it spends more time offloading to the GPU
%   than performning the calculation
%
% This example is meant to provide a general understanding
%   of MATLAB GPU usage
% Meaningful performance measurements depend on many factors
%   beyond the scope of this example
% Downloaded from https://projects.ncsu.edu/hpc/Software/examples/matlab/gpu/gpu_m

% Define a matrix
A1 = rand(3000,3000);

% Just use the compute node, no GPU
tic;
% Do 1000 FFT's
for i = 1:1000
      B2 = fft(A1);
end
time1 = toc;
fprintf('%s\n',"Time to run FFT on the node:")
disp(time1);

% Use GPU
tic;
A2 = gpuArray(A1);
% Do 1000 FFT's
for i = 1:1000
      % MALAB knows to use GPU FFT because A2 is defined by gpuArray
        B2 = fft(A2);
end
time2 = toc;
fprintf('%s\n',"Time to run FFT on the GPU:")
disp(time2);

% Will be greater than 1 if GPU is faster
speedup = time1/time2 
```
We will need to change the partition to datasci and request a gpu. In the Matlab window enter:
```
 >> c.AdditionalProperties.AdditionalSubmitArgs=['--partition=datasci --gres=gpu:1 --mem-per-cpu=10G --time=2-00:00:00'] 
```
![](https://i.imgur.com/md8jfxI.jpg)

Submit the job as before. Since a script is submitted as opposed to a function, only the name of the script is included in the batch command. Do not include the '@' symbol. In a script there are no inputs or ouptuts.
```
 >> j=c.batch('gpu', 'AutoAddClientPath', false) 
```
 ![](https://wiki.hpc.arcs.njit.edu/images/8/8d/GpuSubmit.png){ width=70% height 70%}
 
To get the result:
```
 >> j.diary 
```
![](https://wiki.hpc.arcs.njit.edu/images/4/4a/GpuDiary.png){ width=70% height 70%}

## Load and Plot Results from A Job
In this section we will run a job on the cluster and then load and plot the results in the local Matlab workspace. The code for this example is as follows:
```
n=100;
disp("n = " + n);
A = gallery('poisson',n-2);
b = convn(([1,zeros(1,n-2),1]'|[1,zeros(1,n-1)]), 0.5*ones(3,3),'valid')';
x = reshape(A\b(:),n-2,n-2)';%
```
As before submit the job:
```
 >> j=c.batch('plot_demo', 'AutoAddClientPath', false);
```
![](https://wiki.hpc.arcs.njit.edu/images/d/d4/PlotDemoSub.png){ width=70% height 70%}

To load 'x' into the local Matlab workspace:
```
 >> load(j,'x') 
```
 ![](https://wiki.hpc.arcs.njit.edu/images/2/26/Load_x.png){ width=70% height 70%}
 
 Finally, plot the results:
```
 >> plot(x) 
```
![](https://wiki.hpc.arcs.njit.edu/images/9/90/Plot_x.png){ width=70% height 70%}
 