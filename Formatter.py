#!/bin/python3

import re
from os.path import exists
from os import strerror
import errno
""" This Class is Used to format the Document ready for parser"""

class Formatter:
	def __init__(self):
		""" Initialisation of Formatter class with different types of comments"""
		self.python_comment = r"#.*"
		self.c_comment = re.compile(
        		r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        		re.DOTALL | re.MULTILINE
    		)
	def formatDoc(self, filepath):
		""" Format file with removing all the comments from it.
			Attributes
			----------
			filepath - str 
				path of the file"""
		file = exists(filepath)
		if not file:
			raise FileNotFoundError(errno.ENOENT, strerror(errno.ENOENT), filepath)
		else:
			file_data = open(filepath, "r").read()
			file_data = re.sub(self.python_comment,'',file_data)
			file_data = re.sub(self.c_comment,'',file_data)
			return file_data
	
		
