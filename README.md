Freddy Maidanik 310017280 - corresponding member.
Eli Moshkovich 308240019
Roy Greenberg 201559994
Daniel Bromberg 209529882

How to run:
First, take the firewall and the slice files into the folder: pox/pox/misc
To run the firewall topology, you should open 2 terminals.
The first terminal should be in your first pox folder, and write: ./pox.py log.level --WARNING misc.firewall
The second terminal should be where your topo file is located, and write: sudo python topo.py

After both of them are running, you can write pingall to see which connections are up. We have 2 rules for the firewall, there shouldn't be any connection between h1 and h4, and h2 and h3.
If all is okay, you can exit.

For the video slicing, you need to write on the first terminal: ./pox.py log.level --WARNING misc.slice
The second one should be exactly the same: sudo python topo.py

After both of them are running, on the mininet write:
h4 iperf -s -p 10000 &
h4 iperf -s -p 22 &&
h2 iperf -c h4 -p 10000 -t 2 -i 1
We should get a connection between h2 and h4 via the video and it should be approximetly 10Mbits/sec.
To see the non-video, try:
h2 iperf -c h4 -p 22 -t 2 -i 1
It should be approximetly 1Mbits/sec.

To check if the firewall rule between h1 and h4 is not working, just exit the mininet and run all the lines from above. Except h2, run as h1. You shouldn't have a connection.


IMPORTANT:
To change the firewall policies, you should change the rules at both the firewall and slice files.
We made the possibility to block up to 3 rules, we can have none as well so all hosts could get a signal. To change it to more than 3 rules, it shouldn't take any more than a minute to change.

