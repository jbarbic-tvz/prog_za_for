#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

# tools
import get_os

def main():
    # circular menu
    subs = {}
    subs["1"]="Scan ports"
    subs["2"]="Get OS version"
    subs["3"]="do stuf 3"
    subs["4"]="Create report"
    subs["5"]="Delete reports"
    subs["9"]="Exit"
    # repeat until 0 exit is selected
    while True:
        options=subs.keys()
        sorted(options)
        for entry in options:
            print(entry, subs[entry])

        selection=input("Select from listed:")
        if selection =='1':
            print("Prot scan")
            os.system("./port_scan.py arg1 arg2")
        elif selection == '2':
            print ("Geting OS version")
            get_os.nmap_scan("doreport","report_get_os.txt","192.168.1.71")
        elif selection == '3':
            print("do 3")
        elif selection == '4':
            print("Creating report")
        elif selection == '5':
            print("Deleting reports")
        elif selection == '0':
            break
        else:
            print("Unrecognized option!")

if __name__ == "__main__":
    main()
