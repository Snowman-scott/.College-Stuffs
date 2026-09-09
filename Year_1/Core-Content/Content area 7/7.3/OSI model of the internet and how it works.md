OSI :
# Layer 7 – Application Layer
Facilitates communication between end user applications and the network
Provides various network services like web browsing, email and file transfer
Protocols and services:
-	Email
-	Printers 
-	Web browsers 
-	Network drives
-	File sharing (p2p like torrenting)
-	Online games
-	Websites
-	Instagram
-	YouTube 
-	HTTP/S
-	POP 3
-	SMTP
-	DNS
-	FTP

---

# Layer 6 – Presentation layer 
Configures the Data 
Deals with compression and Encryption (Encrypt/ decrypt)
Translation (So the device can read it)
SSL – Secure socket layer (Redundant)
TLS – Transport Layer Security

---

# Layer 5 – Session layer
Layer is responsible for establishing and terminating connections between devices
Manages and controls the connection between computers (and devices)
Responsible for setting up, managing, and then dismantling the session layer
Authenticating 
Authorising 

---

# Layer 4 – Transport layer
This layer is Responsible for the reliable transfer of data
End – To – End communication 
Segmentation and reassembly 
Common protocols operating at the transport layer includes TCP and UDP. TCP is known for providing reliable connection-oriented-services, ensuring the accurate delivery of data. UDP offers a simpler connectionless service, suitable for applications where speed is critical and occasional data loss is acceptable.

---

# Layer 3 – Network layer
Responsible for data routing, packet forwarding, and logical addressing. Handles fragmentation and reassembly of packets across different networks
Routing:
-	Determines the optimal path for data transmission from the source to the destination across multiple networks
Logical Addressing:
-	Assigns and uses logical address to uniquely identify devices on a network
Quality of service (Qos):
-	Manages Data traffic to reduce packet loss, latency and jitter on a network

---

# Layer 2 – Data Link layer
Physical addressing (MAC Addressing):
-	The Data link layer adds MAC addresses to the frames header to identify the sending and receiving devices
-	These addresses are unique to each network interface and are crucial to Local area networking

Error detection and correction:
-	This layer is responsible for detecting and potentially correcting errors that may have occurred at the physical layer 
-	Techniques like CRC(Cyclical Redundancy check), checksums and parity checks to are used to ensure data integrity 

Flow control:
-	Prevent fast receivers from overwhelming slower receivers. The data link layer adds flow control

Access control:
-	When two or more devices are connected to the same network media, the data link layer protocols determine which has control over the medium at any given time
-	This is particularly important in shared media Like wireless networks or Ethernet Hubs

---

# Layer 1 – Physical layer
-	Transmission and reception of raw bit streams over a physical medium
-	Transmission media: cables (copper, fibre) repeaters and hubs
-	Transmission types: Electrical signals, light signals

---

OSI Layer 7 + 6 + 5 = layer 4 of TCP/IP
OSI Layer 4 = Layer 3 of TCP/IP
OSI Layer 3 = Layer 2 of TCP/IP
OSI Layer 2 + 1 = Layer 1 of TCP/IP

---

1.	The OSI model has 7 Layers. The TCP/IP model has 4 Layers

2.	The OSI model has More layers and breaks down TCP/IP layer 1 and 4 down int to 2 and 3 different layers 

3.	If the application layer is having issues that could cause protocols not to work, could be data lost, the server could be having issues, or there could be bugs in the code causing connectivity drops to the users. If the Transport layer has issues, If the packets aren’t all getting to the end users device the Transport layer is either using UDP and the data is corrupting or TCP is having an issue or has broken causing it not to check to see If the files are arriving properly. If they are not all arriving the webpage or app may not be able to load properly as the files it needs are corrupted

4.	The TCP/IP model is a more simplified version of the OSI model, The TCP/Ip model contains 4 layers (physical – Network – Transport – Application) 

The application layer is the what the users see on screen, encryption and does the Handshakes for talking to other devices. 

The Transport layer is where the data will get a selected protocol TCP or UDP to be sent off to the other device, This is also where data can be End to End encrypted and where a file gets segmented to be sent in packets to the other device.
Then the Network layer is where it picks an optimal route to be sent over the internet and It is also where it gets logically addressed to know where to send the packets

Then the physical layer is where The data is received into the devices LAN Router Then Uses MAC addressing to find the end device and send the packets to them over the transmission medium like cables or Wi-Fi

The OSI model has 3 extra layers. In the Application layer you have Application – presentation – session layers. The application is the same as on the TCP but there are 2 additional layers. Layer 6 and 5. Layer 6 is the presentation layer, it lays out the data and provides Security for web apps Etc..
Layer 5 is the session layer; this establishes the connection to other devices and does the security checking + Handshake to make sure the device is what it says. 
Layer 4 is layer 3 of TCP and layer 3 is Layer 2 of TCP, then the physical layer of TCP is split into 2 different layers, The data link layer (layer 2) and the Physical layer (layer 1) Layer 2 this does error correction, MAC addressing and Flow Control for the Data. And Layer 1 is the physical layer. This is the cables that connect your Pc to the network and the world like Fiber optic cables, copper cable and hubs.
This is useful in networking as it is easier to debug and fix issues that arise in the network and software, they should train their staff with OSI so it is easier to make Debug and fix issues that may arise from their code or infrastructure
