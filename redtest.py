from threading import Thread
from pyparrot.Minidrone import Mambo
from pyparrot.DroneVision import DroneVision
from pyparrot.Model import Model

import time
import numpy as np
import cv2
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = 'protocol_whitelist;file,tcp,rtp,udp | fflags;nobuffer | flag;low_delay'
mamboAddr = "DC-71-96-21-9C-E7"



class RTSPVideoWriterObject(object):
    lowh = 10
    lows = 150
    lowv = 50

    highh = 170
    highs = 255
    highv = 175

    def __init__(self, src, mambo):
        self.mambo = mambo
        print('src', src)
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)

        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # Set up codec and output video settings
        self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
        self.output_video = cv2.VideoWriter('output.avi', self.codec, 30, (self.frame_width, self.frame_height))

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        # Display frames in main program
        if self.status:
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)




            mask1 = cv2.inRange(hsv, (0, self.lows, self.lowv), (self.lowh, self.highs, self.highv))
            mask2 = cv2.inRange(hsv, (self.highh, self.lows, self.lowv), (180, self.highs, self.highv))
            #mask1 = cv2.inRange(hsv, (0, 150, 50), (10, 255, 175))
            #mask2 = cv2.inRange(hsv, (170, 150, 50), (180, 255, 175))
            mask = cv2.bitwise_or(mask1, mask2)
            cropped = cv2.bitwise_and(self.frame, self.frame, mask=mask)
            #cv2.imshow('frame', mask)
            _, width = mask.shape

            left = cropped[:, width//2:]
            right = cropped[:, :width//2]
            cv2.imshow('left', left)
            cv2.imshow('right', right)

            leftsum = cv2.sumElems(left)[0]
            rightsum = cv2.sumElems(right)[0]
            #print(cv2.sumElems(left)[0])
            print('left %d right %d' % (leftsum, rightsum))
            print("left" if leftsum > rightsum else "right")





        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('i'):
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            mambo.disconnect()
            print("disconnect")
            exit(1)
        if key == ord('p'):
            #safe_takeoff
            print('taking off')
            print(self.mambo)
            #self.mambo.safe_takeoff(5)
        if key == ord('l'):
            print('landing')
        #high
        if key == ord("q"):
            self.highh += 1
        if key == ord("z"):
            self.highh -= 1
        if key == ord("w"):
            self.highs += 1
        if key == ord("x"):
            self.highs -= 1
        if key == ord("e"):
            self.highv += 1
        if key == ord("c"):
            self.highv -= 1
        #low
        if key == ord("r"):
            self.lowh += 1
        if key == ord("v"):
            self.lowh -= 1
        if key == ord("t"):
            self.lows += 1
        if key == ord("b"):
            self.lows -= 1
        if key == ord("y"):
            self.lowv += 1
        if key == ord("n"):
            self.lowv -= 1

        print("pritnving valsd")
        print(self.highh)
        print(self.highs)
        print(self.highv)
        print(self.lowh)
        print(self.lows)
        print(self.lowv)


    def save_frame(self):
        # Save obtained frame into video output file
        self.output_video.write(self.frame)

if __name__ == '__main__':
    mambo = Mambo(mamboAddr, use_wifi=True)
    print("trying to connect to mambo now")
    success = mambo.connect(num_retries=3)
    print("connected: %s" % success)
    # mambo.SetResolution()

    time.sleep(2)

    rtsp_stream_link = 'rtsp://192.168.99.1/media/stream2'
    video_stream_widget = RTSPVideoWriterObject(rtsp_stream_link, mambo)
    #video_stream_widget = RTSPVideoWriterObject(0, mambo)

    while True:
        try:
            video_stream_widget.show_frame()
            video_stream_widget.save_frame()
        except AttributeError:
            pass
