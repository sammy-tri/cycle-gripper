# cycle-gripper

Instructions for running the gripper through a repeated cycle

These instructions require that a drake binary release is available.
Download the latest nightly release from
https://drake.mit.edu/from_binary.html and uncompress in this directory.

This project contains a precompiled version of `schunk_driver` from
https://github.com/RobotLocomotion/drake-schunk-driver .  It's not
necessary to checkout that library and bulld the driver, however the
gripper command interface will need to be set up through the web
interface as described there.

Next, confirm that the gripper driver can communicate with the gripper.
```
env LD_LIBRARY_PATH=drake/lib ./schunk_driver --gripper_addr=<gripper_addr>
```

Where `gripper_addr` is the same IP address as the web interface..

If communication with the gripper is working, the fingers will cycle
closed and then open, and the driver will print a message similar to
"Non-success response 1" (this is actually a successful result).

While `schunk_driver` is running, open another window and run
`cycle_gripper.py`.  This will cycle the gripper through the open and
closed positions.
