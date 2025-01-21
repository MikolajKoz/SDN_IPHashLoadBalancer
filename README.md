# SDN_IPHashLoadBalancer

Run floodlight project in eclipse copying whole source code from kt directory from repository to floodlight project on your VM

To run this topology type in directory where topology source code is located: "sudo mn --custom topology_setup.py --topo mytopo --controller=remote,ip=<controller_ip>,port=6653"
Switches list [s1, s2]

When topology is created type into mininet interface: "xterm <host_name>"
Hosts list [h1, h2 ,h3, h4]

In xterm terminal run traffic generator for any of the hosts: "python /path_to_source_code_of_traffic_generators/traffic_generator_h1.py"

To show flow table on switch: "sh ovs-ofctl dump-flows <switch_name>"

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
