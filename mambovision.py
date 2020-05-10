from pyparrot.Minidrone import Mambo
from pyparrot.DroneVision import DroneVision
from pyparrot.Model import Model

import curses
from curses import wrapper
import threading
from threading import Thread
import cv2
import time
import numpy as np
import cv2
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = 'protocol_whitelist;file,rtp,udp | fflags;nobuffer | flag;low_delay'

def fly(stdscr):
    curses.cbreak()
    stdscr.addstr("Press 'q' to quit, 't' to take off, 'l' to land, 'wasd' to steer, 'r' to rise, and 'f' to descend")

    while 1:
        c = stdscr.getch()
        stdscr.clear()

        if c == ord('q'):
            break

        elif c != ord('t'):
            stdscr.addstr("key not recognized")

        else:
            stdscr.addstr("taking off")
            mambo.safe_takeoff(5)

            while 1:
                cv2.imshow('frame', frame)
                ret, frame = cap.read()
                c = stdscr.getch()
                stdscr.clear()

                if c == ord('l'):
                    stdscr.addstr("landing")
                    mambo.safe_land(5)
                    break

                elif c == ord('w'):
                    stdscr.addstr("forward")
                    mambo.fly_direct(roll=0, pitch=20, yaw=0, vertical_movement=0)

                elif c == ord('d'):
                    stdscr.addstr("yaw right")
                    mambo.fly_direct(roll=0, pitch=0, yaw=40, vertical_movement=0)

                elif c == ord('a'):
                    stdscr.addstr("yaw left")
                    mambo.fly_direct(roll=0, pitch=0, yaw=-40, vertical_movement=0)

                elif c == ord('r'):
                    stdscr.addstr("rise")
                    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=15)

                elif c == ord('f'):
                    stdscr.addstr("fall")
                    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-15)

                else:
                    stdscr.addstr("key not recognized")


#IP address of mambo drone
mamboAddr = "DC-71-96-21-9C-E7"

# make my mambo object
# wifi should always be set to true, for retrieving video feed
mambo = Mambo(mamboAddr, use_wifi=True)
print("trying to connect")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

if (success):
    # get the state information
    print("sleeping")
    # finish waking up drone
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)

    wrapper(fly)

    cap.release()
    cv2.destroyAllWindows()
    mambo.disconnect()
    print("disconnect")
