OSI shi

1. Layer 6 is responsible for encryption while data is in transmission using SSL and TLS

2. TCP ensures all the packets of data sent get delivered to the device. this ensures no broke n corrupt fles. 
UDP Does not make sure packets get there but is faster and better for things like online gaming, streaming and VOIP

3. The purpose of a MAC address is to tell packets of data which device they need to go to. the IP address is used to get the packets to your router.
The MAC address is used to point the packets that are being sent to your Router to your specified device.
MAC addresses are hardcoded on Ethernet ports. and can be changed on wireless devices. MAC addresses are encoded with 6 Hexadecimal numbers like (C8:7F:54:5D:58:C4)

4. One function of the network layer is Logical addressing. It uses IP addresses to determine where the destination device is.
Another function of the network layer is Fragmentation. It divides packets to fit the routers MTU and ensure that TCP dosent have to re-send massive files.

5. Through datas journy before it gets sent data is encapsulated. This is giving it information it needs to travle accross the network. Layers 7 - 5 encapsulate it with all the actual data being sent.
Layer 4 adds the TCP/UDP headers so it knows what protoclol its being sent with and has the actual data.
Layer 3 Segments the data into packets and adds the IP headers so it knows where it is being sent
Layer 2 Frames the data and adds the MAC address headers and puts teh segments into packets 
Layer 1 is just the RAW binary data
Then it goes again when it gets sent over

6.