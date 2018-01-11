'''
By storing port numbers here, we can easily change the "wiring" of the robot
from a single location. Instantiate a PortsList for each subsystem and assign
port numbers as needed.
'''

class PortsList:
    '''Dummy class used to store variables on an object.'''
    pass
    


singlemotor = PortsList()
singlemotor.motorID = 1
othermotor = PortsList()
othermotor.motorID = 2
#singlemotor.JoystickAxis = 5

