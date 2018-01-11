from wpilib.command import Command
import csv
import oi
import time
from commands import playbackjoystick
 
class Playback(Command):
    '''
    This command will read inputs from a recorded file and execute them on a "virtual joystick"
    '''
    def __init__(self):
        super().__init__('Playback')

        #TODO get macro number or filename from driver station chooser or other input, so we can have multiple macros
        self.filename = 'macro1.csv'
        print('PLAY Init play command, filename: ', self.filename)

    def initialize(self):
        '''Called just before this Command runs the first time'''
        print('PLAY Opening record file for read, filename: ', self.filename)
        with open(self.filename, newline='') as f:
            self.data = list(csv.reader(f, delimiter=','))[0:]

        self.playback_joystick = playbackjoystick.PlaybackJoystick(self.data)
        oi.set_joystick(self.playback_joystick)

        self.counter = 0
        self.started = int(round(time.time() * 1000))

    def execute(self):
        curtime = int(round(time.time() * 1000)) - self.started
        ####NOTE: record iterates much faster than playback in the simulator
        ##TODO: need to seek ahead in the file and look for the closest "matching" time millis and set counter to there each time
        datalen = len(self.data)
        if datalen > self.counter :
            # skip forward in the input data, as needed, to find the current
            while(datalen > self.counter and int(self.data[self.counter][1]) < curtime):
                self.counter +=1

            if(datalen > self.counter):
                self.playback_joystick.setTime(curtime)
                filecounter = int(self.data[self.counter][0])
                filetime = int(self.data[self.counter][1])
                axis_data = []
                for ax in range(0, 6):
                    val = float(self.data[self.counter][2 + ax])
                    axis_data.append(str(val)) 
                print('PLAY Executing step %d, time %d, AXISDATA=%s (file counter %d, file time %s)' % (self.counter, curtime, ','.join(axis_data), filecounter, filetime))

    def isFinished(self):
        '''Make this return true when this Command no longer needs to run execute()'''
        return self.data is not None and self.counter > len(self.data)
    
    def end(self):
        '''Called once after isFinished returns true'''
        print('PLAY End called')
        oi.set_joystick()

    def interrupted(self):
        '''Called when another command which requires one or more of the same
           subsystems is scheduled to run'''
        self.end()