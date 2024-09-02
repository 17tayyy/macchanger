#!/usr/bin/env python3

import argparse
import re
from termcolor import colored
import signal
import sys
import subprocess

def def_handler(sig, frame):
    print(colored(f"\n[!] Saliendo del programa...\n", 'red'))

signal.signal(signal.SIGINT, def_handler)

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para cambiar la direccion MAC de una interfaz de red")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Nombre de la interfaz de red")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="Nueva direccion MAC para la interfaz de red")

    return parser.parse_args()

def is_valid_input(interface, mac_address):

    is_valid_interface = re.match(r'^[e][n|t][s|h]\d{1,3}$', interface)
    is_valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address)

    return is_valid_interface and is_valid_mac_address

def change_mac_address(interface, mac_address):

    if is_valid_input(interface, mac_address):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw",  "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])

        print(colored(f"\n[+] La dirección MAC ha sido cambiada", 'green'))
    else:
        print(colored(f"\n[!] Los datos introducidos no son correctos", 'red'))

def main():
    args = get_arguments()
    change_mac_address(args.interface, args.mac_address)
    

if __name__ == '__main__':
    main()
