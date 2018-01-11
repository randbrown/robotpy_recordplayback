
'''
Psuedo-joystick object for playback of recorded macros
'''
class PlaybackJoystick():
    def __init__(self, playback_data):
        self.playback_data = playback_data
        self.t = 0

    def setTime(self, t=0):
        self.t = t
    
    def getRawAxis(self, axis):
        #TODO fix me, get correct index for time t
        # in the simulator it's called multiple times per millisecond, but the recorder only stores one per millisecond,
        # so in the simulator index is usually the same as t.... but in the real bot it would be like every 50 ms or so
        index = self.t
        if(index < len(self.playback_data)):
            return float(self.playback_data[index][axis + 2])
        return 0

    def getX(self, hand=None):
        return self.getRawAxis(0)

    def getY(self, hand=None):
        return self.getRawAxis(1)
