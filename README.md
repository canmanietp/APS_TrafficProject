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

### Induction loops and lane area detectors
[Induction loops](http://sumo.dlr.de/wiki/Simulation/Output/Induction_Loops_Detectors_(E1)) and [lane area detectors](http://sumo.dlr.de/wiki/Simulation/Output/Lanearea_Detectors_(E2)) provide information about the state of the network at that area of interest. 

The example code includes two induction loops (the yellow rectangles in diagram below) in the network and one lane area detector (the blue strip), defined in `data/cross.det.xml`.

<center><img src="https://i.imgur.com/Pw2JoYR.png" width="350" height="350" /></center>

The state of these can be read on-line during the simulation using TraCI. See the documentation for [induction loops](http://sumo.sourceforge.net/pydoc/traci._inductionloop.html) and [lane area detectors](http://sumo.sourceforge.net/pydoc/traci._lanearea.html). For example, `traci.inductionloop.getLastStepVehicleNumber("nA0")` will return  the number of vehicles that were on the named induction loop within the last simulation step. Make sure to read the documentation both from SUMO and TraCI to know how to interpret these variables.

An output summary of objects listed in `data/cross.det.xml` is printed in `data/cross.out` after the simulation is run, where the state of each detector/induction loop/traffic signal etc. is printed at the time step interval defined by `freq` in the object definition. 
