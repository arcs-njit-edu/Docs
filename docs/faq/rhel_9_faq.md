# FAQ: RHEL8 to RHEL9 OS Upgrade

We are upgrading Wulver's operating system from RHEL8 to RHEL9 during the [September maintenance cycle](../news/posts/2025-07-29.md/#wulver-maintenance).<br>
Please review these frequently asked questions. Please contact us if you have further questions. 


??? question "What is changing on Wulver with the OS upgrade from RHEL8 to RHEL9?"
    * The cluster’s operating system is being upgraded from Red Hat Enterprise Linux 8 (RHEL8) to Red Hat Enterprise Linux 9 (RHEL9).
    * This affects system libraries, compilers, security tools, and the default environment for all users.
    * A new software stack is being deployed, replacing or upgrading many applications and modules.


??? question "What is included in the new software stack?"
    * Key libraries (e.g., GCC, OpenMPI, Python, R, etc.) and applications have been rebuilt or upgraded for RHEL9 compatibility.
    * Software compiled under RHEL8 will still be available to use at your own risk by loading the older version of foss or Intel modules However, the default path will point to the software compiled under RHEL 9. If users intend to use the older version of the software, the path will be shared upon request.
    * Up-to-date documentation and module lists will be provided—check the cluster’s software page or module system for specifics.
    * The default toolchain for newer RHEL 9 applications is `foss/2025a` and `foss/2024a` 


??? question "How do I access the new modules or software?"
    * Use the `module avail` and `module load` commands to explore new and updated software on RHEL9.
    * Some modules or software stacks may have different names, versions, or paths—review documentation.


??? question "How will the upgrade affect my jobs, software, and workflows?"
    * Jobs started on RHEL8 nodes may not continue without modification on RHEL9 nodes, especially if they rely on system libraries or modules that have changed.
    * Paths, environment variables, or application behavior may differ. Review/retest your scripts.
    * Newer versions of libraries and tools may impact software compatibility and performance.
    * If you were using software installed by the admins and available via modules, those software versions might have changed, as we have built new versions of the software against the updated compilers.
    * Users are advised to create or modify their input scripts based on the new version of the software, if required. However, if you intend to use the old version of the software (compiled under RHEL 8), please contact us and we will share the path..
    * Please note that we will not provide any support for the old versions of the software, as they have not been tested. Use them at your own risk. We will only provide support for the new software that was built with the updated compilers for RHEL 9.


??? question "How can I use software that I built or compiled on RHEL8?"
    * Direct execution is not recommended: Binaries or environments built for RHEL8 may run into compatibility issues on RHEL9 (missing libraries, ABI mismatches).
    * Best Practice: Rebuild or reinstall your software on RHEL9 when possible.
    * For critical cases:
        - **Containers**: Use Singularity/Apptainer to encapsulate your RHEL8 application and its dependencies.
        - **Compatibility Libraries**: If available, modules with compatibility libraries for RHEL8 runtime can be loaded (contact support for availability).
        - **Long-running jobs**: Jobs checkpointed under RHEL8 should ideally resume on RHEL8, or require validation/testing if resuming on RHEL9.


??? question "What about jobs that were running for a long time and need to restart after upgrade?"
    * Checkpoint/Restart: If using application-level checkpointing, confirm that your checkpoint files are forward-compatible with the new software/libraries.
    * Software upgrades may invalidate previous job states or results. Test recovery procedures in a development environment before production.
    * For critical, long-running simulations or legacy applications dependent on the RHEL8 stack, consult with the cluster support team about feasible solutions like containers or legacy compatibility modules.


### Quick tips for a smooth transition

- **Test**: Validate scripts and workflows on RHEL9 nodes before large-scale jobs.
- **Rebuild**: Prefer fresh builds/reinstalls of your applications and conda environments.
- **Stay Informed**: Monitor cluster announcements, documentation, and user forums for updates.


