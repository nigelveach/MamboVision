import curses
from curses import wrapper
import time

from pyparrot.Minidrone import Mambo

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
                c = stdscr.getch()
                stdscr.clear()

                if c == ord('l'):
                    stdscr.addstr("landing")
                    mambo.safe_land(5)
                    break

                elif c == ord('w'):
                    stdscr.addstr("forward")
                    mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0)

                elif c == ord('s'):
                    stdscr.addstr("backward")
                    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0)

                elif c == ord('d'):
                    stdscr.addstr("yaw right")
                    mambo.fly_direct(roll=0, pitch=0, yaw=50, vertical_movement=0)

                elif c == ord('a'):
                    stdscr.addstr("yaw left")
                    mambo.fly_direct(roll=0, pitch=0, yaw=-50, vertical_movement=0)

                elif c == ord('r'):
                    stdscr.addstr("rise")
                    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50)

                elif c == ord('f'):
                    stdscr.addstr("fall")
                    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50)

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
    mambo.smart_sleep(2)
    mambo.ask_for_state_update()
    mambo.smart_sleep(2)
    stdscr = curses.initscr()
    wrapper(fly)
    mambo.disconnect()
    print("disconnect")
