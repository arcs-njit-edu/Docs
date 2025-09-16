## The following are questions we have received over the last several weeks regarding the migration from Lochness to Wulver.

###  What is the timeline for the migration from Lochness to Wulver?
??? answer

    We anticipate the migration process to be complete by the end of February 2024. The migration will commence on January 16, 2024, and our team is dedicated to ensuring a smooth transition for all users. We will keep you informed about any updates or changes to the timeline as the migration progresses. Your cooperation and understanding during this period are greatly appreciated. If you have any specific concerns about the timeline, please feel free to reach out to our support team for further clarification.

### How will the migration impact my existing workflows and computations?

??? answer

     The research facilitation team is committed to assisting you during the migration process. Our team will work closely with you to ensure that your existing workflows and computations are seamlessly transferred to Wulver. We understand the importance of minimizing disruptions to your research activities, and our experts will provide guidance and support to address any compatibility issues that may arise. You can expect personalized assistance to make the transition as smooth as possible. If you have specific concerns about your workflows, please don't hesitate to reach out to our team for tailored support.


### What specific steps should I take to prepare for the migration?

??? answer

    To prepare for the migration, there are a few crucial steps:
    
     - Provide a List of Current Students and Postdocs: 
        - Please share with us an updated list of current students, postdocs, and external collaborators who are actively using the HPC resources on Lochness. This information will ensure that user accounts are accurately migrated to Wulver, and access is maintained for the relevant individuals.
    
       - List of Required Software: 
          - Compile a list of software applications that are essential for your research. This includes both commonly used software and any specialized tools unique to your work. Knowing your software requirements enables us to ensure that the necessary applications are available and properly configured on Wulver. You can find the list of software applications installed on Wulver in [Software](../Software/index.md). If you don't find your applications in the list, submit a request for [HPC Software Installation](https://njit.service-now.com/sp?id=sc_cat_item&sys_id=0746c1f31b6691d04c82cddf034bcbe2&sysparm_category=405f99b41b5b1d507241400abc4bcb6b) by visiting the [Service Catalog](https://njit.service-now.com/sp?id=sc_category).
    
       - Planning for Former Students: 
          - If you have former students who may still have data or files on Lochness, it's essential to plan for their data migration or archival. We recommend reaching out to former students to coordinate any necessary data transfers or backups to avoid potential data loss.
      
      These steps will contribute to a successful migration, allowing us to tailor the process to your specific needs. If you have any questions or need assistance with these preparations, please contact our support team.


### Will there be any downtime during the migration, and how will it affect my research activities?
??? answer

     Once the migration has started for your group, Lochness will be inaccessible. If access to Lochness is critical for specific tasks during this period, we strongly encourage you to reach out to us. We understand that some users may have time-sensitive activities or dependencies on Lochness, and we are committed to working with you to find solutions that meet your needs. Please contact our support team by sending an email to [hpc@njit.edu](mailto:hpc@njit.edu) to discuss your specific requirements, and we will do our best to accommodate your situation during the migration process. You can check [Contact Us](contact.md) to see how to create tickets with us and what information is required to create tickets. 

### Is there a plan for backing up and restoring data during the migration process?
??? answer

     Yes, there is a plan in place for data continuity. The data on Lochness resides on a shared filesystem, and these same filesystems will be mounted and available on Wulver post-migration. This approach ensures that your data remains accessible and seamlessly transfers to the new cluster.

      There is no need for a separate backup and restoration process as the shared filesystem continuity facilitates a smooth transition. If you have specific data-related concerns or requirements, please feel free to reach out to our support team ([Contact Us](contact.md)) for further clarification and assistance. Your data integrity and accessibility are our top priorities throughout the migration process.

### What changes will occur in the file directory structure, especially regarding the `/research` and `/home` directories?
??? answer

    With the migration to Wulver, there will be changes in the file directory structure:
    
    Filesystems on Wulver: Wulver will have three filesystems available for use: `/home`, `/project`, and `/scratch`.
    
    - Availability of `/research` Directory: The `/research` directory from Lochness will be mounted on Wulver and will be available for use. This ensures continuity for research-related files and data.
    
      - Lochness `/home` Directory on Wulver: The Lochness `/home` directory will be mounted on the Wulver login node as `/oldhome`. Users will be able to read files in this directory and move files from this directory but will not be able to write files into this deirectory. This allows users to access their personal home directories from Lochness during the migration period. The Lochness files under `/oldhome` will be available until 1-Jan-2025. Users should move needed files into `/project/PI_UCID` directory (replace PI_UCID with the UCID of PI). 
    
    These changes are designed to optimize the file organization on Wulver while maintaining accessibility to critical research data. The research facilitation team will work closely with users to ensure a smooth transition of data and assist in adapting to the new file directory structure. If you have specific questions or require assistance with data migration, please don't hesitate to contact our support team.


### How will the migration impact access to specialized software or applications that I currently use on Lochness?
??? answer

     The research facilitation team is dedicated to ensuring a smooth transition for users in terms of software and applications:
      
    - Installation Support: 
        - The research facilitation team will handle the installation of necessary software on Wulver, ensuring that essential tools and applications are available for your research. You can request for [HPC Software Installation](https://njit.service-now.com/sp?id=sc_cat_item&sys_id=0746c1f31b6691d04c82cddf034bcbe2&sysparm_category=405f99b41b5b1d507241400abc4bcb6b) by visiting the [Service Catalog](https://njit.service-now.com/sp?id=sc_category). Please visit [Software](../Software/index.md) to see the list of applications isntalled on Wulver.
      - Code Compilation Assistance: 
          - If your research involves custom code that needs compilation, the research facilitation team will provide assistance to ensure a successful compilation on Wulver. This support extends to helping users adapt their code to the new environment.
      
    Our goal is to minimize any disruptions to your research activities and provide the necessary support for a seamless transition. If you have specific software requirements or need assistance with code compilation, please reach out to the research facilitation team, and they will be happy to assist you.

### Can I continue using Lochness for specific tasks during the migration, or will it be completely inaccessible?
??? answer

     Once the migration has started for your group, Lochness will be inaccessible. If access to Lochness is critical for specific tasks during this period, we strongly encourage you to reach out to us. We understand that some users may have time-sensitive activities or dependencies on Lochness, and we are committed to working with you to find solutions that meet your needs. Please contact our support team to discuss your specific requirements, and we will do our best to accommodate your situation during the migration process.

### What happens to my existing job submissions and queued jobs during the migration process?
??? answer

     For the most part, the migration will start after all running jobs have been completed. We understand the importance of job completion for ongoing research activities. Accommodations will be made for long-running jobs that cannot be checkpointed.
      Our aim is to minimize disruptions to your computational tasks and ensure a smooth transition. If you have specific concerns about job submissions or if you anticipate long-running jobs during the migration period, please communicate with our support team. We are here to work collaboratively and make necessary accommodations to facilitate the completion of your jobs during the migration process.

### Are there any adjustments needed for code or scripts to ensure compatibility with Wulver?
??? answer

    Yes, adjustments will be required for code or submission scripts to ensure compatibility with Wulver:
      
     - Submit Script Changes: 
        - Submit scripts will need to be modified to accommodate changes in partitions, hardware configurations, policies, and filesystems on Wulver. The research facilitation team will provide guidance and support in updating your submit scripts for seamless job submissions. Check the sample submit scipts for Wulver in [SLURM](slurm.md).
       - Code Recompilation: 
          - Due to differences in hardware, code may need to be recompiled to ensure optimal performance on Wulver. The research facilitation team is ready to assist you in this process, offering support to recompile code and address any related issues.
          - If you code is compiled based on [FOSS Toolchain](compilers.md#free-open-source-software-(foss)) (GCC and OpenMPI), you need to compile the code the same way you did in Lochness. Just make sure all the dependency libraries are installed on Wulver. Please visit [Software](../Software/index.md) to check the list of applications installed on Wulver.
          - If your code is based on the [Intel toolchain](compilers.md#intel), you need to add the following while configuring your code. 
            ```console
            ./configure CFLAGS="-march=core-avx2"
            ```
          - When installing codes, ensure that you perform the installation on the compute node rather than the login node. Since the hardware architecture is different on the login node, it's best practice to compile your code on the compute node. You need to initiate an [interactive session with compute node](slurm.md#interactive-session-on-a-compute-node) before compiling your code.
      
    Assistance will be provided to help you adapt your code and scripts to the new environment on Wulver. If you have specific concerns or require support in making these adjustments, please reach out to our [research facilitation team](contact.md), and they will work with you to ensure a smooth transition.

### Will there be training sessions or documentation available to help faculty and researchers transition smoothly to Wulver?
??? answer

     While there are no official training sessions scheduled at this point, comprehensive documentation is available at [NJIT HPC Documentation](https://hpc.njit.edu) to assist faculty and researchers during the transition to Wulver.
      In addition to documentation, the research facilitation team is committed to providing personal assistance to faculty and researchers. If you have specific questions, require hands-on support, or need guidance on using Wulver effectively for your research, please do not hesitate to reach out to the [research facilitation team](contact.md). We are here to ensure that you receive the assistance you need for a successful transition.

### How can I request additional resources or discuss specific requirements for my research projects on Wulver?
??? answer

     To request additional resources or discuss specific requirements for your research projects on Wulver, please reach out to us at [hpc@njit.edu](mailto:hpc@njit.edu). Our team is ready to assist you with any inquiries related to resource allocation, project needs, or any other aspects that can enhance your experience on the Wulver cluster. Your requests will be promptly addressed, and we are committed to providing the support necessary for the success of your research endeavors.

### What support services will be available during and after the migration to address any issues or concerns?
??? answer

     The research facilitation team is committed to providing personalized assistance and support services during and after the migration:
    
      - Personal Assistance:
        - The research facilitation team is dedicated to offering personal assistance to each user. Whether you need help with data migration, code adjustments, or understanding the new environment, our team is here to provide tailored support.
    
        - Issue Resolution:
          - Any issues or concerns that arise during or after the migration will be promptly addressed by the research facilitation team. We aim to ensure a smooth transition for all users and are ready to tackle any challenges that may arise.
    
        - Ongoing Support:
          - Support services will continue to be available after the migration to address ongoing needs, answer questions, and assist with any further optimizations or adjustments required for your research projects.
    
      Your success is our priority, and the research facilitation team is here to guide you through the migration process and beyond. If you encounter any issues or have specific concerns, please reach out to the team for personalized assistance.

### Can I test my applications or simulations on Wulver before the migration to ensure compatibility?
??? answer

     Yes, absolutely! We encourage users to proactively test their applications or simulations on Wulver before the migration to ensure compatibility and identify any potential issues. This testing phase allows you to familiarize yourself with the new environment and address any concerns in advance.
    
      If you encounter challenges or have questions during the testing process, please don't hesitate to reach out to us. Our team is here to provide guidance, answer queries, and assist you in ensuring a smooth transition for your research activities on Wulver. Your proactive testing will contribute to a successful migration experience.

### How long will the `/oldhome` directory on Lochness be accessible after the migration, and what actions should I take regarding data stored there?
??? answer

     The `/oldhome` directory on Lochness will be accessible for 6 months after the migration is complete. During this period, users are advised to review and move their data to other locations on Wulver or archive it as needed. This timeframe provides a reasonable window for users to organize and transfer their data while ensuring a smooth transition.
    
      If you have specific questions about data migration or need assistance during this post-migration period, please reach out to our support team. We are here to help you with any further steps or considerations related to your data on Lochness.

### Will AFS be available on Wulver?
??? answer

    The AFS will not be available on Wulver. However we will setup a self-serve procedure for researchers to move AFS files to `/research`. We can do this as part of the full migration process. Please reach out to us at [hpc@njit.edu](mailto:hpc@njit.edu) for any questions.

### I have several Conda environments on Lochness. Should I perform a fresh installation or copy the environment to Wulver?
??? answer

    We recommend a fresh installation since the hardware architecture is different on Wulver. However, you can export the existing Conda environment to a YAML file, transfer it to Wulver, and then install the environment using this YAML file. See [Conda Export Environment](conda.md#export-and-import-conda-environment) for details.