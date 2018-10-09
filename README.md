# Nginx on Docker on EC2 PoC

Deployment configuration for a single EC2 instance running in its own VPC and hosting Docker with an Nginx container. The configuration is driven via Ansible, CloudFormation and Systems Manager.

## Usage

### Deploy the infrastructure
```
ansible-playbook deploy.yaml
```

Optional parameters:

* `region`
* `stack_name`
* `network`

### Run the tests
```
ansible-playbook test.yaml
```

Optional parameters:

* `region`
* `stack_name`

## Implementation

The infrastructure consists of three CloudFormation stacks:

1. VPC
2. SSM Documents
3. Instance

### VPC

A very simple setup with an internet gateway and three public subnets spread across three availability zones.

### SSM Documents

A custom SSM document which is used in a State Manager association. The document installs Ansible and runs an Ansible playbook to configure the OS firewall, install Docker and start the Nginx container.

### Instance

A static instance with an ElasticIP configured via the above mentioned SSM Document and CloudFormation::Init.
