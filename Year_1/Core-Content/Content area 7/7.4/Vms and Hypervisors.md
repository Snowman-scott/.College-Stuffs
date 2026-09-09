# Vms and Hypervisors

## **Question 1**
A Virtual machine is a software based emulation of a physical computer. It runs its own OS on the host machines Hardware.

## **Question 2 - Skipped**

Not Gunna be on the exam

## **Question 3**
There are a few differences between a Type 1 and Type 2 hypervisors 

A Type 2 hypervisor is a Hypervisor that runs on top of an existing OS Like Virtualbox on Windows or Linux. This allows for easy setup of Machines with an intuitive GUI great for consumers. The preformance of the Machine will be decent With decent security and No cost as VirtualBox is a Free software from Oracle. Type 2 hypervisors access the Host machines hardware Through the Host OS This is why it takes a preformance impact. An example of a Type 1 hypervisor would be Virtualbox or VMware

A Type 1 Hypervisor is a Hypervisor that runs Directly on the Hardware. This is harder to initially setup But has benifits like Better preformance as the hardware is not being bottlenecked By Another OS, It has higher security and is easier to scale than Type 2 Hypervisors. An example of a Type 1 hypervisor Would be KVM or Proxmox

## **Question 4**
The Company should make the Switch For many Reassons.

The Company could save Allot of resourcs and money by Virtualising their infrastructure. As the comapny is using a server per service they could just switch to using one or Two servers and sell off the rest. this would cut down on Power and hardware cost and make maintaining the servers more managable. As half their Current services probably do not need a Whole Machine Dedicated to them They can run Low powered Services on one Server stack, and then higher powered services on another stack only using 3-4 Stacks max. This would save allot of money and Time. Running everything on a Type 1 hypervisor will mean you get the best preformance for the services as it is Running Directly on the Hardware, It will also allow you to Backup and Restore anything incase of an emergency. This Will also allow Monitoring of services more easily and Setting up any new services will be easy.

The only Few drawbacks are the initial setup. As type 1 hypervisors require specialized knowledge you would need a trained IT Tech to Setup the servers and services. The migration process may be risky as you are moving 30 Different servers onto Less than 5 and theer could be data loss. and the Cost of Enterprise Type 1 Hypervisors like Proxmox Enterprise and VMware ESXi. And if you have one server running 6 Services, And that server goes down you loose all those services Whereas you wouldnt with the current setup. This can be Fixed using Clustering and mirorring/ Duplication But you would then need An extra server per Server.

Overall i think using a Type 1 Hypervisor Would benifit the company after the setup stage and allow them to cut prices on their Bills and only use the amount of Power that they need rather than runing a small Service on a massicve high powered Server.
