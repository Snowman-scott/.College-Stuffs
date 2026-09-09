# Question 1
1. A router is needed, or a hub, this will provide internet access to the customers, it will cost around £100 - £500
2. A Wireless access point, This helps people to access the internet with a stronger signal and a faster connection, they range from £50 - £350
3. A pos system, This will allow you to take payments from users, they range in cost from £100 up to £400
4. A Pc of some sort to run and manage all of the staff data and memberships, Can range from £600 - £4000+

# Question 2
1. A software solution you could use is An antivirus, this will stop you from getting hacked, or malware injected onto your pc as easily.It should be locally installed.
2. A form of cloud storage or a cloud database, this will allow you to keep track of all the staff and customer information, In the cloud it is backed up and hard to loose. this will ensure that all info will be easily accessible and secure to you and only you. Just not google drive T_T use proton..
3. POS payment system, this allows money to be sent to the company. it should be locally hosted with the info backed up to cloud.

# Question 3
Having the improved hardware and software means the internet for customers will be stable and secure, Having a good pc will allow for easy access to information needed and will allow for easier editing of the information, vs using a mobile device with a small screen

# Exam style Question
Hosting locally vs cloud secerity.

Hosting your services in the cloud is grat as it means you don't have bulky server sitting around, you can pay for what you need, it gets maintained for you etc, But it comes with risks. Hosting in the cloud means having to go over the internet to access the data, serivices and information stored. This causes some concernes and issues.
Sending data across the internet is "secure" but if the provider your using does not secure it properly, or a hacker somehow discovers the decryption key, or a stream of un encrypted data gets sent and intercepted that can cause issues as the information could be confidential, like card details, home addresses, phone numbers, SSN / NIN Etc...
If that data falls in the hands of a scammer or person with malicious intent they can easily exploit people. 
The benifit with cloud based aproches are, if the building burns down, there is still a copy somewhere else, If the file or server goes down data is switched to a new server and still accessible. 

The benifits of locally hosting is, no data gets exposed. You can airgap your network so no malware gets onto the server, or use AV software to block any malicious connections or malware. This reduces and stops the risk of data being taken by hackers, but it also comes with downsides.
You have to maintain the server, which means occasional downtime, you need to look after backups, If the server gets lost or broken you have to deal with buying a new one or fixing it, and if it is lost to a fire, you have lost the data and will have to start fresh.

I would personally use a hybrid aproach, I would host all the confidential stuff localy on a semi airgaped system in a proxmox ve, and have the rest hosted in cloud, like staff clocking times, memberships, menu, etc..
This gives easy access to change things while keeping confidntial data confidential
