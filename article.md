# 1. Motivation
The issue we are addressing here is the distribution of software projects. Let's say you developed a project on your computer, and would like to sent it to another machine, whether it is a remote server or someone else'e personal computer. 

Chances are this project will not **run** successfully right off the bat on this new machine, especially if we are talking about different Operational Systems (OS)... 

# 2. Containerization
To help overcome this issue there's a techique called containarization, which roughly consists of generating a package containing the OS and the dependencies required to run a targeted project. That way you can just ship this package to any computer and the project will work the same way.

# 3. Containerization tools
At the time of this writing (nov 2021), the most popular solution is [Docker](https://www.docker.com/). Although is this article we will focus on the second most popular one, [Podman](https://podman.io/).

Both are very similar solutions. The Podman website even jokes about the fact that you can just do `alias docker=podman` and you are good to go. This means that the same commands you use for Docker apply to Podman as well

>Personally, I would **not** set this alias. I think it would be very confusing.

# 4. Docker vs Podman
Among the most relevant differences between both approaches, we can list:

|Feature  |Docker  |Podman|Advantage (my opinion)|
|--|--|--|--|
|Supported OS |Windows, Mac OS, Linux  |Linux|Docker
|Environment|Daemon (where the containers run on)|Daemonless (cointainers run as regular processes on the host)|Podman
|Security |Containers run as `root`|Containers run as a regular users or `root`|Podman

# 5. How podman works (same applies to docker)
[PIC]
# 6. Pod
A pod is a group of 1 or more containers sharing the same network and more resources. 
If you are familiar with docker, a pod roughly translates to what `docker-compose` does. But it is a different concept, though. It is more relatable to the pods on a [Kubernetes](https://kubernetes.io/) cluster, hence the name `podman`.

# 6.1 Pod alternatives
For people migrating from Docker, one of the "problems" of Podman the lack of a tool as `docker-compose`.

# 6.1.1 Docker-compose
 As of [version 3 of Podman]((https://www.redhat.com/sysadmin/podman-docker-compose)), `docker-compose` is supported. Keep in mind that other tools are required to make it work properly.

# 6.1.2 Podman-compose

There's also there's an ongoing project called `podman-compose`, that requires [Python](https://github.com/containers/podman-compose).

# 7. The ephemeral nature of Podman containers
This is a very important concept to absorb :warning:
A container is a **virtual** instance of a image. When the container goes down (it is supposed to), it is gone forever! The next container based on that same image will be another instance (they even have an ID, so you can check that are actually different instances).
In practice this means that if write changes on a running container, they will be gone as soon as the container goes down.

# 8. Persisting data with Podman
As we just discussed, containers are not good are remembering things. In order to achieve persistancy when working with Podman, there's a concept called `volume`.
A volume works like a shared folder between the host and the container. The changes in one are mirrored on the other. This is very useful for working with databases, for instance. 

# 8.1 Use case for the volume feature
Let's say you have a PostgreSQL container running. The steps to persist its data would be:
* Find out the directory where the data is saved on the container (let's call it "C")
* Pick a folder "H" on the host
* Start the container with a volume, mapping "H" to "C"
* When the current container dies, the database-related data will be backed up in "H"
* The next container will than be able to resume the work left by the previous one, since its "C" folder will match "H".

# 9. Port mirroring
By using the same principle of the volumes, we can mirror ports between host and container using the same sintax `<port_host>:<port_container>`.

# 10. 