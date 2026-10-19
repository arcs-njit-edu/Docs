# Wulver Status and Usage

These dashboards show the live state of Wulver and how it has been used over time. They are updated automatically.

!!! warning "Network requirements: on-campus or VPN only"

    The status dashboards can only be reached from the NJIT network. You must either:

    * be connected to the NJIT campus network (wired or the campus Wi-Fi), or
    * be connected to the [NJIT VPN](https://ist.njit.edu/vpn) if you are off campus.

    If you open one of the links below from any other network, the page will not load. Depending on your browser, you may see an error such as **"This site can't be reached"**, **"ERR_CONNECTION_TIMED_OUT"**, or **"The connection has timed out"**. This does not mean the dashboards are down. Connect to the VPN and reload the page.

## [Current Load](https://hpc.njit.edu/Monitor/load.html)
A near real-time view of the cluster. Use it to see how busy Wulver is before submitting jobs, or to check why a job is still pending.

* Node status and current CPU, GPU, and memory usage
* Per-node usage for A100, L40, and MIG GPUs
* Running and pending jobs, queue status, and queue history
* QOS summaries for CPU and GPU jobs

## [Resource Usage Summary](https://hpc.njit.edu/Monitor/summary.html)
A high-level overview of Wulver usage since it went into service.

* Number of active users, PIs, and departments
* Total jobs and CPU hours
* Usage split by partitions (gpu, bigem, general)
* A cost comparison against running the same workload on AWS

## [Resource Usage (this year so far)](https://hpc.njit.edu/Monitor/cy2026.html)
A detailed report of usage for the current calendar year.

* Usage and number of jobs by college, department, and QOS
* CPU vs. GPU usage
* Breakdown by job type (serial, SMP, and DMP)
* Usage by courses

## [Application Usage](https://hpc.njit.edu/Monitor/modules.html)
Shows which software modules are loaded most often on Wulver. Use it to see which applications are popular across the user community.
