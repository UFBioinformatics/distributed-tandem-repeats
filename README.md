# Simple Sequence Repeats identification using a MapReduce based Distributed Implementation of K-mer algorithm

## Overview

The goal of this project is to understand the performance and feasibility of finding Simple Sequence Repeats in biological sequences using a distributed architecture. The project aims to identify any potential benefits of using a distributed model rather than the traditional approach.


## Contributors
- Devanshu Singh
- Rachana Gugale
- Mohammad Uzair Fasih

## Instructions for running the implementation
> You will need to setup the project before using the make commands. See Installation and Setup

The code contains implementations of K-mer algorithm that run both in a distributed and centralized manner.

All the normal non-distributed implementations are hosted inside the `standard-implementations` folder. The distributed implementations are hosted in the `map-reduce-python` folder.

## Datasets

The datasets used for implementing and testing the code is present in the dataset folder

## Algorithms

### K-mer Algorithm
---

To run the normal implementation of k-mer algorithm
```
make k-mer source=<source-file-path> kval=<size-of-k-mer> [output=<oupit-file-path>]
```

### Distributed K-mer Algorithm
---

To run the distributed implmentation of k-mer algorithm

```
make hadoop-k-mer source=<source-file-path> kval=<size-of-k-mer> [jobcount=><number-of-files>]
```

## Installation

This project uses Hadoop to implement a distributed architecture.
In order to ensure portability, this project uses docker to run hadoop and python based MapReduce.

In order to run this project, you need to install 
- Docker and Docker Compose (On Windows Machine, **WSL2 is required**)
- Git

## Setup

1. Clone this repo
2. Run the docker containers for docker

```bash
cd docker-hadoop
docker-compose up -d
```

3. After building the containers, use the following command to verify all the containers are up and running
```bash
docker ps
```

You should be able to see the following running containers
```
CONTAINER ID   IMAGE                           COMMAND                  CREATED              STATUS                        PORTS                                            NAMES
1250c84d3206   docker-hadoop_historyserver     "/entrypoint.sh /run…"   About a minute ago   Up About a minute (healthy)   0.0.0.0:8188->8188/tcp                           historyserver
332c9c511e1e   docker-hadoop_resourcemanager   "/entrypoint.sh /run…"   About a minute ago   Up About a minute (healthy)   0.0.0.0:8089->8088/tcp                           resourcemanager
1ae1d648dd42   docker-hadoop_nodemanager       "/entrypoint.sh /run…"   About a minute ago   Up About a minute (healthy)   0.0.0.0:8042->8042/tcp                           nodemanager
1ce3576b38c5   docker-hadoop_datanode          "/entrypoint.sh /run…"   About a minute ago   Up About a minute (healthy)   9864/tcp                                         datanode
efab4803b9c6   docker-hadoop_namenode          "/entrypoint.sh /run…"   4 minutes ago        Up About a minute (healthy)   0.0.0.0:9000->9000/tcp, 0.0.0.0:9870->9870/tcp   namenode
```


Or if you have Docker Desktop <br /><br />
<img src="./images/Docker_Desktop.PNG" />

Also visit [Hadoop Dashboard](http://localhost:9870) by going to http://localhost:9870 <br /><br />
<img src="./images/Hadoop_Dashboard.PNG" />


4. You can tear down your runnning containers using the following command.
```bash
docker-compose down
```