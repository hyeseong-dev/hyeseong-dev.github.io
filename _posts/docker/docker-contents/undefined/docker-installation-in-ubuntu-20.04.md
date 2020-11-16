# Docker Installation in ubuntu 20.04

## How to Install and Configure Docker on Ubuntu 20.04

5 months agoby [Younis Said](https://linuxhint.com/author/yunissaid12/)Docker is a container based on the “Platform as a Service” software application. Docker uses virtualization technology to provide isolated containers for software and tools. These containers use well-defined channels to communicate with each other. This article will show you the easiest way to install Docker on Ubuntu 20.04 and get it running in less than 5 minutes.

[![](https://linuxhint.com/wp-content/uploads/2020/06/1-16.jpg)](https://linuxhint.com/wp-content/uploads/2020/06/1-16.jpg)

This simple tutorial will show you how to download Docker, enable or disable Docker upon system reboot/startup, and change usage permissions for users in six easy steps.

## Step 1: Update APT

As always, first, update and upgrade your APT.How to Install and Configure Docker on Ubuntu 20.04×Volume 0% 

**$ sudo apt update**

[![](https://linuxhint.com/wp-content/uploads/2020/06/2-39.png)](https://linuxhint.com/wp-content/uploads/2020/06/2-39.png)

**$ sudo apt upgrade**

[![](https://linuxhint.com/wp-content/uploads/2020/06/3-37.png)](https://linuxhint.com/wp-content/uploads/2020/06/3-37.png)

## Step 2: Download and Install Docker

Enter the following command to download and install the Docker package.

**$ sudo apt install docker.io**

[![](https://linuxhint.com/wp-content/uploads/2020/06/4-34-1024x328.png)](https://linuxhint.com/wp-content/uploads/2020/06/4-34.png)

## Step 3: Launch Docker

Start Docker and enter the following command to enable it after every time the system reboots.

**$ sudo systemctl enable --now docker**

[![](https://linuxhint.com/wp-content/uploads/2020/06/5-38-1024x170.png)](https://linuxhint.com/wp-content/uploads/2020/06/5-38.png)

To disable it again, simply type in the following command.

**$ sudo systemctl disable --now docker**

[![](https://linuxhint.com/wp-content/uploads/2020/06/6-32-1024x117.png)](https://linuxhint.com/wp-content/uploads/2020/06/6-32.png)

#### Step 4: Set User Privileges

This step will show you how to give privileges to any user with Docker. You can replace “younis” with the user account you are giving permission.

**$ sudo usermod -aG docker younis**

[![](https://linuxhint.com/wp-content/uploads/2020/06/7-33.png)](https://linuxhint.com/wp-content/uploads/2020/06/7-33.png)

#### Step 5: Check Docker Version

You can check the version of Docker with the following command.

**$ docker --version**

[![](https://linuxhint.com/wp-content/uploads/2020/06/8-33-1024x146.png)](https://linuxhint.com/wp-content/uploads/2020/06/8-33.png)

#### Step 6: Test Docker

Test Docker by running the following command, which will open a container to run the Hello World command.

**$ docker run hello-world**

[![](https://linuxhint.com/wp-content/uploads/2020/06/9-26.png)](https://linuxhint.com/wp-content/uploads/2020/06/9-26.png)

#### Conclusion

Docker is a very useful tool for working with third-party software tools, as it establishes well-defined and secure channels for communication. Because it is so useful, Docker is becoming more popular day by day.

