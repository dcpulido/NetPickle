import logging
import pickle
import json
import time

import sys
sys.path.insert(0, './src')
from Instance import Instance
from MqttHand import MqttHand

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(message)s',
        level=logging.DEBUG)
    logging.info('NetPickle sender')

    ins = Instance(dict(name="holi", edad=0))
    #ins.__class__.__name__ = "persona"

    logging.info(json.dumps(ins.to_dict()))

    mqtt = MqttHand()
    try:
        mqtt.start()
        mqtt.on_publish("test/",
                        pickle.dumps(ins))
        mqtt.disconnect()
    except KeyboardInterrupt:
        mqtt.disconnect()
