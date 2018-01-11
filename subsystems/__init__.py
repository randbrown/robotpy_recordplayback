'''
All subsystems should be imported here and instantiated inside the init method.
If you want your subsystem to be accessible to commands, you must add a variable
for it in the global scope.
'''

from wpilib.robotbase import RobotBase

from .singlemotor import SingleMotor
from .othermotor import OtherMotor

motor = None
othermotor = None

def init():
    '''
    Creates all subsystems. You must run this before any commands are
    instantiated. Do not run it more than once.
    '''
    global motor
    global othermotor

    '''
    Some tests call startCompetition multiple times, so don't throw an error if
    called more than once in that case.
    '''
    if motor is not None and not RobotBase.isSimulation():
        raise RuntimeError('Subsystems have already been initialized')

    motor = SingleMotor()
    othermotor = OtherMotor()
