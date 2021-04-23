#!/usr/bin/env python

import subprocess
import optparse

#Author = Kimanxo
print(" ")
print(" ")
print("===[WELCOME TO Xmac CHANGER SCRIPT]===")
print(" ")


def get_args(): #a function to get options form the user 
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest = "interface", help = "Interface To Change It's Mac Adress")
	parser.add_option("-m", "--mac", dest = "mac", help = "The New  Mac Adress")
	(options, arguments) =  parser.parse_args()
	if not options.interface :
		parser.error("please specify the interface and a new mac adress , type -h for more HELP")		
	elif not options.mac :
		parser.error("please specify the interface and a new mac adress , type -h for more HELP")		
	return options	

def change_mac(interface, mac): #a function to change the Mac 
	print('Changing The Mac Adress For ' + interface + ' to ' +  mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", mac])
	subprocess.call(["ifconfig", interface, "up"])
options = get_args()
change_mac(options.interface, options.mac) #excuting the function 

