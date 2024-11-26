from mininet.topo import Topo
from scapy.all import send, IP, ICMP, TCP, UDP, Raw
import random
import threading
import time

class MyTopo(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Initialize topology
        # Add hosts and switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        # Add links
        self.addLink(s1, s2)
        self.addLink(s1, h1)
        self.addLink(s2, h2)

        # Start traffic generation in a separate thread
        traffic_thread = threading.Thread(target=self.start_traffic)
        traffic_thread.daemon = True
        traffic_thread.start()

    def start_traffic(self):
        time.sleep(5)
        dst_ip = "10.0.0.2"

        def generate_icmp():
            send(IP(dst=dst_ip) / ICMP())

        def generate_tcp():
            send(IP(dst=dst_ip) / TCP(dport=random.randint(1, 65535), sport=random.randint(1024, 65535)))

        def generate_udp():
            send(IP(dst=dst_ip) / UDP(dport=random.randint(1, 65535), sport=random.randint(1024, 65535)) / Raw(load="Test payload"))

        def generate_http():
            http_request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(dst_ip)
            send(IP(dst=dst_ip) / TCP(dport=80, sport=random.randint(1024, 65535), flags="S") / Raw(load=http_request))

        def send_random_packet():
            packet_type = random.choice(['ICMP', 'TCP', 'UDP', 'HTTP'])
            print("packet_type:" + packet_type)
            if packet_type == 'ICMP':
                generate_icmp()
            elif packet_type == 'TCP':
                generate_tcp()
            elif packet_type == 'UDP':
                generate_udp()
            elif packet_type == 'HTTP':
                generate_http()

        packet_count = random.randint(10, 25)
        while True:
            send_random_packet()
            time.sleep(random.uniform(0.1, 1.0))  # Wait between packets

topos = {'mytopo': (lambda: MyTopo())}