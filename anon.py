#!/bin/python
from scapy.all import *
import sys
import gc

def write(pkt,filename):
    wrpcap(filename+"-anon.pcap", pkt, append=True)

macs = {}
ips = {}
new_ips=[0,1]
new_mac=[0,1]
pkt_counter = 0

#usage: python anon.py pcap1,[pcap2...]

if __name__ == "__main__":

  if len(sys.argv) != 2:
    print "usage: python anon.py pcap1,[pcap2...]"
    sys.exit()

  files = sys.argv[1].split(',')

  for f in files:

    print "reading " + f
    pcap = rdpcap(f)
    print "done reading "+f+", starting anonymization"

    for pkt in pcap:

      pkt_counter += 1 # number of packets analysed, just for documentation

      # anonymizing MAC adresses in the form ff:ff:ff:ff:__:__

      #src
      if Ether in pkt:
        if pkt[Ether].src in macs:
          pkt[Ether].src = macs[pkt[Ether].src]
        else:
          tmp_mac = "ff:ff:ff:ff:"+str(new_mac[0]).zfill(2)+":"+str(new_mac[1]).zfill(2)
          macs[pkt[Ether].src] = tmp_mac
          pkt[Ether].src = tmp_mac
          new_mac[1] += 1
          if new_mac[1] >= 99:
            new_mac[0] +=1
            new_mac[1] = 0

      #dst
      if Ether in pkt:
        if pkt[Ether].dst in macs:
          pkt[Ether].dst = macs[pkt[Ether].dst]
        else:
          tmp_mac = "ff:ff:ff:ff:"+str(new_mac[0]).zfill(2)+":"+str(new_mac[1]).zfill(2)
          macs[pkt[Ether].dst] = tmp_mac
          pkt[Ether].dst = tmp_mac
          new_mac[1] += 1
          if new_mac[1] >= 99:
            new_mac[0] +=1
            new_mac[1] = 0

      # anonymizing IP adresses. New IPs in 192.168.0.0/16

      #src
      if IP in pkt:
        tmp_ip = pkt[IP].src.split('.')
        if int(tmp_ip[0]) == 10 and int(tmp_ip[1]) == 128: # attacker, do not anonymize
	        print "found attacker with IP " + str(tmp_ip)
        else:
          if pkt[IP].src in ips:
            pkt[IP].src = ips[pkt[IP].src]
          else:
            ips[pkt[IP].src]="192.168."+str(new_ips[0])+"."+str(new_ips[1])
            pkt[IP].src = ips[pkt[IP].src]
            new_ips[1] +=1
            if new_ips[1] == 255:
                new_ips[0] += 1
                new_ips[1] = 0

      #dst
      if IP in pkt:
        tmp_ip = pkt[IP].dst.split('.')
        if int(tmp_ip[0]) == 10 and int(tmp_ip[1]) == 128: # attacker, do not anonymize
          print "found attacker with IP " + str(tmp_ip)
        else:
          if pkt[IP].dst in ips:
            pkt[IP].dst = ips[pkt[IP].dst]
          else:
            ips[pkt[IP].dst]="192.168."+str(new_ips[0])+"."+str(new_ips[1])
            pkt[IP].dst = ips[pkt[IP].dst]
            new_ips[1] +=1
            if new_ips[1] == 255:
                new_ips[0] += 1
                new_ips[1] = 0

      #write packet to new file
      write(pkt,f)

    print "done anonymizing " + f
    print str(len(macs)) + " MAC adresses and " + str(len(ips)) + " IPs anonymized in " + str(pkt_counter) + " packets."
    print "saved anon file to "+f+"-anon.pcap"
    pcap = []
    gc.collect()
