#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def nmap_scan(report, report_path, target_ip):
    print("========== Try to get OS info ================")

    print("Report path is: " + report_path)
    print("Target address is: " + target_ip)

    command_string="nmap -O "+target_ip

    os.system(command_string)
    fun_d = os.popen(command_string)
    raw_data = fun_d.read()

    print(raw_data)
    raw_data="========== OS info =============\n"+raw_data+"================================\n"

    if(report == "doreport"):
        print("Writing report file to: " + report_path)
        fil_d = open(report_path, "w")
        fil_d.write(raw_data)
        fil_d.close()

if __name__ == '__main__':
    nmap_scan()