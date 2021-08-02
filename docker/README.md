# HoneyPooh - Docker container
This is a version of our HoneyPooh that running on docker container.

# Getting Started
***Prerequisites***

First, you need to install docker. For this you can use the [site](https://docs.docker.com/engine/install/ubuntu/) or use our explanation.

Second, you need to install our code from this folder(`docker` folder). 

***Installing Docker***

**Delete all previous versions:**
```
sudo apt-get remove docker docker-engine docker.io containerd runc
```

**Set up the repository:**

1. Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```
$ sudo apt-get update

$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```
2. Add Docker’s official GPG key:
```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
3. Use the following command to set up the stable repository:
```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"


```

**Install Docker Engine:**

Update the apt package index, and install the latest version of Docker Engine and containerd:
```
 $ sudo apt-get update
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io
```

**Test:**

Run the command:
```
$ sudo docker run hello-world
```
This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.

# Running

After the downlonds, you can run the HoneyPooh. All you need to do is to run the HoneyPooh.exe on your computer.

You can run the file from the terminal with the command:
```
./HoneyPooh.exe
```

> The first run may take longer time than the rest because the downlonds.

When the project run you would see a control window.

From this window you will manage your HoneyPooh. 
