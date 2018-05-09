# gotal
Vagrant and Docker based mix environment which demonstrates end to end demo for DevOps Cycle.
Involves github,dockerhub and other third party services to complete enitre cycle where we show code changes being pushed from git
till it gets deployed to production

<img src="/dv-cc.png" alt="Whole Cycle"/>

# towar [Java Micro Service]
Open Docker Quickstart Terminal
When your current folder is towar, execute below command 

   docker-compose up

This is sample app shows two docker image
1. mysql:8.0
2. web: tomcat:9
	mysql-connector-java:8.0 version

If you are running on docker machine on windows
  http://192.168.99.100:8080/towar/db.jsp?user=root

If you are running on linux machine
  http://127.0.0.1:8080/towar/db.jsp?user=root

You can query different user by replacing "root" with other user

It was create with below command in maven
mvn archetype:generate -DgroupId=example.ashish   -DartifactId=gotal -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
Added JDBC driver and two new jsp
1. index.jsp
2. db.jsp


# Automated Testing [ Selenium / Cucumber ]

Google Search Example taken from
Borrowed from https://github.com/dev9com/cucumber-java-selenium-example.git

mvn archetype:generate -DgroupId=example.ashish -DartifactId=towar -DarchetypeArtifactId=maven-archetype-webapp -DinteractiveMode=false

# Vagrant on Windows Setup

vagrant init
vagrant box add ubuntu/xenial64
vagrant up
vagrant ssh

# Flkpy [ Flask Python ]

Python and Flask web framework based icroservice 
