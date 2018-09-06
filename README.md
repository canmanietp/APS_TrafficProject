# APS_TrafficProject

## Necessary installations
- [Python](https://www.python.org/downloads/)
- [SUMO](http://sumo.dlr.de/wiki/Installing)

To test:  
Open a command line, run `python test.py`. The SUMO GUI should open and allow you to run the simulation.

## Getting started

You can design your own road network by modifying the files in the /data folder (see SUMO documention [here](http://sumo.dlr.de/wiki/Tutorials/Hello_Sumo))

Notes:
- After modifying files in the data folder, run in the command line `cd data` and then `netconvert --node-files=cross.nod.xml --edge-files=cross.edg.xml --output-file=cross.net.xml`
- Routes are generated automatically in the `generate_routefile()` method in `runner.py`. This can be modified to change the probability distributions of vehicle departures and the paths of the vehicles.

### Induction loops and edge detectors
The example code includes two induction loops on the southbound side of the 

<center><img src="https://i.imgur.com/AD7UWeC.png" width="200" height="200" /></center>

Printed in `cross.out`
