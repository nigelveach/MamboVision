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
mamboAddr = "DC-71-96-21-9C-E7"


# make my mambo object and connect to the drone
mambo = Mambo(mamboAddr, use_wifi=True)
print("trying to connect to mambo now")
success = mambo.connect(num_retries=3)
print("connected: %s" % success)

#sleep to allow for connection to finish initalizing
time.sleep(2)


# start video capture
cap = cv2.VideoCapture("rtsp://192.168.99.1/media/stream2", cv2.CAP_FFMPEG)
ret, frame = cap.read()
print(ret);


while ret:
    cv2.imshow('frame', frame)
    # do other processing on frame...

    ret, frame = cap.read()
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
mambo.disconnect()
print("disconnect")
# When everything done, release the capture
