# Same Machine Clustser Setup

Download required file 
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.1.1-linux-x86_64.tar.gz

## First Machine
If you already have Elastic Search on your machine. 
1. Stop server 
1. Open config/elasticsearch.yml with vi/gedit/vscode
1. Uncomment line
    <pre>#cluster.name: my-application</pre>
1. Uncomment line
    <pre>#node.name: node-1</pre>    
1. Uncomment line
    <pre>#http.port: 9200</pre>    
1. Start server
    <pre>bin/elasticsearch</pre>


## Second and Onwards

      
      mkdir -p tmp/
      mv elasticsearch-7.1.1-linux-x86_64.tar.gz tmp/
      cd tmp/
      tar zxvf elasticsearch-7.1.1-linux-x86_64.tar.gz 
      mv elasticsearch-7.1.1 ~/es/node-2-es
      tar zxvf elasticsearch-7.1.1-linux-x86_64.tar.gz 
      mv elasticsearch-7.1.1 ~/es/node-3-es
      cd ~/es/node-2-es/
      cd ~/es/node-3-es/
      
### Setup again Node-2
1. Open New Terminal
1. Goto installation Zip
      <pre>cd ~/es/node-2-es/ </pre>
1. Uncomment line
      <pre>#cluster.name: my-application</pre>
1. Uncomment line
      <pre>#node.name: node-2</pre>    
1. Uncomment line
      <pre>#http.port: 9400</pre>    
1. Start server
      <pre>bin/elasticsearch</pre>

### Setup again Node-3
1. Open New Terminal
1. Goto installation Zip
      <pre>cd ~/es/node-3-es/ </pre>
1. Uncomment line
      <pre>#cluster.name: my-application</pre>
1. Uncomment line
      <pre>#node.name: node-3</pre>    
1. Uncomment line
      <pre>#http.port: 9600</pre>    
1. Start server
      <pre>bin/elasticsearch</pre>



    
1. Start server
<pre>bin/elasticsearch</pre>
  
  




#### Configuration Sample
Different type of nodes configurations

    node.master: true 
    node.data: false 
    node.ingest: false 
    cluster.remote.connect: false 

#### Data Node
    node.master: false 
    node.data: true 
    node.ingest: false 
    cluster.remote.connect: false

#### Ingest Node
    node.master: false 
    node.data: false 
    node.ingest: true 
    cluster.remote.connect: false

#### Coordinating Node
    node.master: false 
    node.data: false 
    node.ingest: false 
    cluster.remote.connect: false 
