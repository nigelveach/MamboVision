# MamboVision

This library aims to develop an object-avoidance system using the FPV camera of Parrot Mambo drones.  Computations will be performed wirelessly on a laptop, due to the limited on-board computational power of a Mambo drone.  The pyparrot library (https://github.com/amymcgovern/pyparrot) will be used extensively

## Completed

- pyparrot library implemented
- programming capability of the drone achieved
- video streaming to laptop achieved in both VLC and ffmpeg formats

## To-Do

- fix VLC bug
- determine best and easiest way to achieve object avoidance
- determine best format for receiving video stream (opencv, VLC, ffmpeg, etc)
