from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

from commands.crash import Crash
from commands.record import Record
from commands.followjoystick import FollowJoystick

# "real" joystick from human player
joystick_player = None
# virtual joystick used by record/playback logic
joystick_current = None

def init():
    '''
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    '''
    global joystick_player

    joystick_player = Joystick(0)
    set_joystick()

    trigger = JoystickButton(joystick_player, Joystick.ButtonType.kTrigger)

    trigger.whenPressed(Record(FollowJoystick()))

def set_joystick(joystick = None):
    global joystick_player
    global joystick_current
    if joystick is None:
        joystick_current = joystick_player
    else:
        joystick_current = joystick

def get_joystick(key = None):
    global joystick_current
    #TODO look at key if specified (for example if caller really needs a "real" joystick)
    return joystick_current
