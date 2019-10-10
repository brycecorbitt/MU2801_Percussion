# MU2801_Percussion
Final Project Code For MU2801

Quick Demo Video: [https://photos.app.goo.gl/p4jtpKGJ3gVdFLwV8](https://photos.app.goo.gl/p4jtpKGJ3gVdFLwV8)

NOTE: This project was poorly hacked together due to time constraints. Base code will likely be re-written in the future.

Final Setup:
![Final Iteration](https://i.imgur.com/zRk1IqF.jpg)

The core of the system is controlled by a Raspberry Pi 3. An L298N driver circuit is connected with pins to control forward motion, reverse motion, and speed ( via PWM). The L298N is also connected to a 12V 5A power supply which is used to provide adequate power to the 120RPM motor that drives the drumstick. Wood was laser cut to mount the motor onto music stand, and a mount for the drumstick was 3D printed to fit onto the motor. 

In order to know when to lift the motor up, a Piezo knock sensor was placed on the drum itself to detect vibration. It wires into a MCP3008 ADC which the Raspberry Pi uses to read analog data. 

From the software end, drivers were written for reading in data from the ADC, as well as basic control running the motor at different speeds in both directions. A simple Percussion class was developed that connects the two. When the Pi is instructed to hit, the motor starts a timer and moves forward. When a hard-coded threshold from the Piezo sensor is reached, the program assumes that the drum has been hit. From here, the timer stops, and the motor reverses direction for the same amount of time as recorded, allowing the stick to lift and return to its original position.

To control the setup, the [pymidi](https://github.com/mik3y/pymidi/) library was used to create an rtpMIDI/AppleMIDI server on the pi. The host computer running Ableton/Max MSP is then configured to connect to the device using “Apple Midi Setup” on Mac OS or “rtpMIDI” for Windows. Once the device is configured and connected, MIDI software will recognize it as a MIDI device. Any messages to the device will be routed over the network to the Pi, which is currently programmed to handle any “note_on” message and process a drum hit.
