#! /usr/bin/env python
# -*- coding: utf-8 -*-

# DaVinci Resolve V16 export to DRP all projects and delete projects in current folder
# Copyright 2019 Igor Riđanović, www.metafide.com, www.hdhead.com

from python_get_resolve import GetResolve
import os

def export_drp():

	projs = pm.GetProjectsInCurrentFolder()
	for i in projs.values():
		pm.ExportProject(i, os.path.join(path, i))

		# Uncomment to delete projects after export		
		#pm.DeleteProject(i)

if __name__ == '__main__':

	# Instantiate Resolve objects
	resolve = GetResolve()
	pm      = resolve.GetProjectManager()

	# Set the path to the DRP export directory
	path = ''
