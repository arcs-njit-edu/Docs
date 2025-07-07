# Facilities
As New Jersey’s Science and Technology University, New Jersey Institute of Technology (NJIT) has developed a local cyberinfrastructure well positioned to allow NJIT faculty and students to collaborate at local, national, and global levels on many issues at the forefront of science and engineering research.

## Cyberinfrastructure
NJIT’s Information Services and Technology (IST) resources provide members of the university community with universal access to a wealth of resources and services available over the NJIT network. NJIT's multi-100 gigabit backbone and multi-gigabit user network provides access to classrooms, laboratories, residence halls, faculty and staff offices, the library, student organization offices and others. 50% of these locations are provided with speeds of 5Gb/s or more. The campus wireless network 2,900+ access points blanket the university’s public areas, classrooms, offices, collaboration spaces and outdoor areas. Over 60% of the Wi-Fi network is Wi-fi 6 capable, enabling NJIT’s mobile users connectivity with multiple devices at increasing speeds. NJIT’s connectivity to NJEdge, NJ’s state-wide higher education network, provides access to the Internet and Internet 2. Students have the opportunity to work closely with faculty and researchers as new families of advanced applications are developed for an increasingly networked and information-based society. NJIT is also directly connected to cloud service providers such as AWS (Amazon Web Services) to provide low latency high speed access to cloud resources. A redundant diverse 100Gb network connection is being provisioned to support NJIT’s new HPC co-location facility in Piscataway NJ.

## Compute Resources
NJIT’s Advanced Research Computing Services (ARCS) group presently maintains a 127-node heterogeneous condominium cluster at the new HPC co-location facility, Databank in Piscataway, NJ, which went into production for general use in early 2024. The previous 224-node heterogeneous condominium cluster, Lochness, was decommissioned.

```python exec="on"
import pandas as pd
df = pd.read_csv('docs/assets/tables/facilities.csv')
#df.columns = pd.MultiIndex.from_tuples([(new_header, col) for col in df.columns])
print(df.to_markdown(index=False))
```

## Storage Resources
Storage on Wulver will be provided by a 1PB arcastream high-performance storage that combines flash, disk, tape, and cloud storage into a unified single namespace architecture. Data moves seamlessly through various tiers of storage - from fast flash to cost-effective, high capacity object storage, all the way out to the cloud.

The ARCS team provides 50TB of research and academic storage via the Andrew File System (AFS) distributed file system. AFS is backed up daily via IST’s enterprise backup system. The current AFS implementation, OpenAFS, which is open source, will be replaced with a commercial implementation, AuriStor, during the 2022-2023 academic year, providing important enhancements in performance, security,capacities, authorization, permissions, and administration as well as bug fixes and technical support.

## AFS Storage
AFS is a distributed file system. Its principal components are :

* Database servers : provide information on authorization, and directory and file locations on file servers 
* File servers : store all data in discrete "volumes", with associated quotas 
* Client software : connects AFS clients to database servers and file servers over a network. Every client has access to every file in AFS, subject to the permissions attached to the identity of the user logged into the client. Client software is available for Linux, MacOS, and Windows. Single global name space for all clients. See the identical path names and permissions.

An AFS "cell" is a group of database servers and file servers sharing the same cell name.

AFS was designed for highly-distributed wide area network (WAN) use. A cell can be concentrated in one physical location, or be widely geographically dispersed. A client in one cell can be given fine-grained levels of access to the data in other cells.

The NJIT cell name is `cad.njit.edu`; all file and directory paths begin with `/afs/cad.njit.edu/`(abbreviated to `/afs/cad/`). This cell currently contains about 27TB of research data, 4TB of user data,and 1.4TB of applications data, in about 47,700 volumes.

The current AFS implementation, OpenAFS, which is open source, will be replaced with a commercial implementation during the 2022-2023 academic year, providing important enhancements in performance, security,capacities, authorization, permissions, and administration as well as bug fixes and technical support.

All of `/afs/cad/` is backed up daily via IST enterprise backup.

## Cloud Computing
Access to Cloud Computing is provided via Rescale, a cloud computing platform combining scientific software with high performance computing. Rescale takes advantage of commercial cloud computing vendors such as AWS, Azure and Google Cloud to provide compute cycles as well as storage. The Rescale services also include applications setup, and billing and provides a pay-as-you-go method for researchers to use commercial cloud services - e.g., Amazon Web Services, Azure, Google Cloud Platform.

## Data Center: Space, Power and Cooling
NJIT’s recent purchase of the Wulver cluster exceeds the capacity of NJIT’s current computing facilities in terms of power and cooling. To accommodate Wulver and future expansion, NJIT has partnered with Databank, a leader in collocation facilities. Databank has more than 65 datacenters in over 27 metropolitan areas, supporting many industries including very large HPC deployments. The Databank location in Piscataway NJ will provide NJIT with 100% uptime SLA due to redundant power, cooling, and network facilities. The facility also provides water-cooling instead of traditional air-conditioned cooling in order to support far denser equipment needed for modern HPC. 


## Services
NJIT employs nine FTE staff members to administer and support research computing resources. Services available to the user community include system design, installation, and administration of research computing resources, application support, assistance with software purchasing and consulting services to faculty members, their research associates, and students.
