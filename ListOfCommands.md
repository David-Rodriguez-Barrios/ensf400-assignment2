# Here is a list of all the commands necessary to run this lab in code blocks!

## Setting up the Code Space
```
pipx install ansible-core
ansible -galaxy collection install ansible.posix
ansible-galaxy colection install comunity.general
```


## Creating the SSH Secrets
These commands will create a secrets file, which contains an, id_rsa ( the private key Ansible Controller will hold as the credential to access the managed hosts.)

id_rsa.pub (This is the **Public** key that will be distributed to the managed hosts to authroize the Ansible Controller to login.)

id_rsa_container.pub (This is the public key copy to be mounted to the containers)

``` 
mkdir secrets
ssh-keygen -t rsa -N "" -C "root@0.0.0.0" -f secrets/id_rsa
chmod 400 secrets/id_rsa
cp secrets/id_rsa.pub secrets/id_rsa_container.pub
```
