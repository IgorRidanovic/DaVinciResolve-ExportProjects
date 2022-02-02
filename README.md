# DaVinciResolve-ExportProjects
Export all DaVinci Resolve projects from the current folder to DRP and delete the projects.

This script requires DaVinci Resolve Studio V16 or above. We import the API using the canonical Blackmagic Design implementation. This is not the only OS portable way to import the API library. Read the developer documentation that ships with Resolve if unable to create a resolve instance.

If writing an automated DRP export tool consider that Resolve Studio must be running and that each ExportProject() call will block the application. Generally speaking, a database dump is a more end-user transparent DaVinci Resolve backup method.

YouTube tutorial for exporting Resolve DRP files using the Blackmagic API: https://youtu.be/a8au-dJEZ5Y

See DaVinci Resolve disk database backup: https://www.hdhead.com/?p=841 
DaVinci Resolve PostgreSQL backup: https://www.hdhead.com/?p=857
