# pyez-network-testing

### Nano framework for network testing with Junos PyEZ, with some example scripts

You always want to make sure the functionality of your network does not degrade after upgrading software, committing configurations, or
changing a physical topology. Even during normal operations there is always a need to check your work. This repository contains examples on how to automate checks of your network’s health using Junos PyEZ.

### Problem

Administering networks requires a lot of repetitive tasks. Automating network administration, on the other hand, is a way to increase effectiveness, reduce downtime, and release human resources for more creative tasks. 

Network automation comes in numerous flavors. You can automate configuration, monitoring, and event processing. You can write on-box
scripts or orchestrate off-box, from a central server. Different possibilities lead to an initial question – where should you start automation efforts?

It makes sense to start with automating network monitoring, not only because it is very valuable, but because it allows you to feel the automation power while occupying a space in which it’s safer to experiment (when compared to configuration automation).

Typically, to make sure your network is operating normally, you log in to several devices and check the command outputs (e.g., show bgp
summary). Alternatively, you might look at graphs that represent different counters and values (such as CPU load, interface throughput, etc.). Here, you will see how to do it with Junos PyEZ, a powerful yet simple library for automating Junos-based devices.

### Solution

The base [script](https://github.com/pklimai/pyez-network-testing/blob/master/pyez-network-testing.py) of the nano framework calls all tests that you create. The actual tests must be placed in other files in the same directory, with names tests_XXX.py. 

For the example [topology](https://github.com/pklimai/pyez-network-testing/blob/master/TOPOLOGY/example-network-topology.tif) and the set of test scripts contained in repository, the result of a test run might be the following:

```
$ python pyez-network-testing.py
Running tests for R1
Running test_R1_arp_gateway... pass
Running test_R1_bgp_default... pass
Running test_R1_ospf... pass
Running test_all_chassis_alarms... pass
Running test_all_core_dumps... pass
Running test_all_system_alarms... pass
Running test_all_total_memory_percent_util... pass
Running tests for R2
Running test_R2_arp_gateway... pass
Running test_R2_bgp_peers_established... pass
Running test_R2_ospf... pass
Running test_all_chassis_alarms... pass
Running test_all_core_dumps... pass
Running test_all_system_alarms... pass
Running test_all_total_memory_percent_util... pass
Running tests for R3
Running test_R3_bgp_default... pass
Running test_R3_ospf... pass
Running test_R3_ping_ISP1_GW... pass
Running test_R3_ping_ISP2_GW... pass
Running test_all_chassis_alarms... pass
Running test_all_core_dumps... pass
Running test_all_system_alarms... pass
Running test_all_total_memory_percent_util... pass
--------
Network test script finished. Successful tests: 22, failed tests: 0
All went OK.
```

More details are explained in Chapter 6 of this book, which is free to download for J-net members:
https://www.juniper.net/us/en/training/jnbooks/day-one/networking-technologies-series/cookbook-2017/

