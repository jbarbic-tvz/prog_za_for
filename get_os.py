#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def nmap_scan(report, report_path, target_ip):
    print("DO SCAN")
    if(report == "doreport"):
        print("Report shall be created")
    else:
        print("Report shall not be created")
    print("Report path is: " + report_path)
    print("Target address is: " + target_ip)

    command_string="nmap -O "+target_ip

    os.system(command_string)
    f = os.popen(command_string)
    raw_data = f.read()
    print(raw_data)

if __name__ == '__main__':
    nmap_scan()