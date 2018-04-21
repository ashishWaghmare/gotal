master
rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
yum -y install puppetserver
vim /etc/profile.d/puppet-agent.sh

agent-centos
rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm
yum -y install puppetagent
vim /etc/profile.d/puppet-agent.sh

agent-ubuntu
wget http://apt.puppetlabs.com/puppet-release-xenial.deb
apt-get update
apt-get install puppetagent
vim /etc/profile.d/puppet-agent.sh


/etc/puppetlabs/code
/etc/puppetlabs/code/enviroments
/etc/puppetlabs/puppetserver


