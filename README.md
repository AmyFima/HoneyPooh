# HoneyPooh
HoneyPooh is a honeypot.
A honeypot is a security mechanism that detects attacks and gives you the option to investigate the attack. 
Our HoneyPooh is a like a proxy and he gives you the option to protect your server. 
It is located between the server and the client and tells you what is happening and whether the server is under attack. 

# Built With 
* [Elasticsearch](https://www.elastic.co/what-is/elasticsearch) - The database that stores all the information. 
* [Kibana](https://www.elastic.co/what-is/kibana) - The web that displays the information stored in the database.
* [Docker](https://www.docker.com/why-docker) - A virtual machine on which the project runs. 


# Getting Started 
**Prerequisites**

To run the project you just need to decide in which port the project will run and in which port you want to detect unusual actions.

> If you use **Docker** to run the project, you would need to download a docker. You can download a docker with the instructions in [README.md](https://gitlab.com/AmyFima/kinneret-201-honeypot/-/blob/5.0.0/docker/README.md) document in the `docker` folder or use the instructions in the [site](https://docs.docker.com/engine/install/ubuntu/).

> You need to download **Elasticsearch** and **Kibana** on your computer. You can use the instructions later in the document or use the [site](https://www.elastic.co/start).

***Installing Elasticsearch***

Enter the [site](https://www.elastic.co/start). Download Elasticsearch and Kibana for Linux. 
Start Elasticsearch with the commend:
```
bin/elasticsearch
```

Start Kibana with the commend:
```
bin/kibana
```

Open the browser in the site [http://localhost:5601](http://localhost:5601).
Link between Kibana and Elasticsearch by selecting Elasticsearch as a database of Kibana.

# Deployment
In the main folder, you can see 4 folders: 
* *attacks* - a few codes of attacks that you can check your server with them. 
* *docker* - the files for running the project on docker container.
* *proxy* - the files for running the project on the computer itself. 

# Running 
_There are 2 running options:_ 
* _running on the computer itself._
* _running on a Docker container._

For running on *the computer itself* go to the [README.md](https://gitlab.com/AmyFima/kinneret-201-honeypot/-/blob/5.0.0/proxy/README.md) document in the `proxy` folder.
For running on a *docker container* go to the [README.md](https://gitlab.com/AmyFima/kinneret-201-honeypot/-/blob/5.0.0/docker/README.md) document in the `docker` folder. 

# Versioning 
This version of the project works only in linux and contains a detection for 4 attacks:
* *DOS* - denial of service to real customers. 
* *Brute-Force* - sending many passwords in hopes of guessing the right combination. 
* *Remote-Code-Execution* - running code with system-level privileges. 
* *Session-Prediction* - impersonating or abducting a user by guessing the user's unique value. 

# Authors 
* **Amy Fima**
