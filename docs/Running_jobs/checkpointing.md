## Overview

Checkpointing is the process of saving the current state of a running job at regular intervals so that it can be resumed later from that state, rather than starting from scratch. This is especially useful in long-running or resource-intensive tasks on HPC systems like Wulver, where interruptions or failures may occur.

Checkpointing typically involves:

- Periodic saving of application state (memory, variables, file handles, etc.)
- Resuming computation from the last saved state
- Integration with SLURM job re-submission or recovery workflows

## Why Use Checkpointing?

| Benefit | Description |
|--------|-------------|
| **Failure Recovery** | Resume jobs from the last checkpoint after a node crash or time expiration. |
| **Efficient Resource Use** | Prevents waste of computation time on long jobs that are interrupted. |
| **Preemption Tolerance** | Helps tolerate job preemption on shared clusters or spot instances. |
| **Job Time Limit Bypass** | Breaks large jobs into smaller chunks to fit within SLURM time limits. |


## Examples for checkpointing

=== "Python"

    Save intermediate state using Python’s built-in `pickle` module — ideal for lightweight scripts.

    ```python
    import pickle
    import time

    def save_checkpoint(data, filename="checkpoint.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(data, f)

    def load_checkpoint(filename="checkpoint.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return {"iteration": 0}

    state = load_checkpoint()
    for i in range(state["iteration"], 1000):
        # Do some work
        time.sleep(1)
        print(f"Running step {i}")
        
        # Save progress every 100 steps
        if i % 100 == 0:
            save_checkpoint({"iteration": i})

    ```

=== "Pytorch"

    A common practice in PyTorch to checkpoint model weights, optimizer state, and epoch index — useful for training recovery.    

    ```python
    import torch

    # Save checkpoint
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict()
    }, 'checkpoint.pth')

    # Load checkpoint
    checkpoint = torch.load('checkpoint.pth')
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    ```

=== "Tensorflow"

    Using Keras callbacks, checkpoints are saved automatically during training. Only model weights are saved to keep storage efficient.

    ```python
    import tensorflow as tf

    model = tf.keras.models.Sequential([...])
    checkpoint_path = "checkpoints/model.ckpt"
    checkpoint_cb = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                    save_weights_only=True,
                                                    save_freq='epoch')

    model.fit(data, labels, epochs=10, callbacks=[checkpoint_cb])
    ```

=== "C/C++"

    In C/C++, you can implement basic checkpointing by writing a loop index or state to a file and loading it at the next run. Ideal for simple simulations or compute-intensive loops.

    ```cpp
    int main() {
        int current_step = load_checkpoint("state.dat"); // Custom function
        for (int i = current_step; i < MAX; i++) {
            // Work
            if (i % 1000 == 0) {
                save_checkpoint(i, "state.dat");
            }
        }
    }
    ```

=== "GROMACS"
    
    GROMACS supports checkpointing with `.cpt` files during molecular simulations:

    ```shell
    gmx mdrun -deffnm simulation -cpt 15  # Saves checkpoints every 15 minutes

    # Restart from checkpoint
    gmx mdrun -s topol.tpr -cpi simulation.cpt
    ```

=== "LAMMPS"

    LAMMPS checkpointing is usually done using `write_restart` and `read_restart`:

    ```lammps
    write_restart restart.equilibration

    # In a new job
    read_restart restart.equilibration
    ```

=== "OpenFOAM (CFD)"

    Checkpointing is done by writing time steps to disk and restarting from a previous time directory:

    ```shell
    # Set in controlDict
    writeInterval   100;

    # Restart
    startFrom       latestTime;
    ```
