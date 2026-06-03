# Wulver Maintenance Policy

ARCS HPC performs regular maintenance on Wulver and its associated storage to apply security patches, perform hardware repairs, upgrade system software, and deploy new features. This page describes the maintenance schedule, how maintenance affects users and jobs, and how notifications are handled.

## Maintenance Schedule

Wulver follows a **monthly maintenance cycle** on the **second Tuesday of every month**, from **9:00 AM to 9:00 PM (Eastern Time)**. During this window, Wulver and the associated GPFS storage are taken out of service for maintenance, repairs, patches, and upgrades.

!!! important "Regular Maintenance Window"

    - **Frequency:** Monthly
    - **Day:** Second Tuesday of every month
    - **Time:** 9:00 AM – 9:00 PM (ET)
    - **Systems affected:** Wulver compute nodes, login nodes, and GPFS storage (`/home`, `/project`, `/scratch`)

ARCS HPC reserves the right to reboot nodes once a month for maintenance on this same schedule.

## What Happens During Maintenance

During the scheduled maintenance window:

* Logins to Wulver and Open OnDemand are **disabled**.
* Users will **not have access** to their stored data in `/home`, `/project`, and `/scratch`.
* All running and queued jobs are paused; no new jobs will start.
* Data transfers to and from the cluster are unavailable.

Users will see a cluster service information message upon attempting to log in to Wulver during the maintenance window.

## How Maintenance Affects Your Jobs

The SLURM scheduler is configured with a reservation for the maintenance window. Jobs are handled as follows:

* **Jobs that complete before 9:00 AM on the maintenance day** run normally to completion.
* **Jobs whose requested walltime would overlap with the maintenance window** are held by the scheduler and shown in pending state with the reason `(ReqNodeNotAvail, Reserved for maintenance)`. They will start automatically after maintenance concludes.
* **Jobs submitted during the maintenance window** are accepted into the queue but will not start until maintenance is complete.

!!! tip "Avoid having jobs held"

    If you submit a job and notice it is held with reason *"ReqNodeNotAvail, Reserved for maintenance"*, you can either:

    - Wait until the maintenance window ends — the scheduler will start the job automatically, or
    - Cancel and resubmit the job with a shorter walltime so it finishes before maintenance begins.

    Example: A job submitted on Monday with a 2-day walltime when maintenance is scheduled for Tuesday will be held immediately because its runtime overlaps with the maintenance reservation.

For more details on the SLURM job states during maintenance, see [Managing and Monitoring Jobs](../Running_jobs/managing-jobs.md).

## Notifications

* **Routine monthly maintenance** (second Tuesday) does not require advance announcement, as the schedule is fixed and published here.
* **Any change** to the regular cycle, an **extended maintenance window**, or **emergency maintenance** will be communicated to all users via the user mailing list.
* A notification is also sent to the user mailing list when the systems are returned to service or if the maintenance window is extended into the following day(s).
* The **Message of the Day (MOTD)** displayed at login serves as a reminder for upcoming downtimes and other crucial cluster-related information. Users are encouraged to read the MOTD at every login.
* Specific upcoming and past maintenance announcements are posted at [Cluster Maintenance Updates and News](../news/index.md).

## Extended and Emergency Maintenance

ARCS HPC anticipates that regular maintenance will be completed within the scheduled window. However:

* Maintenance may occasionally finish **earlier** than scheduled, in which case the cluster is returned to service early.
* Maintenance may be **extended** into the following day(s) if issues are encountered. Users will be notified by email.
* In the case of **emergency maintenance** (e.g., critical security patches, hardware failures, or storage incidents), ARCS HPC may take Wulver out of service outside the regular maintenance window. Users will be notified as soon as possible via the user mailing list.

## User Responsibilities

* **Plan your work around the maintenance window.** Take the second-Tuesday cycle into account when scheduling jobs and when developing plans to meet research, course, or grant deadlines.
* **Choose appropriate walltimes.** If your job must complete before maintenance, request a walltime that ensures completion before 9:00 AM on the second Tuesday.
* **Do not contact the help desk** or open SNOW tickets to request access to the cluster or data during the maintenance downtime. Tickets opened during the maintenance window asking for access will not expedite the return to service.
* **Pay attention to the MOTD** and mailing list announcements for upcoming downtimes and other cluster-related information.

## Related Information

* [Cluster Maintenance Updates and News](../news/index.md) — latest maintenance announcements
* [FAQ: Maintenance](../faq/faq.md#maintenance) — frequently asked questions
* [Wulver Policies](wulver_policies.md) — full computing, storage, and job priority policies
* [Job Limitations](../Running_jobs/job_limitation.md) — limits and behavior of jobs on Wulver
