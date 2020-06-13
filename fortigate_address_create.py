# Script created by aa@aztek.xyz
# Please send all questions,bugs to aa@aztek.xyz

from csv import reader
import os
import sys

#gets current file path
cwd = os.getcwd()

# gets sys platform for last line of script
os_platform = sys.platform

open_file = open('ip_addresses.csv')
read_file = reader(open_file)

# makes file contents a dict
addresses = dict(read_file)

# removes column headers
del addresses["IP Address"]

num_of_addr = len(addresses)


# a dict of cidr notation
cidr_dict = {'/32': '255.255.255.255', '/31': '255.255.255.254', '/30': '255.255.255.252', '/29': '255.255.255.248', '/28': '255.255.255.240', '/27': '255.255.255.224', '/26': '255.255.255.192', '/25': '255.255.255.128', '/24': '255.255.255.0', '/23': '255.255.254.0', '/22': '255.255.252.0', '/21': '255.255.248.0', '/20': '255.255.240.0', '/19': '255.255.224.0', '/18': '255.255.192.0', '/17': '255.255.128.0', '/16': '255.255.0.0', '/15': '255.254.0.0', '/14': '255.252.0.0', '/13': '255.248.0.0', '/12': '255.240.0.0', '/11': '255.224.0.0', '/10': '255.192.0.0', '/9': '255.128.0.0', '/8': '255.0.0.0', '/7': '254.0.0.0', '/6': '252.0.0.0', '/5': '248.0.0.0', '/4': '240.0.0.0', '/3': '224.0.0.0', '/2': '192.0.0.0', '/1': '128.0.0.0', '/0': '0.0.0.0'}


# new txt script is created
fgt_script = open("fortigate_address_add.txt", "w")

print("===========")
print("There is " + str(num_of_addr) + " addresses listed in ip_addresses.csv\n")
input("Press enter to continue or press ctrl+c to stop")
print("Starting script...\n===========")
print("  IP Address         Subnet")
print("  ----------         ------")

new_script = open("fortigate_address_add.txt", "w")
new_script.write("config firewall address\n\n")

for addr, subnet in addresses.items():
    
#  Looks up subnet value and assigns cidr notation to cidr var
    for cidr_key,cidr_subnet in cidr_dict.items():
        if cidr_subnet == subnet:
            cidr = cidr_key

# Writes fortigate script to file
    new_script.write("edit {addr}{cidr}\nset subnet {addr} {subnet}\nnext\n\n".format(addr=addr, cidr=cidr, subnet=subnet))
    print("Added {addr}    {subnet}".format(addr=addr, subnet=subnet))


new_script.write("end\n")
new_script.close()


print("===========\nScript finished!\n")

if os_platform == "win32":
    print("Saved script at " + cwd + "\\fortigate_address_add.txt")

else:
    print("Saved script at " + cwd + "/fortigate_address_add.txt")
