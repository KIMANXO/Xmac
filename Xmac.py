#!/usr/bin/env python3

print(" ")
print(" ")
print("===[WELCOME TO Xmac CHANGER SCRIPT]===")
print(" ")
import subprocess
import optparse

def get_args():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest = "interface", help = "Interface To Change It's Mac Adress")
	parser.add_option("-m", "--mac", dest = "mac", help = "The New  Mac Adress")
	(options, arguments) =  parser.parse_args()
	if not options.interface :
		parser.error("please specify the interface and a new mac adress , type -h for more HELP")		
	elif not options.mac :
		parser.error("please specify the interface and a new mac adress , type -h for more HELP")		
	return options	

def change_mac(interface, mac):
	print('Changing The Mac Adress For ' + interface + ' to ' +  mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", mac])
	subprocess.call(["ifconfig", interface, "up"])
options = get_args()
change_mac(options.interface, options.mac)

