# SDN_IPHashLoadBalancer

## Project Overview

This project implements a Load Balancer using the IP Hash algorithm in a Software Defined Networking (SDN) environment. The topology is created using Mininet and controlled by the Floodlight controller. The primary objective is to analyze the performance of load balancing with the IP Hash algorithm in SDN networks.

## Setting Up the Project

### 1. Configuring the Project in Eclipse

To run this project, first copy the entire source code from the `kt` directory in the repository to your local Floodlight project directory to `pl.edu.agh.kt` package in `src/main/java` 

### 2. Running the Topology

Once you’ve copied the files, navigate to the directory where the topology source code is located, and use the following command to start the Mininet network with the custom topology:
```bash
sudo mn --custom topology_setup.py --topo mytopo --controller=remote,ip=<controller_ip>,port=6653
```
### 3. Sending Host IPs via API
To configure the IPs for the hosts in the topology, you can send a JSON request to the provided API endpoint. Here’s how to use it:

### API Endpoint
```bash
http://<controller_ip>/sdnlab/hosts
```
### Request Body

To send the list of hosts with their IPs, switch assignments, and ports, use the following JSON format:

```json
{
    "hostList": [
        {
            "name": "h1",
            "sw": 3,
            "port": 3,
            "ip": "10.0.0.1"
        },
        {
            "name": "h2",
            "sw": 4,
            "port": 3,
            "ip": "10.0.0.2"
        },
        {
            "name": "h3",
            "sw": 5,
            "port": 3,
            "ip": "10.0.0.3"
        },
        {
            "name": "h4",
            "sw": 6,
            "port": 3,
            "ip": "10.0.0.4"
        }
    ]
}
```
### How to Send the Request
You can send the JSON request using any HTTP client. For example, using curl:
```bash
curl -X POST -H "Content-Type: application/json" -d @hosts_config.json http://<controller_ip>:8080/sdnlab/hosts
```

### 4. Interacting with Hosts

To interact with the hosts in the topology, open a terminal in Mininet for each host by running the following command:
```bash
xterm <host_name>
```
The available hosts are:
- `h1`
- `h2`
- `h3`
- `h4`

### 5. Traffic Generation

To generate traffic from any of the hosts, run the traffic generator script located at:
```bash
python /path_to_source_code_of_traffic_generators/traffic_generator/traffic_generator_h1.py
```

### 6. Viewing Flow Tables on Switches
To display the flow tables on a specific switch, use the following command in Mininet terminal, where topology is created:
```bash
sh ovs-ofctl dump-flows <switch_name>
```
The available switches are:
- `s1`
- `s2`
- `l1`
- `l2`
- `l3`
- `l4`

### 7. Getting Link Information Between Switches via API

To get information about the links between switches in your topology, you can send a GET request to the following endpoint:
### API Endpoint
```bash
http://<controller_ip>:8080/wm/links/switch/json
```

# Topology
![obraz](https://github.com/user-attachments/assets/d0d7e3e0-429b-468d-ba50-474af776dab6)


# Authors
- Maciej Szymański
- Mikołaj Kozak
- Zofia Maślanka
- Marcin Bąba

# Bibliography
 - Analysis of Load Balancing Performance using Round Robin and IP Hash Algorithm on P4 (https://ieeexplore-1ieee-1org-1000047ao00f8.wbg2.bg.agh.edu.pl/document/10052975)
 - Enhanced network load balancing technique for efficient performance in software defined network (https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0284176)
 - Increasing SDN Network Performance Using Load Balancing Scheme on Web Server (https://ieeexplore-1ieee-1org-1000047ao00f8.wbg2.bg.agh.edu.pl/document/8528803)
