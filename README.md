Example Record/Playback Robot
============================

A simple command based program with a record/playback feature

This is based on the "Command based robot" in RobotPy.

## How it works
While in Teleop mode, the first trigger button runs the Record command.  This captures all the joystick axis readings in every call to the Execute method, and stores them in a CSV file.  It records for 15 seconds and then stops recording.

The Autonomous command is a Playback command object.  This loads the recorded info from the CSV file, and then creates a PlaybackJoystick object to take the place of the real Joystick in the OI (operator interface).  This means any other commands/subsystems which read joystick input are now reading from the PlaybackJoystick instead of the real joystick.  Each time through the Execute method, it skips to the next pre-recorded values.  The end result is a 15 second playback macro which is identical to the original recording.

## TODO
This is a crude proof of concept.  Some ideas for something production-ready:
 
 * Needs to store buttons and D-pad (and any other relevant inputs) in addition to axis readings.
 * Provide a chooser on the dashboard with, for example, 10 options (or whatever makes sense), so the driver can record/playback up to 10 macros.  These would be stored in files such as macro-01.csv, macro-02.csv, and so on.
 * Needs better timing code.  Tested on simulator the Execute is fired several times per millisecond, but in the real robot it would be more like once per 20 ms or so.
 * Use data structures to represent the macro data, instead of using lists of strings with indicies.
 * MUCH CLEANUP
 * MUCH ERROR HANDLING
 * MUCH TESTING
 
 
  