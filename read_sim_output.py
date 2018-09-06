import xml.etree.ElementTree as ET
import os

output_file = 'TraCI/data/cross.out'

def return_sars():
	os.chdir("/Users/canmanie/Documents/LearnSDM/Code/SDM_Traffic/") ##dangerous to hard code this
	tree = ET.parse(output_file)
	root = tree.getroot()
	state = { 0: [0,0,0,0,0,0] }
	action = { 0: 0 }
	sars = []
	old_phase = 0
	interval = 1 #time step
	step = 10 #accumulating rewards
	total_reward = 0
	last_step_rewards = []
	old_phase = 0
	
	reward = read_rewards()
	
	for child in root:
		if child.tag=='interval':
			time = int(float(child.attrib['end']))
			if 'meanTimeLoss' in child.attrib and (child.attrib['id']=="fA" or child.attrib['id']=="iA0" or child.attrib['id']=="iA1" or child.attrib['id']=="CA" or child.attrib['id']=="BA0" or child.attrib['id']=="BA1"):
				n_veh = float(child.attrib['nVehEntered'])
				n_seen = float(child.attrib['nVehSeen'])

				if  (int(float(child.attrib['end'])))%interval==0:
					
					if state.get(time)==None:
						state[time] = [n_seen]
					else:
						state[time].append(n_seen)
			
# 			if 'flow' in child.attrib and (int(float(child.attrib['time'])))%interval==0:
#  				continue
# # 				if state.get(time)==None:
# # 					int_s = int(float(child.attrib['nVehEntered']))
# # 					#int_s = int(float(child.attrib['speed']))
# # 					state[time] = [int_s]
# # 				else:
# # 					int_s = int(float(child.attrib['nVehEntered']))
# # 					#int_s = int(float(child.attrib['speed']))
# # 					state[time].append(int_s)

		#action list
		# 0: NO CHANGE
		# 1: phase to next phase
			
		if child.tag=='tlsState' and (int(float(child.attrib['time'])))%interval==0:
			current_phase = int(float(child.attrib['phase']))
			time = int(float(child.attrib['time']))
						
			if current_phase==1 or current_phase==2:
				action[time]=1
			if current_phase==3 or current_phase==0:
				action[time]=0
				
			old_phase = current_phase
			
# 		elif child.tag=='tlsState' and (int(float(child.attrib['time'])))%interval==0: 
# 			time = int(float(child.attrib['time']))
# 			state[time].append(int(float(child.attrib['phase'])))
				
	## adding next states
	for key in state:
		if state.get(key+interval)!=None and action.get(key+interval)!=None:
			sars.append([state[key],action[key+interval],reward[key],state[key+interval]])
		
	return sars
	
def read_rewards():	
	tree = ET.parse('TraCI/emissions.xml')
	root = tree.getroot()
	
	reward = { 0: 0 }
	
	for child in root:
		if child.tag=='timestep':
			time=int(float(child.attrib['time']))
			reward[time]=0
			
			if len(child):
				for vehicle in child:
					reward[time] += int(float(vehicle.attrib['CO']))*-1
					
	reward[time+1]=0 #there seems to be an extra time check?? this is hacky
	
	return reward