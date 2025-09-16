# Lochness to Wulver Migration: File Directory Changes

## Overview

As part of the HPC cluster migration from Lochness to Wulver, there will be changes in the file directory structure to ensure a smooth transition. This documentation provides details on how the `/research` and home directories will be handled on the new Wulver cluster.

### `/research` Directory

The `/research` directory from Lochness will be mounted on Wulver as `/research`. This ensures that users can seamlessly access their research-related files and data in the familiar directory structure. All content, including subdirectories and files, within `/research` on Lochness will be avaialble on the same location on Wulver.

### Home Directories

#### Lochness Home Directory

The home directories from Lochness will be available on Wulver under the directory `/oldhome`. Users will find their personal home directories within `/oldhome`, allowing them to access their files and configurations.

#### Locking of `/oldhome` Directory

After the migration is completed, the `/oldhome` directory on Lochness will be locked. This means that no additional files or directories can be created in `/oldhome`. The locking of this directory is a crucial step to maintain the integrity of the migrated data and to ensure a stable environment on both clusters.

Users are advised to review and transfer any necessary files from `/oldhome` on Lochness to their new home directories on Wulver during the migration period.

### Important Notes

- **Migration Date:** The migration process is scheduled to start on January 16, 2024.
- **Locking Date for `/oldhome`:** After the migration, the `/oldhome` directory on Lochness will be locked to prevent further modifications.
- **File Access:** Users will have continued access to their research files under `/research` on Wulver and their home directories under `/oldhome` on Lochness until the specified locking date.

Please make the necessary adjustments to your workflows and ensure a smooth transition by reviewing and moving your files as needed. If you have any questions or concerns, feel free to reach out to our support team.
