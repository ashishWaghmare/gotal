apt-get -yq update
apt-get -yq install curl
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker $(uname -s)
sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
