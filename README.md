# APS_TrafficProject

## Necessary installations
- [Python](https://www.python.org/downloads/)
- [SUMO](http://sumo.dlr.de/wiki/Installing)

To test:  
Open a command line, run `python test.py`. The SUMO GUI should open and allow you to run the simulation.

## Getting started

You can design your own road network by modifying the files in the /data folder (see SUMO documention [here](http://sumo.dlr.de/wiki/Tutorials/Hello_Sumo))

Notes:
- After changing the nodes and edges, in the command line `cd data` and then `netconvert --node-files=hello.nod.xml --edge-files=cross.edg.xml --output-file=cross.net.xml`
- Routes are generated automatically in the `generate_routefile()` method in `runner.py`

