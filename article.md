# 1. Motivation
The issue we are addressing here is the distribution of software projects. Let's say you developed a project on your computer, and would like to sent it to another machine, whether it is a remote server or someone else'e personal computer. 

Chances are this project will not **run** successfully right off the bat on this new machine, especially if we are talking about different Operational Systems (OS)... 

# 2. Containarization
To help overcome this issue there's a techique called containarization, which roughly consists of generating a package containing the OS and the dependencies required to run a targeted project. That way you can just ship this package to any computer and the project will work the same way.

# 3. Containarization tools
At the time of this writing (nov 2021), the most popular solution is [Docker](https://www.docker.com/). Although is this article we will focus on the second most popular, [Podman](https://podman.io/).

Both are very similar solutions. The Podman website even jokes about the fact that you can just do `alias docker=podman` and you are good to go (I would not do that, by the way).


# 4. Docker vs Podman
The most important differences between both approaches

|Feature  |Docker  |Podman|
|--|--|--|
|Supported OS |Windows, Mac OS, Linux  |Linux
|Environment|Daemon (where the containers run)|Daemonless (cointainers run as regular processes on the host)
|Security |Containers run as `root` (default)|Containers run as a regular users (default)

# 5. How podman works (same applies to docker)
[PIC]
