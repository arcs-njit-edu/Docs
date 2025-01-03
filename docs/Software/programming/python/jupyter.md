# Jupyter Notebooks
The Jupyter Notebook is a web-based interactive computing platform. The notebook combines live code, equations, narrative text, and visualizations. In our cluster, we have JupyterLab which is the next-generation user interface for Project Jupyter offering all the familiar building blocks of the classic Jupyter Notebook (notebook, terminal, text editor, file browser, rich outputs, etc.) in a flexible and powerful user interface. 

## Using Jupyter Notebook on Wulver

!!! warning "Jupyter Notebook via slurm on Wulver is deprecated "

    Since two-factor authentication has been implemented on Wulver, the use of Jupyter Notebook via SLURM scripts has been discontinued and is no longer supported. Users should use [OnDemand](https://ondemand.njit.edu) to use [Jupyter Notebook on Wulver](Notebook.md). First, users need to install Jupyter Notebook in their Conda environment. Once the [Conda Environment](conda.md#activate-and-deactivate-conda-environment) is activated, users can install Jupyter Notebook using the command `conda install -c conda-forge jupyter notebook`. Then, you need to specify the environment in OnDemand to start the Jupyter Notebook session. Check [here](Notebook.md) for details.

<!-- 
Users can install Jupyter Notebook on the Conda Environment. Once the [Conda Environment](conda.md#activate-and-deactivate-conda-environment) is activated users can install Jupyter Notebook via `conda install -c conda-forge jupyter notebook` command. Here we provide a sample SLURM script on how to start Jupyter Notebook session on Wulver.

??? example "Sample Batch Script to run Jupyter Notebook"

    === "Wulver"
    
        ```slurm
        #!/bin/bash -l                                                                                                                                                                                                                          
        #SBATCH --job-name=jupyter_test                                                                         
        #SBATCH --output=%x.%j.out                                                                                    
        #SBATCH --tasks-per-node=1
        #SBATCH --partition=gpu
        #SBATCH --gres=gpu:1
        #SBATCH --mem=4G
        #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
        #SBATCH --qos=standard
        #SBATCH --time=71:59:59 # D-HH:MM:SS
                                                                                                                                                                                                                                          
        ######################################                                                                                                                                                                                               
        module purge > /dev/null 2>&1
        module load wulver
        module load Anaconda3
        source conda.sh 
        conda activate ENV # Replace the name of the environment with the environment you are using. For example, if your environment is torch-cuda then use cond to activate torch-cuda
        
        port=$(shuf -i 6000-9999 -n 1)
        /usr/bin/ssh -N -f -R $port:localhost:$port login01.tartan.njit.edu
        
        cat<<EOF
        
        Jupyter server is running on: $(hostname)
        Job starts at: $(date)
        Step 1: Create SSH tunnel
        
        Open new terminal window, and run:
        (If you are off campus you will need VPN running)
        
        ssh -L $port:localhost:$port $USER@login01.tartan.njit.edu
        
        Step 2: Connect to Jupyter
        
        Keep the terminal in the previouse step open. Now open browser, find the line with
         
        Or copy and paste one of these URLs:
        
        the URL will be something like:
        
        http://localhost:${port}/?token=XXXXXXXX
        
        you should be able to connect to Jupyter Notebook running remotely on a Wulver compute node with the above url
        
        EOF
        
        jupyter notebook --no-browser --port $port --notebook-dir=$(pwd)
                     
        ```
Once you submit this job script, you will see an output file indicating the port number that you need to use to connect to Wulver in a new terminal window. Please follow further instructions from the output file.
-->

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/blob/main/CONTRIBUTING.md).
