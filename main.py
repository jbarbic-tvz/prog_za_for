#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import operator
from pathlib import Path

# tools
import get_os

def final_report(path_dest):
    full_report="full_report.txt"
    print("Do final report from sub reports...")

    # delete old final report
    os.system("rm full_rport.txt")

    # iterate over reports
    pathlist = Path("/home/josip//workbench/workspace-py/prog_za_for/").glob("report*")
    for path in pathlist:
        # because path is object not string
        path_str = str(path)
        print(path_str)
        file_rd = open(path_str, "r")
        read_from=file_rd.read()
        print(read_from)
        print("Writing report file to: " + full_report)
        fil_d = open(full_report, "a")
        fil_d.write(read_from)
        fil_d.close()

def main():
    # default configuration
    report_status="doreport"
    target_address="192.168.1.1"
    final_report_path="report_full.txt"
    # circular menu
    subs = {}
    subs["1"]="Scan ports"
    subs["2"]="Get OS version"
    subs["3"]="do stuf 3"
    subs["4"]="Create report"
    subs["5"]="Delete reports"
    subs["6"]="Print current configuration"
    subs["7"]="Set report output"
    subs["8"]="Set target IP"
    subs["9"]="Exit"
    # repeat until 0 exit is selected
    while True:
        options=subs.keys()
        options=sorted(options)
        for entry in options:
            print(entry, subs[entry])

        selection=input("Select from listed:")
        if (selection == 1):
            print("Prot scan")
            os.system("./port_scan.py arg1 arg2")
        elif (selection == 2):
            print ("Geting OS version")
            get_os.nmap_scan(report_status,"report_get_os.txt",target_address)
        elif (selection == 3):
            print("do 3")
        elif (selection == 4):
            print("Creating full report...")
            final_report(final_report_path)
        elif (selection == 5):
            print("Deleting reports")
            os.system("rm repor*")
        elif (selection == 6):
            print("Current configuration:")
            print("Report output: " + report_status)
            print("Target address: " + target_address)
        elif (selection == 7):
            print("Please set report output (default doreport)")
            report_status=input("Set [doreport | noreport]: ")
        elif (selection == 8):
            print("Please set target IP (default 192.168.1.1)")
            target_address=input("Set target IP: ")
        elif (selection == 9):
            break
        else:
            print("Unrecognized option!")

if __name__ == "__main__":
    main()
