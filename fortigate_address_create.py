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
    new_script.write("edit {addr}\nset subnet {addr} {subnet}\nnext\n\n".format(addr=addr, subnet=subnet))
    print("Added {addr}    {subnet}".format(addr=addr, subnet=subnet))


new_script.write("end\n")
new_script.close()


print("===========\nScript finished!\n")

if os_platform == "win32":
    print("Saved script at " + cwd + "\\fortigate_address_add.txt")

else:
    print("Saved script at " + cwd + "/fortigate_address_add.txt")