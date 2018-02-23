# 2017-SUEE-data-set

Data sets can be downloaded here:

| data set      | start date    | duration | #hosts |
| ------------- |:------------- | -----: |-----: |
| [SUEE1](https://github.com/vs-uulm/2017-SUEE-data-set/releases/download/v1.0/SUEE1.pcap "24h traffic on 2017-11-02")        | 2017-11-02    | 24 h | 1634 |
| [SUEE8](https://github.com/vs-uulm/2017-SUEE-data-set/releases/download/v1.0/SUEE8.pcap "8d traffic from 2017-11-05")       | 2017-11-05    |  8 d | 8286 |

The data sets contain traffic in and out of the web server of the [Student Union Electrical Engineering (Fachbereichsvertretung Eletrotechnik) at Ulm University](https://fs-et.de).

The data was mixed with attack traffic. The attacks contained in these data sets are:

 * 50 attackers running [slowloris](https://github.com/gkbrk/slowloris) (IP addresses 10.128.0.1 to 10.128.0.50)
 * 50 attackers running [slowhttptest](https://github.com/shekyan/slowhttptest) (IP addresses 10.128.0.50 to 10.128.0.100)
 * 50 attackers running [slowloris-ng](https://github.com/vs-uulm/slowloris-ng) (IP addresses 10.128.0.100 to 10.128.0.150)

Caution: because of an of-by-one error, the IP addresses 10.128.0.50 and 10.128.0.100 are used twice. In our own evaluation, we therefore choose to omit any packets sent or received by these clients completely.

The IP and MAC addresses of the benign clients were anonymized with [anon.py](https://github.com/vs-uulm/2017-SUEE-data-set/blob/master/anon.py), all IP addresses in the anonymized data sets are in the 192.168.0.0/16 block. The original IP addresses were in part from the Ulm University network and mostly from diverse networks in Ulm and surrounding areas. Keep in mind, that the same IP address in SUEE1 and SUEE8 are not affiliated. However, every packet sent (or received) by an IP within one data set was originally sent (or received) by the same node.

## Attacker Configuration

The attacking tools were adapted to allow IP spoofing to simulate distributed attacks and were left in standard configuration apart from that. The parameters for slowhttptest were 30 seconds intervals, 8192
bytes for the Content-Length header, 10 bytes POST-body length per packet and one socket per client. Slowloris is also configured to use only one socket per client. The default configuration was left in place in all other settings, resulting in a packet interval of 15 seconds.

Slowloris-ng includes several changes to the original slowloris. The additional features implement randomized behavior, which is configured to send in intervals of 15 seconds with a randomization interval of 5 seconds and sending the header lines as bursts of single messages per character.

# Contact

For questions, please contact [Thomas Lukaseder](https://www.uni-ulm.de/?seder).

# Acknowledgment

We like to thank the Student Union Electrical Engineering (Fachbereichsvertretung Elektrotechnik) at Ulm University and Philipp Hinz in particular for providing the necessary data.

This work was supported in the bwNET100G+ project
by the Ministry of Science, Research and the Arts Baden-
Württemberg (MWK).

