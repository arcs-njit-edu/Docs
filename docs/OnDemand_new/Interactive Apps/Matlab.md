# MATLAB

## Overview

We have three different ways to connect Matlab: 

* Matlab VNC
* Matlab Server
* Jupyter Matlab Proxy

![matlab.png](../../assets/ondemand_new/matlab.png){ width=40% height=40%}

## Guide

=== "Matlab VNC"

    ## Launching MATLAB

    * Navigate to the Interactive Apps section.
    * Select `MATLAB` from the list of available applications.

    ## Loading the Matlab Version 

    * Select the dropdown option in `MATLAB Version`. The current versions installed on Wulver are `2023a` and `2024a`

    ![matlab1](../../assets/ondemand/matlab1.png){ width=60% height=60%}

    ## Configuring Resources

    * Specify your Slurm account/partition/qos.
    * Set the maximum wall time requested.
    * Choose the number of cores you need.
    * If required, specify the number of GPUs.

    ![matlab2](../../assets/ondemand/matlab2.png){ width=60% height=60%}

    ![matlab3](../../assets/ondemand/matlab3.png){ width=60% height=60%}

    ![matlab4](../../assets/ondemand/matlab4.png){ width=60% height=60%}

    ## Launching the Session

    * Select the `Launch` option after finalizing the resources. Once clicking **Launch**, the request will be queued, and when resources have been allocated, you will be presented with the option to connect to the session by clicking on the blue `Launch MATLAB` option.

    ![matlab5](../../assets/ondemand/matlab5.png){ width=60% height=60%}

    ![matlab6](../../assets/ondemand/matlab6.png){ width=60% height=60%}

    * You might see `Unable to contact settings server` message. It does not mean the Matlab session is terminated. You need to wait a few minutes to see the Matlab popup window.


    ![matlab7](../../assets/ondemand/matlab7.png){ width=60% height=60%}

    ![matlab8](../../assets/ondemand/matlab8.png){ width=60% height=60%}

    ![matlab9](../../assets/ondemand/matlab9.png){ width=60% height=60%}

=== "Matlab Server"

    *Same steps as matlab vnc upto launching the session*

    * Select existing License

    ![existing-license-button.png](../../assets/ondemand_new/existing-license-button.png){ width=60% height=60%}

    * Click start Matlab

    ![start-matlab-button.png](../../assets/ondemand_new/start-matlab-button.png){ width=60% height=60%}

    * Wait for couple minutes

    ![matlab-loading.png](../../assets/ondemand_new/matlab-loading.png){ width=60% height=60%}

    * Start working!!

=== "Jupyter Matlab Proxy"

    * Select matlab-proxy as conda env

    ![conda-env-matlab-proxy.png](../../assets/ondemand_new/conda-env-matlab-proxy.png){ width=80% height=80%}

    * Fill the rest of the form based on your desired configurations and click Launch. Wait for couple of seconds (same way as other matlab servers)
    * Once the Jupyter opens, click on Open Matlab

    ![jupyter-matlab-button.png](../../assets/ondemand_new/jupyter-matlab-button.png){ width=80% height=80%}

    * Then select existing license, wait for couple of minutes and matlab will start. *Same license steps as matlab server*

    * Start working!!



