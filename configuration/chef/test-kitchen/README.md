
kitchen -version

kitchen init --driver=kitchen-vagrant --provisioner=chef_zero

kitchen create --log_level=debug

kitchen list


