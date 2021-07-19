# Trouble Shooting Tools

## Traceroute
- `Traceroute` displays the path a packet takes to get to remote device by using `IP packet Time to Live (TTL)`
```
traceroute [DNS name] or [IP Address]
```
## if config
- `ifconfig` is used to both view and configure the TCP/IP protocol
```
ifconfig interface [address [parameters]]
```
## iptables
- `iptables` uses following chains to allow or disallow traffics
	- Input
	- Output
	- Forward
```
Block a connection from the device 192.168.10.1
iptables -A INPUT -s 192.168.10.1 -j DROP
```
```
Block all conections from all devices in 172.16.0.0/16 network
iptables -A INPUT -s 172.16.0.0/16 -j DROP
```
```
Blosk SSH connections from 10.110.61.5
iptables -A INPUT -p tcp --dport ssh -s 10.110.61.5 -j DROP
```
```
BLock SSH connections from any IP address
iptables -A INPUT -p tcp --dport ssh -j DROP
```

## Ping
- `ping` is used to find out; if host a responding - if you can reach a host
```
ping hostname or IP address
```

## Arp
- `ARP` is used to translate TCP/IP addresses to MAC addresses using broadcasts
```
arp -a displays the current ARP table
```

## nslookup
- `nslookup` utility allows you to query a name server and quickly find out which name resolves to which IP address
```
nslookup [option]
```
## nmap
- `nmap` is popular port scaining tool

## route
- `route` is used to manipulate network routing table
```
route print
```
## netstat
- `netstat` checks out the inbound and outbound TCP/IP connections on your machine
```
netstat -a: Displays all TCP/IP and UDP connections
netstat -e: Displays summary of all the packets
```
## tcpdump
- `tcpdump` used to read either packets captured live from a network or packetsthat have been saved a file
```
tcpdump -i any: Captures traffic on all interfaces
tcpdump -i [eth0]: Captures traffic on a particular interface
```

## ftp
- `file transfer protocol` is used for the transfer of files
```
ftp
```
## telnet and ssh
- `telnet` allows you to make connections to remote devices, gathering information
- `ssh` provides same options as `telnet` plus a lot more and transfers the data in encrypted
```
ssh user-name@host(IP or Domain Name)
```

## scp amd curl
- `scp` command-line tool which is used to transfer files and directories accroos the system
```
scp <options> <files_or_directories> user@target-host:/<folder>
```
- `curl` command-line tool to transfer data to or from a server, using any of the supported protocols
```
curl [options] [URL..]
```

