#!/bin/python3

from  Formatter import *
def main():
	print("main function")
	formatter = Formatter()
	data = formatter.formatDoc("sys_config.txt")
	print(data)



if __name__ == "__main__":
	main()
