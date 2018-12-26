import logging
import pickle
import json
import time

import sys
sys.path.insert(0, './src')
from MqttHand import MqttHand
from Instance import Instance

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(message)s',
        level=logging.DEBUG)
    logging.info('NetPickle listener')

    conf = dict(host="localhost",
                port=1883,
                timeout=60,
                subscribe=["MqttHand/#", "test/#"])

    mqtt = MqttHand(conf = conf)
    try:
        mqtt.start()

        while True:
            buff = mqtt.get_buffer()
            if(len(buff)>0):
                logging.info("ON MESSAGE")
                #logging.info(json.dumps(pickle.loads(buff[0]["payload"]).to_dict()))
                
                ins = pickle.loads(buff[0]["payload"])
                
                print ins.exe(2)
                ins.exe2("holis")
            
            time.sleep(1)
    except KeyboardInterrupt:
        mqtt.disconnect()
