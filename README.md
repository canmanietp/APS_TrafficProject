# CS4010 Traffic Simulation Guide

## Necessary installations
- [Python](https://www.python.org/downloads/)
- [SUMO](http://sumo.dlr.de/wiki/Installing)
	- You will need to set the environment variable `SUMO_HOME` to the base directory of your installation. This can be done temporarily by running `export SUMO_HOME="/your/path/to/sumo"`. More details [here](http://sumo.dlr.de/wiki/Basics/Basic_Computer_Skills).

You will also be using [TraCI](http://www.sumo.dlr.de/userdoc/TraCI.html) to interface with SUMO on-line using Python. TraCI comes bundled with SUMO.

**To test your installations**:  
Open a command line, run `python test.py`. The SUMO GUI should open and allow you to play the simulation.

## Getting started

You can design your own road network by modifying the files in the `/data` folder (see SUMO tutorial [here](http://sumo.dlr.de/wiki/Tutorials/Hello_Sumo))

Notes:
- After modifying node and edge files, run `netconvert --node-files=cross.nod.xml --edge-files=cross.edg.xml --output-file=cross.net.xml` in the data folder to generate the net file.
- Routes are generated automatically by the `generate_routefile()` method in `runner.py`. This can be modified to change the probability distributions of vehicle departures and the paths of the vehicles.
- Outside of testing, you will likely want to run your simulations without the GUI. This can be done by calling the method `simulate_n_steps(N,'nogui')` in `runner.py` with `'nogui'`.

### Induction loops and lane area detectors
[Induction loops](http://sumo.dlr.de/wiki/Simulation/Output/Induction_Loops_Detectors_(E1)) and [lane area detectors](http://sumo.dlr.de/wiki/Simulation/Output/Lanearea_Detectors_(E2)) provide information about the state of the network at that area of interest. 

The example code includes two induction loops (the yellow rectangles in diagram below) in the network and one lane area detector (the blue strip), defined in `data/cross.det.xml`.

<p align="center"><img src="https://i.imgur.com/IiYIlLC.png" width="350" height="350" /></p>

The state of these can be read on-line during the simulation using TraCI. See the documentation for [induction loops](http://sumo.sourceforge.net/pydoc/traci._inductionloop.html) and [lane area detectors](http://sumo.sourceforge.net/pydoc/traci._lanearea.html). For example, `traci.inductionloop.getLastStepVehicleNumber("nA0")` will return  the number of vehicles that were on the induction loop `nA0` within the last simulation step. Make sure to read the documentation both from SUMO and TraCI to know how to interpret these variables.

An output summary of elements listed in `data/cross.det.xml` is printed in `data/cross.out` after the simulation is run, where the state of each detector/induction loop/traffic signal etc. is printed at the time step interval defined by `freq` in the element  definition. 

### Traffic lights
A node is indicated to be a traffic-signal-controlled intersection in `data/cross.nod.xml`. The phases of the signal can be defined in `data/cross.det.xml`; see http://sumo.dlr.de/wiki/Simulation/Traffic_Lights for further explanation on signal phases.

Using TraCI, the current phase of the signal can be read or set. For example, `traci.trafficlight.setPhase("A",0)` will set the phase of light `A` to 0. Further documentation on controlling and reading lights with TraCI is [here](http://www.sumo.dlr.de/daily/pydoc/traci._trafficlight.html#TrafficLightDomain-setPhase).
