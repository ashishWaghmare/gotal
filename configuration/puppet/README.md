All machine Remove firewall
sudo su
iptables -F
iptables-save

master
sudo su
rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
yum -y install puppet-server


vim /etc/puppet/puppet.conf
dns_alt_name
certname

puppet puppet master --no-demonize --verbose



vagrant ssh puppet-agent-centos
sudo su
rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
yum -y install puppet


vim /etc/profile.d/puppet-agent.sh

vim /etc/puppet/puppet.conf

[agent]
  server=puppetmaster

puppet agent -t

vagrant ssh puppet-agent-ubuntu
sudo su
wget http://apt.puppetlabs.com/puppet-release-xenial.deb
dpkg -i puppet-release-xenial.deb
apt-get update
apt-get install puppet
vim /etc/profile.d/puppet-agent.sh


/etc/puppetlabs/code
/etc/puppetlabs/code/enviroments
/etc/puppetlabs/puppetserver




Fix DNS Name for all machines
vagrant ssh <machine_name>
sudo su
vi /etc/hosts
Add below linex
192.168.33.10   puppetmaster    puppetmaster.example.com
192.168.33.11   pac pac.example.com
192.168.33.12   pau pau.example.com

In Master 
vi /etc/puppet/puppet.conf
[main]
dns_alt_names =  puppetmaster,puppetmaster.example.com
certname=puppet

service puppet start

Agent Centos
[agent]
    server=puppetmaster.example.com

In Master
 /usr/bin/puppet master --no-daemonize --verbose
Kill before Server start

/usr/bin/puppet resource service puppetmaster ensure=running

service puppetmaster status

Agent Centos
service puppet stop
[root@centos-agent vagrant]# /usr/bin/puppet agent -t
Exiting; no certificate found and waitforcert is disabled

In Master
/usr/bin/puppet cert list
/usr/bin/puppet cert sign centos-agent

Agent Centos
/usr/bin/puppet resource service puppet ensure=running


In Master

Install Java Module
puppet module install puppetlabs-java
vim /etc/puppet/manifests/site.pp
class{ 'java' :
  package => 'java-1.8.0-openjdk-devel',

}

puppet module install puppetlabs-tomcat 

vim /etc/puppet/manifests/site.pp
class{ 'java' :
  package => 'java-1.8.0-openjdk-devel',
}
tomcat::install { '/opt/tomcat':
  source_url => 'https://archive.apache.org/dist/tomcat/tomcat-9/v9.0.7/bin/apache-tomcat-9.0.7.tar.gz'
}
tomcat::instance { 'default':
  catalina_home => '/opt/tomcat',
}

puppet agent --test --server pac.example.com --report

puppete agent -t

puppet agent --configprint server





https://github.com/ashishWaghmare/gotal.git
cd gotal\environments\puppet
vagrant up
vagrant ssh puppetmaster

http://nagiosxi.demos.nagios.com/nagiosxi/login.php?redirect=/nagiosxi/index.php%3f&noauth=1