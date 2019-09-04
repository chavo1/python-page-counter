# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.box = "chavo1/bionic64-ember"
  config.vm.define "python" do |python|
    python.vm.hostname = "python"
    python.vm.network "private_network", ip: "192.168.56.56"
    python.vm.provision "shell",inline: "cd /vagrant ; bash scripts/install_redis.sh"
    python.vm.provision "shell",inline: "cd /vagrant ; bash scripts/provision.sh"

  end
end
