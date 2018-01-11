import wpilib
from wpilib.command.subsystem import Subsystem

# from commands.followjoystick import FollowJoystick
import robotmap

class OtherMotor(Subsystem):
    '''
    This example subsystem controls a single CAN Talon SRX in PercentVBus mode.
    '''

    def __init__(self):
        '''Instantiates the motor object.'''

        super().__init__('OtherMotor')

        self.motor = wpilib.Talon(robotmap.othermotor.motorID)


    def setSpeed(self, speed):
        self.motor.set(speed)


    # def initDefaultCommand(self):
    #     self.setDefaultCommand(FollowJoystick())
