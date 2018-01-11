from wpilib.command import Command
import oi
import subsystems
import time
class Record(Command):
    '''
    This command will read the joystick's inputs and store that to a file
    '''
    def __init__(self, concurrent_command = None):
        super().__init__('Record')
        # this recorder acts as a "pass-through" it records inputs and then runs the inner command such as FollowJoystick
        self.concurrent_command = concurrent_command
        self.setTimeout(15) # record for 15 seconds

        #TODO get from driver station or other input?
        self.filename = 'macro1.csv'
        print('REC Init record command, filename: ', self.filename)

    def initialize(self):
        '''Called just before this Command runs the first time'''
        print('REC Opening record file for write, filename: ', self.filename)
        self.file = open(self.filename, 'w')
        self.counter = 0
        self.started = int(round(time.time() * 1000))
        self.lastcurtime = -1
        if self.concurrent_command is not None:
            self.concurrent_command.initialize()

    def execute(self):
        curtime = int(round(time.time() * 1000)) - self.started

        # only update the file if it's been at least a millisecond!
        # this is because the simulator runs really quick. 
        #TODO on the real robot, need more sophisticated timing logic here
        if(curtime != self.lastcurtime):
            self.lastcurtime = curtime
            axis_data = []
            for ax in range(0, 6):
                val = oi.get_joystick().getRawAxis(ax)
                axis_data.append(str(val))
                
            #TODO get button values too

            linetext = str(self.counter) + ',' + str(curtime) + ',' + ','.join(axis_data) + '\n'
            self.file.write(linetext)
            self.counter += 1
        
        if self.concurrent_command is not None:
            self.concurrent_command.execute()

    def isFinished(self):
        '''Make this return true when this Command no longer needs to run execute()'''
        return self.isTimedOut()
    
    def end(self):
        '''Called once after isFinished returns true'''
        print('REC End called')
        if self.file is not None :
            try:
                print('REC Closing record file, filename: ', self.filename)
                self.file.close()
            except Exception as e:
                print('Exception: ' + e)
        
        if self.concurrent_command is not None:
            self.concurrent_command.end()

    def interrupted(self):
        '''Called when another command which requires one or more of the same
           subsystems is scheduled to run'''
        self.end()