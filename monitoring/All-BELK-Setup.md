
## NodeJs
Take sample code of Nodejs as sample to test code

    git clone https://github.com/omerio/employee-microservice-node.git
    cd employee-microservice-node
    npm install
    npm start > node.log 2>&1 &

## Logstash

    bin/logstash -f logstash-beats.conf

## Filebeat

    curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-7.1.1-darwin-x86_64.tar.gz
    tar xzvf filebeat-7.1.1-darwin-x86_64.tar.gz
    cd filebeat-7.1.1-darwin-x86_64/

    bin/filebeat setup
    bin/filebeat -c filebeat.yml -e

## Elastic-Search

As usual just start server

## Kibana

As usual just start server after ES

