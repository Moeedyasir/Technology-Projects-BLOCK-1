# Part 4 – Raspberry Pi Hardware Identification
Upload:
```
/Users/moeed/Documents/Technology-projects/Technology-Projects-BLOCK-1/1.2_logic/01_computers/Images/pi-board.jpg
/Users/moeed/Documents/Technology-projects/Technology-Projects-BLOCK-1/1.2_logic/01_computers/Images/Raspberry-Pi-Components-Explanation.jpg
```
---
| Component | Function                                                                                                           |
|-----------|--------------------------------------------------------------------------------------------------------------------|
| SoC       | (system on chip) is the main integrated circuits that combines core computer hardware - such                       |
|           | such as the cpu, gpu, memory controllers, input/output interfaces - onto single microchip.                         | 
|           |                                                                                                                    |
|           |                                                                                                                    |
| GPIO      | (General purpose Input/Output) on raspberry pi is a set of programmable metal pins - typically arranged in         |
|           | 40 - pin header on modern models (26 pins on early models) that lets the raspberry pi send and recieve             |
|           | digital signals with external electronics. Sends signals out of the raspeberry pi to control comnponents.          |
|           | Reads signals coming into Raspberry Pi from swicthes, buttons or sensors. Code Typically refernces pins            |
|           | either by a physical header position (1-40) or by BCM (Broadcam) GPIO Numbers. Typical useages of GPIO is,         |
|           | Controlling LED's and Buzzers: Turning lights or indicators on and off through code,                               |
|           | Reading buttons and sensors Detecting button presses or enviromental/motion data, Driving motors or higher-        |
|           | power loads. Attaching HATs (Hardware Attached on Top) connecting add-on boards that use the GPIO header           |
|           | and ID pins for sensors, displays or robotics. Pins operate on 3.3v- applying a higher amount will damage          |
|           | the board. Devs commonly control pibs with python library.                                                         |
| USB       | Raspberry Pi USB designed to expnad storage and connectivity                                                       |
| HDMI      | Video and Output interface built on to connect to monitors, TV's or small HDMI displays.                           |
| Power     | The electrical power supply and power requirments used to run a raspberry Pi single-board-computer. Power          |
|           | supply can also come from GPIO pins, Power over ethernet, HATS or batteries.                                       |
| microSD   | A removable flash memory card used as the primary storage drive for a raspberry Pi computer. It holds the          |
|           | Raspberry pi OS.                                                                                                   
| Network   | Usally refers to either a group of interconnected raspberry pi network working togather such as (classroom         |
|           | Network) or a Home/local network applicances such as (router, ad-blocker, or VPN Gateway). raspberry pi runs       |
|           | Linux. Common uses of Raspberry pi is: linking multiple raspberry pis ober Ethernet or wifi to practise networking |
|           | command, share workloads, or build kubernets. Running home automation hubs, local file/media servers, or monitoring |
|           | dashbaords accessible to other devices on the networks. Hosting a VPN Server or using remote access tools          |
|           | to reach home network services from outside. (Raspberry pi cluster) - Multiple Pi Cluster linked to act            | 
|           | like a single computer system. (Homelab) - a home testband of servers and network gear often built around pi's.    |  
|           | (Edge network/ IoT network) - connected sensors, hubs and local nodes. (Pi-Based LAN/ Wireless mesh or hotspot) -  |   
|           | a local area network managed to extended by a pi.                                                                  
| Wireless  | is Using a Pi to connect to wifi - or act as a wireless hub, hotspot or access point - using built in wifi         |
|           | or a compatible USB Wifi adapter. Depends on how you put it, pi can simply join an existing network as a           |
|           | client or broadcast its own wireless network for other devices. The pi connects to a home router or a public wifi  |
|           | net to access the www, stream media, or run headless projects via SSH. Pi broadcasts its own wifi net so 
|           | phones, sensors or laptops can connect directly to it. It can route traffic to the Ethernet port, another 
|           | WIFI Network, or a standalone local network.  The Pi can also link wireless connection to wired ethernet 
|           | devices or pass a wired/vpn connection out over wifi so non-wireless gear can get online. 

---
## Reflection
Why are many components integrated into a single board in embedded computers such as the Raspberry Pi?
Write **100 words**.

Components integrated into a single board credit card size in embedded computers such as the raspberry Pi makes them smaller, 
cheaper and more efficient. Having components inside the pi the CPU, RAM, input/out connections on one board saves physical 
space and redcues the need for extra cables. It lowers manufactering costs because fewer seperate parts are needed. Integrating
components can improve reliability because there are few external connections that could become loose or damaged. It can also reduce power
consumption by allowing components to comminucate efficiently. This makes embedded computers suitable for devices with limited space and power. 