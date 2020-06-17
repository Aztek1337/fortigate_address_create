# Fortigate Address Create

## This script makes a Fortigate script for adding subnet address objects.

## Steps

Requires python 3.7.x or higher

1.  Add IP addresses with the full subnet masks into the csv file named "ip_adresses.csv"
    1.  Entries must be placed beneath the column headers.
    2. Each Entry must be on it's own line.
    2.  Ip address must be first, followed by full subnet mask (Example: 255.255.255.0)
    3.  Save and keep the same file name.
    4. run script by using Python, from cmd line,Powershell or BASH `python fortigate_address_create.py` 

2.  Run script, the last line of script will tell you where it output the Fortigate script at.
