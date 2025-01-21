# SDN_IPHashLoadBalancer

## Project Overview

This project implements a Load Balancer using the IP Hash algorithm in a Software Defined Networking (SDN) environment. The topology is created using Mininet and controlled by the Floodlight controller. The primary objective is to analyze the performance of load balancing with the IP Hash algorithm in SDN networks.

## Setting Up the Project

### 1. Configuring the Project in Eclipse

To run this project, first copy the entire source code from the `kt` directory in the repository to your local Floodlight project directory on your virtual machine. 

### 2. Running the Topology

Once you’ve copied the files, navigate to the directory where the topology source code is located, and use the following command to start the Mininet network with the custom topology:
```bash
sudo mn --custom topology_setup.py --topo mytopo --controller=remote,ip=<controller_ip>,port=6653
```

### 3. Interacting with Hosts

To interact with the hosts in the topology, open a terminal in Mininet for each host by running the following command:
```bash
xterm <host_name>
```
The available hosts are:
- `h1`
- `h2`
- `h3`
- `h4`

### 4. Traffic Generation

To generate traffic from any of the hosts, run the traffic generator script located at:
```bash
python /path_to_source_code_of_traffic_generators/traffic_generator_h1.py
```

### 5. Viewing Flow Tables on Switches
```bash
sh ovs-ofctl dump-flows <switch_name>
```

To display the flow tables on a specific switch, use the following command:
# Topology
![obraz](https://github.com/user-attachments/assets/24b4f6ee-8b3f-4051-ac7d-51ecd707c693)

# Authors
- Maciej Szymański
- Mikołaj Kozak
- Zofia Maślanka
- Marcin Bąba

# Bibliography
 - Analysis of Load Balancing Performance using Round Robin and IP Hash Algorithm on P4 (https://ieeexplore-1ieee-1org-1000047ao00f8.wbg2.bg.agh.edu.pl/document/10052975)
 - Enhanced network load balancing technique for efficient performance in software defined network (https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0284176)
 - Increasing SDN Network Performance Using Load Balancing Scheme on Web Server (https://ieeexplore-1ieee-1org-1000047ao00f8.wbg2.bg.agh.edu.pl/document/8528803)
