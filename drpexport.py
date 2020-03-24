#! /usr/bin/env python
# -*- coding: utf-8 -*-

# DaVinci Resolve V16 export to DRP all projects in the current folder.
# Copyright 2019 Igor Riđanović, www.metafide.com, www.hdhead.com

from python_get_resolve import GetResolve
import os

def export_drp(p):

	projs = pm.GetProjectsInCurrentFolder()

	for i in projs.values():

		try:
			pm.ExportProject(i, os.path.join(p, i))
		except TypeError:
			print 'This script requires DaVinci Resolve 16.'
			return None

		print 'Exported', i

	return True


if __name__ == '__main__':

	# Instantiate Resolve objects
	resolve = GetResolve()
	pm      = resolve.GetProjectManager()

	# Set the path to the DRP export directory
	path = ''

	if export_drp(path):
		print 'Export completed.'
