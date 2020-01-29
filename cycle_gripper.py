#!/usr/bin/python3

import sys
import time

sys.path.append("drake/lib/python3.6/site-packages")

import drake
import lcm


def open_gripper(lc):
    cmd = drake.lcmt_schunk_wsg_command()
    cmd.utime = 1
    cmd.target_position_mm = 109
    cmd.force = 80
    lc.publish("SCHUNK_WSG_COMMAND", cmd.encode())


def close_gripper(lc):
    cmd = drake.lcmt_schunk_wsg_command()
    cmd.utime = 1
    cmd.target_position_mm = 5
    cmd.force = 80
    lc.publish("SCHUNK_WSG_COMMAND", cmd.encode())

def main():
    lc = lcm.LCM()

    while True:
        open_gripper(lc)
        time.sleep(5)
        close_gripper(lc)
        time.sleep(5)


if __name__ == "__main__":
    main()
