import time
from paho.mqtt import client as mqtt
import sys

client = mqtt.Client("CANBus Replay")
client.connect("localhost")

client.loop_start()

# Output topic for simulator and input topic for DataConverter
topic = "data/raw"


def main(realtime):

    # TODO separe realtime to "in one breath" modes

    # Read candump log
    file = open(sys.argv[1][6:], "r")
    log = file.read()

    # Make log clean and fix json
    log = log.replace("$SYS/raw ", "").replace(",]", "]")

    # Split log to single events
    log = log.split("\n")

    for event in log:
        client.publish(topic, event)
        # Wait to evitate packet confusion
        time.sleep(.00001)


if len(sys.argv) >= 2 and sys.argv[1].startswith("--log="):
    if len(sys.argv) == 3 and sys.argv[2] == "--realtime":
        print("\n * CANBusReplay started in realtime mode\n")
        main(realtime=True)
    else:
        main(realtime=False)
else:
    print("\nCANBus Replay - Usage:\n\npython canBusReplay.py --log=candump.log --realtime (OPTIONAL)\n")
