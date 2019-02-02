# CANBusReplay
A simulation software used to send candump packets via MQTT gathered by a candump log file


### Requirements
Install required dependencies located in "requirements.txt" to run simulator


### Run!
To start simulation use:
```
python canBusReplay.py --log=candump.log
```
Where candump.log is your dump file



##### Realtime mode
To start simulation in realtime mode use:
```
python canBusReplay.py --log=candump.log --realtime
```