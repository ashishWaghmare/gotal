
# My SaaS
Simple SaaS to demonstarte micro services deployment.
Goal is to use DevOps cycle.

# Account
Represents User of Service which can be object, machine or company
Will use java

# Inventory
All service inventory being provided by the SaaS.
Will use python


# Metering
Captures service usuage by an Account which can be used to charge.
Will use golang

mvn io.quarkus:quarkus-maven-plugin:1.7.1.Final:create -DprojectGroupId=com.ashish.gotal -DprojectArtifactId=metering -Dextensions="vertx"
