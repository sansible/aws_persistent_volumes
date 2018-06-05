# AWS Persistent Volumes

This role runs inside a provisioned service image to connect and mount EBS volumes from the CF stack spun up by persistent_volumes role in services_ops.

Volumes can be looked up in two ways:

* An EBS volume ID can be assigned to an instance via tags, specifying the name of
the tag to lookup via the ```persistent_volumes.aws.assigned_volume_instance_tag```
* Volumes be searched for using tags on the volumes themselves, this is the default
behaviour


Role Variables
--------------
| Variable| Default| Description|
|---|---|---|
|device|/dev/xvdb|The linux device path where the block device is expected to appear.|
|ensure_directories|[]|List of directories that will be created if they do not exist on the device|
|group|"root"|The group id that should be applied on the mount point.|
|label|"auxiliary"|The filesystem label that should be applied on the ext4 filesystem. This is largely used for internal purposes in the role.|
|mode|"0755"|The octal permission mode applied to the mount point.|
|owner|"root"|The owner id that should be applied on the mount point.|
|path|"/mnt"|The system path where the filesystem should be mounted. It creates the path, if not present.|
|aws.assigned_volume_instance_tag|false|Name instance tag from which to grab the EBS volume ID|
|aws.tagged_volume_lookup_filters|See defaults/main.yml|Tags to use to lookup volumes|

Dependencies
------------

This role needs to be run at startup before any software requiring the content of the file system is started. This means that services should not be set to auto-start, but started by Ansible as part of its startup routine.

In order for this role to work under Vagrant, the following config should be added to the Vagrantfile:

```
unless File.exist?("es1.vdi")
  vb.customize ['createhd', '--filename', "es1.vdi", '--size', "10240"]
end
vb.customize ['storageattach', :id, '--storagectl', 'SATAController', '--port', '1',  '--device', '0','--type', 'hdd','--medium',  "es1.vdi"]
```


Example Playbook
----------------

The role should be called as per the following example:

```YAML
- role: sansible.persistent_volumes
  sansible_persistent_volumes_device: /dev/xvdb
  sansible_persistent_volumes_path: /var/lib/elasticsearch
  sansible_persistent_volumes_owner: "{{ elasticsearch.user }}"
  sansible_persistent_volumes_group: "{{ elasticsearch.group }}"
```
