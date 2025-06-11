---
title: VS Code
---
Visual Studio Code (often abbreviated as VS Code) is an Integrated Development Environment (IDE). It is a lightweight and highly extensible code editor developed by Microsoft. Although referred to as a code editor, VS Code offers many features. One of the important feature of VS Code is an integrated terminal that allows developers to execute commands, run scripts, and interact with the command-line interface without leaving the editor. VS Code also provides Git integration, enabling developers to manage version control operations, such as committing, branching, and merging, without switching to a separate Git client. 

## Availability
VS Code is not installed on the cluster. To use VS Code, you need to install it on your computer and connect remotely to the cluster using NJIT VPN.

## Application Information, Documentation
The documentation of VS Code is available at [VS Code documentation](https://code.visualstudio.com/docs). You can download the VS Code from [VS Code download page](https://code.visualstudio.com/Download)

## Using VS Code on Cluster

!!! warning

    If you want to use VS Code on NJIT cluster, don't use VS Code installed on your machine to connect to cluster! Please use the method described belelow so that you can use VS Code not only to edit scripts, but also run your script on the cluster.

Use the following slurm script and submit the job script using `sbatch vs-code.submit.sh` command.

??? example "Batch Script to use VS Code : vs-code.submit.sh"
        
    ```slurm
    #!/bin/bash -l
    #SBATCH --job-name=vs-code
    #SBATCH --output=%x.%j.out # %x.%j expands to slurm JobName.JobID
    #SBATCH --error=%x.%j.out # prints the error message
    #SBATCH --partition=general 
    #SBATCH --nodes=1
    #SBATCH --ntasks-per-node=32
    #SBATCH --mem-per-cpu=4000M # Maximum allowable mempry per CPU 4G
    #SBATCH --qos=standard
    #SBATCH --account=PI_ucid # Replace PI_ucid which the NJIT UCID of PI
    #SBATCH --time=71:59:59  # D-HH:MM:SS
    
    set -e
    
    module purge
    module load wulver # load slurn, easybuild
    
    # add any required module loads here, e.g. a specific Python
    
    CLI_PATH="${HOME}/vscode_cli"
    
    # Install the VS Code CLI command if it doesn't exist
    if [[ ! -e ${CLI_PATH}/code ]]; then
        echo "Downloading and installing the VS Code CLI command"
        mkdir -p "${HOME}/vscode_cli"
        pushd "${HOME}/vscode_cli"
        # Process from: https://code.visualstudio.com/docs/remote/tunnels#_using-the-code-cli
        curl -Lk 'https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64' --output vscode_cli.tar.gz
        # unpack the code binary file
        tar -xf vscode_cli.tar.gz
        # clean-up
        rm vscode_cli.tar.gz
        popd
    fi

    # run the code tunnel command and accept the licence
    ${CLI_PATH}/code tunnel --accept-server-license-terms
    ```

    
Once you submit the job, you will see an output file with `.out` extension. Once you open the file, you will see the following
```
*

* Visual Studio Code Server

*

* By using the software, you agree to

* the Visual Studio Code Server License Terms (https://aka.ms/vscode-server-license)and

* the Microsoft Privacy Statement (https://privacy.microsoft.com/en-US/privacystatement).

*

To grant access to the server, please log into https://github.com/login/device and use code XXXX-XXXX

```
You need to have the [GitHub](https://www.github.com) account, please open the GitHub profile and use the code printed in the output file. Once you authorize GitHub, you will see the following in the output file

```
Open this link in your browser https://vscode.dev/tunnel/nodeXXX
```

Now copy and paste this link in your browser and VS Code is ready to use.


## Related Applications

* PyCharm

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/blob/main/CONTRIBUTING.md).


