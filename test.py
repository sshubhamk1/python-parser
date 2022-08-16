#!/bin/python3


import re
def show(module):
	for grp in module.keys():
		print(f"[{grp}]")
		for key in module[grp].keys():
			print(f"\n{key} = {module[grp][key]}")
			

words = {"core0":{"pci":"01:02:03.a", "key":"value"}, "core2":{"pci":"02:03:02.4", "ip": "127.0.0.1"}}
f = open("sys_config.txt", "r").read()
print("before regex")
print(f)
print("after regex")
f = re.sub("\/\/.*",'',f)
f = re.sub("#.*",'',f)
f = re.sub("\/\*.*\*\/",'',f)
print(f)
#for line in f.readlines():
#	print(line)
#f.close()
#show(words)
