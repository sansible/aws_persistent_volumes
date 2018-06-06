# AWS Persistent Volumes

This role runs inside a provisioned service image to connect and mount EBS volumes.

Volumes can be looked up in two ways:

* An EBS volume ID can be assigned to an instance via tags, specifying the name of
  the tag to lookup via the ```persistent_volumes.aws.assigned_volume_instance_tag```
* Volumes be searched for using tags on the volumes themselves, this is the default
  behaviour




## Role Variables

Check [default variables](defaults/main.yml) for more details.




## Dependencies

This role needs to be run at startup before any software requiring the content of the file system is started. This means that services should not be set to auto-start, but started by Ansible as part of its startup routine.

In order for this role to work under Vagrant, the following config should be added to the Vagrantfile:

```Ruby
unless File.exist?("es1.vdi")
  vb.customize ['createhd', '--filename', "es1.vdi", '--size', "10240"]
end
vb.customize ['storageattach', :id, '--storagectl', 'SATAController', '--port', '1',  '--device', '0','--type', 'hdd','--medium',  "es1.vdi"]
```




## Example Playbook

The role should be called as per the following example:

```YAML
- role: sansible.persistent_volumes
  sansible_persistent_volumes_device:
    mount: /var/lib/elasticsearch
    owner: "{{ elasticsearch.user }}"
    group: "{{ elasticsearch.group }}"
```
