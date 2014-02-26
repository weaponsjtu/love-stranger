#!/usr/bin/env python
import os
import sys

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

if __name__ == "__main__":
	print sys.path
	sys.path.append(BASE)
	print sys.path
	#import imp
	#imp.find_module('settings') # Assumed to be in the same directory.
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fclover.settings")

	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
