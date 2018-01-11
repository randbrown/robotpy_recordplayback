from wpilib.command import Command

import subsystems

class FollowJoystick(Command):
    '''
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    '''

    def __init__(self):
        super().__init__('Follow Joystick')

        self.requires(subsystems.motor)


    def execute(self):
        import oi
        subsystems.motor.setSpeed(oi.get_joystick().getY())
        subsystems.othermotor.setSpeed(oi.get_joystick().getX())
