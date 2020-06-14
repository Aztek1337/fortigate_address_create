# Script created by aa@aztek.xyz
# Please send all questions,bugs to aa@aztek.xyz

from csv import reader
from pathlib import Path
import os, sys

#gets current file path
cwd = os.getcwd()

# gets sys platform
os_platform = sys.platform

open_file = open('ip_addresses.csv')
read_file = reader(open_file)

# makes file contents a dict
addresses = dict(read_file)

# removes column headers
del addresses["IP Address"]

num_of_addr = len(addresses)


# a dict of cidr notation for script to refernece
cidr_dict = {'/32': '255.255.255.255', '/31': '255.255.255.254', '/30': '255.255.255.252', '/29': '255.255.255.248', '/28': '255.255.255.240', '/27': '255.255.255.224', '/26': '255.255.255.192', '/25': '255.255.255.128', '/24': '255.255.255.0', '/23': '255.255.254.0', '/22': '255.255.252.0', '/21': '255.255.248.0', '/20': '255.255.240.0', '/19': '255.255.224.0', '/18': '255.255.192.0', '/17': '255.255.128.0', '/16': '255.255.0.0', '/15': '255.254.0.0', '/14': '255.252.0.0', '/13': '255.248.0.0', '/12': '255.240.0.0', '/11': '255.224.0.0', '/10': '255.192.0.0', '/9': '255.128.0.0', '/8': '255.0.0.0', '/7': '254.0.0.0', '/6': '252.0.0.0', '/5': '248.0.0.0', '/4': '240.0.0.0', '/3': '224.0.0.0', '/2': '192.0.0.0', '/1': '128.0.0.0', '/0': '0.0.0.0'}


# new "output" dir is created and txt script is created
Path("Output").mkdir(parents=True, exist_ok=True)

if os_platform == "win32":
    new_script = open("Output\\fortigate_address_add.txt", "w")
else:
    new_script = open("Output/fortigate_address_add.txt", "w")

print("===========")
print("There is " + str(num_of_addr) + " addresses listed in ip_addresses.csv\n")

addr_group_quest = input("Would you lik these addresses added as a new address group object? (y/n): ")
addr_group_quest = addr_group_quest.lower()

if addr_group_quest == "y":
    addr_group_name = input("Please input a name for this new address group: ")

print("Starting script...\n===========")
print("  IP Address         Subnet")
print("  ----------         ------")

new_script.write("config firewall address\n\n")

# List of addess object names
address_objects = []

for addr, subnet in addresses.items():

#  Looks up subnet value and assigns cidr notation to cidr var
    for cidr_key,cidr_value in cidr_dict.items():
        if cidr_value == subnet:
            cidr = cidr_key

# Adds address object names to address_objects list
    address_object = str(addr) + str(cidr)
    address_objects.append(address_object)

# Writes fortigate script to file
    new_script.write("edit {addr}{cidr}\nset subnet {addr} {subnet}\nnext\n\n".format(addr=addr, cidr=cidr, subnet=subnet))
    print("Added {addr}    {subnet}".format(addr=addr, subnet=subnet))


new_script.write("end\n")
new_script.close()

# Write new address object group script
if addr_group_quest == "y":

# wraps each object in double qoutes
    address_objects_quotes = []
    for addrobj in address_objects:
        addrobj =  "\"" + addrobj + "\""
        address_objects_quotes.append(addrobj)

# creates str from list, seperated by a space
    address_str = " ".join(address_objects_quotes)

    if os_platform == 'win32':
        new_addr_group_script = open("Output\\fortigate_address_group_create.txt", "w")
    else:
        new_addr_group_script = open("Output/fortigate_address_group_create.txt", "w")

    new_addr_group_script.write("config firewall addgrp\n\n")
    new_addr_group_script.write("edit {addgrpname}\n\n".format(addgrpname=addr_group_name))
    new_addr_group_script.write("set member {addr_str}\n\n".format(addr_str=address_str))
    new_addr_group_script.write("next\n\n")
    new_addr_group_script.write("end\n\n")

print("===========\nScript finished!\n")

if os_platform == "win32":
    if addr_group_quest == "y":
         print("Saved address add script at " + cwd + "\\Output\\fortigate_address_add.txt")
         print("Saved address group create script at " + cwd + "\\Output\\fortigate_address_group_create.txt")
    else:
         print("Saved script at " + cwd + "\\Output\\fortigate_address_add.txt")

else:
    if addr_group_quest == "y":
         print("Saved address add script at " + cwd + "/Output/fortigate_address_add.txt")
         print("Saved address group create script at " + cwd + "/Output/fortigate_address_group_create.txt")
    else:
         print("Saved script at " + cwd + "/Output/fortigate_address_add.txt")