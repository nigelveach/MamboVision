"""
Use laptop keys to control a Parrot mambo drone remotely

Author: Nigel Veach
"""

from pyparrot.Minidrone import Mambo

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


    print("taking off")
    mambo.safe_takeoff(5)
    mambo.smart_sleep(2)

    print("forward")
    mambo.fly_direct(roll=0, pitch=50, yaw=0, vertical_movement=0, duration=1)
    mambo.smart_sleep(2)

    print("yaw right")
    mambo.fly_direct(roll=0, pitch=0, yaw=50, vertical_movement=0, duration=1)
    mambo.smart_sleep(2)

    print("yaw left")
    mambo.fly_direct(roll=0, pitch=0, yaw=-50, vertical_movement=0, duration=1)
    mambo.smart_sleep(2)

    print("up")
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=50, duration=1)
    mambo.smart_sleep(2)

    print("down")
    mambo.fly_direct(roll=0, pitch=0, yaw=0, vertical_movement=-50, duration=1)
    mambo.smart_sleep(2)

    print("backward")
    mambo.fly_direct(roll=0, pitch=-50, yaw=0, vertical_movement=0, duration=1)
    mambo.smart_sleep(2)

    print("landing")
    mambo.safe_land(5)
    mambo.smart_sleep(5)

    print("disconnect")
    mambo.disconnect()
