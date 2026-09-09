1.	You will need a few switches, The Computers and A router, Unless they want to run a fibre link between the 2 sites so it is a fast connection.
2.	A router Routes the packets across the internet. A switch Switches the packets on a LAN
3.	The desktop Pc is the Client, the server is running the service


1.	A server may Host a service For a client Like a music server. Or Run a Storage server on the network Like a NAS
2.	A client on a Network is Someone using a Desktop Pc to access the internet and work using their Pc accessing a service Being hosted on a server. A server Hosts the Service for the client to use.
3.	One role of the Internet backbone is ISPs. Tier 1 ISPs Connect together their High speed Fiber-optic networks to make the Backbone. Tier 2 Often Contract with Tier 1 ISPs to gain access to the Global network. Tier 3 ISPs Offer internet access to Businesses and consumers, they rely on Tier 1 and tier 2 ISPs to do this.
4.	If part of the Internet Backbone Fails users could have issues connecting to a service. The User could Get an error message Telling them that the server they are looking for is down,  Or have a connection to the server with a Higher latency as it will have to re route the packets of data through Different cables to get to its destination. This could mean Loosing a game due to higher latency. File uploads or transfers taking longer Due to the packets having to take a different route.
5.	Routers Use The Internet Protocol, Media Access Control and Routing Tables to ensure data is delivered safely across networks By Breaking Down the Data Into packets, These packets are then Given a destination IP And MAC address so it knows where to send them. They are then Sent Across the network to data centres and ISPs. They will arrive in a router, the router will then look at the Destination IP in the packet header It will compare it against entries in its  Routing table using Longest prefix matching. This means it will find the best matching Route that matches the Destination, If more than one Route Exists, it selects the route with the longest subnet mask. It will then pick a routing method and send the packets to the Ip of the server That was next in the Routing table Until it reaches the Router At the location where the packets need to be, Ip has done its Job and got the packets to their Location, the MAC addresses then used to get the packets to the Destination Device where the packets are reassembled.


6.	There are many advantages and disadvantages to both Wired and wireless Networking. The advantages of Wired Networking are:

Wired networking will usually Deliver a Faster and more stable connection to the Users Device, allowing for faster File uploads and transfers as well as a better user experience for downloading files and general use of the machine.

With Wired networking there is better security. To connect to a wired network, you have to be in a room with an Ethernet or RJ45 Connector to be able to connect to the network as you have to plug in the device whereas Wireless You can connect to it from anywhere you have a signal.

However, there are Disadvantages Like:

Wired networking is less Flexible and scalable. With a wired network you have to be in a room with the cable to connect onto the network which means people have to sit at designated spaces to connect to the network. And to add more connections you have to run more cables to allow more users to connect to the network.

Another downside is Cost. It can cost more money to Buy all the Cables, switches and any other major costs. It can add up and be way more expensive than a wireless system as you need to buy appropriate switches to manage your workload. If a cable breaks you have to replace the whole cable which doesn’t cost allot unless it’s the cable in the wall that breaks or a Vital cable needed for carrying 10Gb/s of data, this can increase the cost of a wired setup.

With Wireless networking you get a similar experience, there are some advantages and disadvantages of Wireless networking, and they are:

High speed’s okay reliability. With wireless networking you get fast speeds, they won’t be as fast as a wired connection, but they will still be fast, the downside is they are less stable usually having more latency, suffering from speed drops resulting in a mediocre stability for the system.

Easy to scale and very flexible. With a wireless network you don’t need as many switches or as powerful of a switch, this is because you buy a Wireless Access Point (AP)and install it by running one cable to it. This then allows users to connect Via Wi-Fi to the network without any cables. This allows users to be anywhere within range of an AP and allow them to work easily allowing for better teamwork on projects. You can also buy higher power AP Allowing more users to connect to one AP rather than have 3 For 1 Room Improving scalability.

Cost and maintenance. The cost to set up a Wireless network will be Slightly Less expensive than a Wired network, but maintenance should also be lower as you set up the AP and people can access it. Unless the AP dies you don’t need to do anything. If the AP dies you can buy a new one and replace it easily.

The major Disadvantage of Wireless networking is Security. If a wireless network and its Access Points are setup incorrectly it can be a huge security risk, this Is because Anyone withing Range of the AP can connect and if it is not setup with a strong and secure Password people could gain access to the network and steal data. This can be stopped with proper setup and regular updates to the password and Access points Firmware.

Overall, it would be best to go for a hybrid network having the PCs you need most secure on their own Switch in their own VLAN, so they are off the Wireless network and not accessible unless you are in the room they are in. Then have a wireless network for the general use case stuff like most employees work and visitors. If you had to pick between One or the other, I would go with wireless as it offers the most flexibility for employees and can be cheaper and if setup properly should be secure for company use.

Simple Network Diagram
