from multiprocessing.connection import wait
import os
import sys
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI


class controller():

    def __init__(self):
        self.swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})

        self.swift.waiting_ready(timeout=3)

        device_info = self.swift.get_device_info()
        print(device_info)
        firmware_version = device_info['firmware_version']
        if firmware_version and not firmware_version.startswith(('0.', '1.', '2.', '3.')):
            self.swift.set_speed_factor(0.0005)

        self.swift.set_mode(0)
        self.swift.reset(wait=True, speed=20000)


    def look_left(self):
        # self.swift.reset(wait=True, speed=30000)
        # self.swift.set_position(x=200, y=160, wait=True)
        # self.swift.flush_cmd(wait_stop=True)
        # print("Looking left")

        # self.swift.set_polar(stretch=200, speed=10000)
        self.swift.set_polar(rotation=180)
        # self.swift.set_polar(height=150)
        # print(self.swift.set_polar(stretch=200, rotation=90, height=150, wait=True))
    

    def look_right(self):
        self.swift.reset(wait=True, speed=30000)
        self.swift.set_position(x=30, y=-200, wait=True)
        # self.swift.flush_cmd(wait_stop=True)
        print("Looking right")
    

    def exit(self):
        self.swift.reset(wait=True, speed=20000)
        self.swift.set_position(x=140, y=0, z=50, wait=True)
        # self.swift.flush_cmd(wait_stop=True)

        print("Bye")
        self.swift.disconnect()


def testRoutine():
    example = controller()

    example.look_left()
    time.sleep(3)
    # example.look_right()
    # time.sleep(3)

    example.exit()


testRoutine()
