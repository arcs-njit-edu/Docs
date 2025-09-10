---
title: GNU Parallel
---

[GNU Parallel](https://www.gnu.org/software/parallel/) is a shell tool for executing jobs in parallel using one or more computers. A job can be a single command or a small script that has to be run for each of the lines in the input. The typical input is a list of files, a list of hosts, a list of users, a list of URLs, or a list of tables. A job can also be a command that reads from a pipe. GNU parallel can then split the input and pipe it into commands in parallel.

!!! tip
     You can use GNU Parallel on your Mac OSX laptop/desktop to run applications in parallel. Just install using either brew or Macports

     ```console
     sudo port install parallel
     brew install parallel
     ```


## Availability

=== "Wulver"

     ```python exec="on"
     import pandas as pd
     
     df = pd.read_csv('docs/assets/tables/module_wulver_rhel9.csv')
     soft = df.query('Software == "parallel"')
     print(soft.to_markdown(index=False))
     ```


## Usage

???+ example "Usage"

    ```console
    module load parallel/20200422
    parallel echo ::: 1 2 3 ::: 4 5 6
    ```

## Purpose

GNU Parallel is a tool for running a series of jobs, mostly serial jobs, in parallel. This tool is best suited for running a bunch of serial jobs that may not run for the same simulation time. For example, the most easiest way to run a series of serial jobs in parallel on __n cpus__ within one submit script is as follows

```bash
./job_1 &
./job_2 &
...
./job_n &
wait
./job_(n+1) &
./job_(n+2) &
...
./job_2n &
wait
./job_(2n+1) &
./job_(2n+2) &
...
./job_3n &
wait
```

This works most efficiently when all jobs have the same or almost the same run time. If run times for jobs are unequal, then __n__ jobs are run simultaneously and the cpus remain idle until all __n__ jobs are completed before looping through the next __n__ jobs. This will lead to idle time and inefficient consumption of cpu time.

![Without Parallel](http://i.stack.imgur.com/uH0Dh.png){ width = "400" }

GNU Parallel solves this issue by first launching __n__ jobs. When one job completes, then the next job in sequence is started. This permits efficient use of cpu time by reducing the wait time and letting a number of small jobs to run while some cpus work on longer jobs.

```bash
parallel job_{1} ::: $(seq 1 3n)
```

![With Parallel](http://i.stack.imgur.com/17FsG.png){ width = "400" }

## Single Node example

## Multi Node example





## Related Links
* https://www.gnu.org/software/parallel/parallel_tutorial.html
* https://www.biostars.org/p/63816/
* http://www.shakthimaan.com/posts/2014/11/27/gnu-parallel/news.html
* https://www.msi.umn.edu/support/faq/how-can-i-use-gnu-parallel-run-lot-commands-parallel
* https://github.com/LangilleLab/microbiome_helper/wiki/Quick-Introduction-to-GNU-Parallel
* https://davetang.org/muse/2013/11/18/using-gnu-parallel/
* https://sites.google.com/a/stanford.edu/rcpedia/parallel-processing/gnu-parallel-examples
* http://phili.pe/posts/free-concurrency-with-gnu-parallel/
 

## User Contributed Information

!!! info "Please help us improve this page"

    Users are invited to contribute helpful information and corrections through our [Github repository](https://github.com/arcs-njit-edu/Docs/issues).


