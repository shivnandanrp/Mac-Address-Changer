#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():

    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="The interface which needs to changed")


    parser.add_option("-m", "--mac", dest="new_mac", help="To set new mac address for the interface")

    return parser.parse_args()

def change_mac(interface, new_mac):


    print("[+] The mac address will be changed  in interface " + interface + " to " + new_mac)

    subprocess.call(["ifconfig ", interface, " down"])
    subprocess.call(["ifconfig ", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig ", interface, "up"])




(options, arguments) = get_arguments()

change_mac(options.interface, options.new_mac)





