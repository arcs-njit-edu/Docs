---
title: Requesting an Account on Wulver
---

# Requesting an Account on Wulver

Every account on Wulver is sponsored by NJIT faculty. This page explains **who has to send the request**, **what to include in it**, and **what happens after it is submitted**, for research groups, courses, and external collaborators.

!!! info "Summary"

    Requests for an account must come from a faculty advisor or PI by emailing [hpc@njit.edu](mailto:hpc@njit.edu) with the UCIDs of the accounts to be created. Students may write to us first, but the account is created only after the advisor confirms.

## Who Sends the Request

=== "Faculty / PI"

    Email [hpc@njit.edu](mailto:hpc@njit.edu) directly. Your own account and your group allocation are set up together.

    #### What to Include in the Request

    * **UCID for each person** — the short NJIT username such as `ab123`. A nine-digit student ID number cannot be used to create an account.
    * **The PI or group account** the usage should be charged to.
    * **A one-line description of the work** the account is for.
    * **Software the user expects to need**, so we can confirm what is already available in the [module stack](../Software/index.md).

=== "Student / Postdoc / Lab member"

    Ask your faculty advisor to email [hpc@njit.edu](mailto:hpc@njit.edu) approving your access and naming the group account your jobs should be charged to.

    If you write to us first, add your advisor to the email so they can reply and confirm in the same thread.

    #### What to Include in the Request

    * **UCID for each person** — the short NJIT username such as `ab123`. A nine-digit student ID number cannot be used to create an account.
    * **The PI or group account** the usage should be charged to.
    * **A one-line description of the work** the account is for.
    * **Software the user expects to need**, so we can confirm what is already available in the [module stack](../Software/index.md).

    !!! warning "Most common delay"

    A student emails us without their advisor on the request. We reply asking the student to have their PI contact us, which adds days to the process. Students should copy their faculty advisor on the first email.

=== "Course"

    The **course instructor** submits the request, including the UCIDs of the students who need accounts.

    [HPC Course Request Form](https://nexus.njit.edu/highlander_nexus?id=sc_cat_item&sys_id=cd6eaea13b97e210e914eb0864e45a7f){ .md-button }

    See [HPC Resources for Teaching & Coursework](../Courses/index.md) for what a course account includes.

    #### What to Include in the HPC Course Request Form

    * **UCID for each person** — the short NJIT username such as `ab123`. A nine-digit student ID number cannot be used to create an account.
    * **Instructor** — the UCID of the course instructor the usage is charged to.
    * **Allocations per student** — the default is 2500 Service Units per student; see [Service Units](../Courses/course-resource-config.md#service-units) for details. The default storage allocation per user is 100 GB. For more than the default, include a justification in "Description of Course Activities".
    * **Software the user expects to need**, so we can confirm what is already available in the [module stack](../Software/index.md).

    #### Account Lifetime and Data Retention

    | | |
    |---|---|
    | Account lifetime | Through the end of the semester |
    | Data retention | Course data remains readable for one year after the course ends |
    | Course directory | Each student is assigned a directory under `/course/<year>/<semester>/<course>/<instructor_ucid>/<student_ucid>` |

    !!! note

        The course directory path is emailed to each student along with their account
        information. See [Course Resource Configuration](../Courses/course-resource-config.md#course-directory)
        for details.

=== "External collaborator"

    An NJIT faculty member sponsors the guest account. Guest access lasts one year, and can be renewed annually.

    [Request Guest Access](https://njit.service-now.com/highlander_nexus?id=sc_cat_item&sys_id=afee4ca83b547e10ed2df90eb3e45a6f&table=sc_cat_item){ .md-button }

    #### What to Include in the Guest Access Request Form

    * **Contact ID for each person** — enter the NJIT UCID (in "UCID") if the guest is NJIT alumni, otherwise give their institutional or personal email address (in "Guest's Email").
    * **Sponsor** — the UCID of the sponsoring NJIT faculty member.
    * **What are you requesting the account for?** — select "Research Computing" and check "HPC (Wulver)".

    !!! warning "Select HPC (Wulver) to get the export control questions"

        Checking **HPC (Wulver)** adds a questionnaire to the form that routes the
        request through export control review with the Office of Research Integrity
        and Compliance. Submitting without it delays activation of the guest account.

    !!! warning "Most common delay"

        If HPC account request is submitted without the Export Control Questionnaire. Make sure to check the HPC (Wulver) box to avoid this delay.



## What Happens Next

1. **Sponsorship is confirmed.** If the PI sent or answered the request, the account is created. If not, we write back asking for their approval.
2. **The account is created and added to the group**, so jobs draw on that group's Service Units.
3. **An automated welcome email** with login details and first-step instructions is sent to the NJIT email address.
4. **The user logs in**, either over SSH or through [Open OnDemand](https://ondemand.njit.edu). See [Access to NJIT Clusters](cluster_access.md) for connection instructions.

    ```
    localhost> ssh -X -Y $UCID@wulver.njit.edu
    ```

5. **The user sets the account in their job scripts.** Jobs must name the group account they are charged to:

    ```bash
    #SBATCH --account=<PI_UCID>
    ```

    To see which associations an account belongs to:

    ```bash
    sacctmgr show assoc user=$USER format=account,partition,qos
    ```

!!! tip "Off campus"

    Connections from off campus require the [NJIT VPN](https://ist.njit.edu/vpn). All logins are completed with Cisco two-factor authentication (TFA).

## Related Requests

| Request | Who submits it | How |
|---------|----------------|-----|
| Add a member to an existing group | PI | Email [hpc@njit.edu](mailto:hpc@njit.edu) with the UCID |
| Remove a member from a group | PI | Email [hpc@njit.edu](mailto:hpc@njit.edu) with the UCID |
| Additional storage | PI | Email [hpc@njit.edu](mailto:hpc@njit.edu) with the amount needed |
| Additional Service Units | PI | See [Allocation Policy](../Policies/allocation_policies/index.md) |
| Software installation | Any user | [HPC Software Installation](https://njit.service-now.com/sp?id=sc_cat_item&sys_id=0746c1f31b6691d04c82cddf034bcbe2&sysparm_category=405f99b41b5b1d507241400abc4bcb6b) |

## Frequently Asked

??? question "I already have an account. Do I need a new one to work with a second group?"
    No. An account can be associated with more than one group. The second PI emails [hpc@njit.edu](mailto:hpc@njit.edu) to add you, and you select the group per job with `--account`.

??? question "A student in my group is graduating. What happens to their account?"
    Accounts follow NJIT affiliation. If continued access is needed, the PI should email us before the UCID is deactivated.

??? question "How long does account creation take?"
    Complete requests that include PI approval and UCIDs are typically processed within one business day. Guest accounts take longer because of the export control review.

??? question "I was told 'permission denied' when I tried to log in."
    The account may not be active yet, or the PI may not have added you to the group. See the [FAQs](../faq/faq.md#login-issues-access).

## Still Need Help?

Email [hpc@njit.edu](mailto:hpc@njit.edu). Please start a new email thread for a new question rather than replying to a resolved ticket.
