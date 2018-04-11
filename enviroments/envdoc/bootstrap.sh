apt-get -yq update
apt-get -yq install curl
curl -sSL https://get.docker.com/ | sh
sudo usermod -aG docker vagrant
