MEMORY = 2048
CPU_COUNT = 1
IP_ADDR = "192.168.10.5"

Vagrant.configure("2") do |config|

  config.vm.box     = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  config.vm.network :private_network, ip: IP_ADDR

  config.vm.synced_folder ".", "/vagrant", :create => true

  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", MEMORY.to_s]
    vb.customize ["modifyvm", :id, "--cpus", CPU_COUNT.to_s]
  end
  #config.ssh.forward_x11 = true
  config.ssh.forward_agent = true
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "statsd-graphite.yaml"
    ansible.inventory_path = "inventory/vagrant/inventory.ini"
    ansible.verbose = "extra"
  end
end
