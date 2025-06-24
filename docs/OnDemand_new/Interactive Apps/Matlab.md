# MATLAB

## Overview

We have three different ways to connect Matlab: 

* Matlab VNC
* Matlab Server
* Jupyter Matlab Proxy

![matlab.png](../../assets/ondemand_new/matlab/matlab-dropdown.png){ width=30% height=30%}

## Guide

=== "Matlab VNC"

    ## Launching MATLAB

    * Navigate to the Interactive Apps section.
    * Select `MATLAB` from the list of available applications.

    ## Loading the Matlab Version 

    * Select the dropdown option in `MATLAB Version`. The current versions installed on Wulver are `2023a` and `2024a`

    ![matlab-vnc-1](../../assets/ondemand_new/matlab/matlab-vnc-1.png){ width=60% height=60%}

    ## Configuring Resources

    * Specify your Slurm account/partition/qos.
    * Set the maximum wall time requested.
    * Choose the number of cores you need.
    * If required, specify the number of GPUs.

    ![matlab-vnc-1](../../assets/ondemand_new/matlab/matlab-vnc-2.png){ width=60% height=60%}

    ![matlab-vnc-3](../../assets/ondemand_new/matlab/matlab-vnc-3.png){ width=60% height=60%}

    ![matlab-vnc-4](../../assets/ondemand_new/matlab/matlab-vnc-4.png){ width=60% height=60%}

    ## Launching the Session

    * Select the `Launch` option after finalizing the resources. Once clicking **Launch**, the request will be queued, and when resources have been allocated, you will be presented with the option to connect to the session by clicking on the blue `Launch MATLAB` option.

    ![matlab-vnc-5](../../assets/ondemand_new/matlab/matlab-vnc-5.png){ width=60% height=60%}

    ![matlab-vnc-6](../../assets/ondemand_new/matlab/matlab-vnc-6.png){ width=60% height=60%}

    * You might see `Unable to contact settings server` message. It does not mean the Matlab session is terminated. You need to wait a few minutes to see the Matlab popup window.


    ![matlab-vnc-7](../../assets/ondemand_new/matlab/matlab-vnc-7.png){ width=60% height=60%}

    ![matlab-vnc-8](../../assets/ondemand_new/matlab/matlab-vnc-8.png){ width=60% height=60%}

    ![matlab-vnc-9](../../assets/ondemand_new/matlab/matlab-vnc-9.png){ width=60% height=60%}

=== "Matlab Server"

    * Select Matlab Server from the interactive apps dropdown menu. 
    
    * Fill in your configurations based on your job requirements

    ![matlab-server-1.png](../../assets/ondemand_new/matlab/matlab-server-1.png){ width=60% height=60%}

    * Wait for the job to start and then click on **Connect to Matlab**

    ![matlab-server-2.png](../../assets/ondemand_new/matlab/matlab-server-2.png){ width=60% height=60%}

    * Select existing License

    ![matlab-license-1.png](../../assets/ondemand_new/matlab/matlab-license-1.png){ width=40% height=40%}

    * Click **Start Matlab** 

    ![matlab-license-2.png](../../assets/ondemand_new/matlab/matlab-license-2.png){ width=40% height=40%}

    * Wait for couple minutes

    ![matlab-license-3.png](../../assets/ondemand_new/matlab/matlab-license-3.png){ width=40% height=40%}

    * Start working!!

    ![matlab-start-working.png](../../assets/ondemand_new/matlab/matlab-start-working.png){ width=60% height=60%}

=== "Jupyter Matlab Proxy"

    Check our video tutorial [here](../../assets/ondemand_new/matlab/Matlab_OnDemand_Tutorial_Server.mp4)

    * Select **Jupyter-matlab-proxy** from the dropdown menu.
    
    * Choose matlab-proxy as conda env

    ![conda-env-matlab-proxy.png](../../assets/ondemand_new/matlab/jupyter-matlab-proxy-1.png){ width=60% height=60%}

    * Fill the rest of the form based on your desired configurations and click Launch. Wait for couple of seconds (same way as other matlab servers)

    * Once the Jupyter opens, click on Open Matlab

    ![conda-env-matlab-proxy.png](../../assets/ondemand_new/matlab/jupyter-matlab-proxy-2.png){ width=60% height=60%}

    * Select existing License

    ![matlab-license-1.png](../../assets/ondemand_new/matlab/matlab-license-1.png){ width=40% height=40%}

    * Click start Matlab

    ![matlab-license-2.png](../../assets/ondemand_new/matlab/matlab-license-2.png){ width=40% height=40%}

    * Wait for couple minutes

    ![matlab-license-3.png](../../assets/ondemand_new/matlab/matlab-license-3.png){ width=40% height=40%}

    * Start working!!

    ![matlab-start-working.png](../../assets/ondemand_new/matlab/matlab-start-working.png){ width=60% height=60%}



