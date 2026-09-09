# CIA Triad

1. Confidentiality, integrity, availability

2. Confidentiality is ensuring that information is accessible only to those authorised to access it.
Stopping any random people finding the information
Encrypting files help to stop this happening 

3. One method an organisation could use is version control.
This is having copies of your data from every time it was updated. This is crucial for maintaining data integrity in environments where multiple revisions are common such as software development.
Having this means if something breaks you can revert back to an older version of your code allowing for easy fixing and remodelling.

Another method you could use is data backup.
This is taking regular backups of your data and having redundant systems to prevent data loss and ensure a consistent, accurate version is always available.
You should follow the 3-2-1 backup system for the most important files 

3 - Keep three copies of the data. This includes the original files plus at least two backups
2 - Store these copies on two different types of media or storage device. For example on the computer's hard drive, an external drive and a cloud backup.
1 - Keep one copy offsite (physically separate from your main location). Protects from disasters like fire and theft.

4. To follow the CIA triad the company must follow the following:

Confidentiality
The company must ensure that all information is accessible to only those authorised to see/access it.
This protects sensitive data from unauthorised disclosure.
To do this the company should encrypt everything to make sure it is secure.
They should set up access controls so only the people who need to see it can see it.
They should also classify their data as either public, internal, confidential or secret 
And have physical security to stop theft and damage from occurring.

Integrity
The company must ensure that the information remains accurate, consistent and trustworthy over its entire lifecycle.
To achieve this they should use:

Data validation to make sure information being put in is correct and use error checking methods like checksums and hashes to detect alterations
Version control to see who is changing what. This is good when lots of people are working on a project/file at once and can allow it to be reverted back to a past version if needed.
Audit trails - This allows people to see who changed what. You make a log of every change made to said file, so if someone messes it up you can see what they changed and revert it.
Data backup - Companies should backup files and data so they do not lose it. They should follow the 3-2-1 backup scheme as this keeps the files the safest: 3 copies of the file, stored across 2 different mediums, with 1 offsite backup (Google Drive, OneDrive)

Availability
The company must ensure that information is accessible to people who can see and need to see it when they need it.
To do this they can try:

Hardware maintenance - they should keep hardware up to date and replace desktops after 5-6 years. If they store data on an onsite NAS they should run it in a RAID array to ensure no data is lost and replace hard drives as soon as they die
Network management - They should maintain a reliable network infrastructure with minimal downtime so the files stored on the network are accessible. They should also make sure that they balance load to distribute traffic evenly.
Disaster recovery - They should have plans in place for data recovery in case of a disaster like a flood, fire, or cyber attack
Redundant systems - Their servers like the NAS should have dual power supplies and 2-4 NICs to ensure that if a power supply dies the NAS stays up. They should also have failovers just in case the whole system does die so people can still access data and resources during a failure of the main system.

Implementing these will ensure compliance with the CIA triad and allow everything to be accessed pretty much 24/7