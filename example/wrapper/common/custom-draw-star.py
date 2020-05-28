#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
Description: Move line(linear motion)
"""

import math
import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI


#######################################################
"""
Just for test example
"""
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read('../robot.conf')
        ip = parser.get('xArm', 'ip')
    except:
        ip = input('Please input the xArm ip address:')
        if not ip:
            print('input error, exit')
            sys.exit(1)
########################################################


arm = XArmAPI(ip, is_radian=True)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.reset(wait=True)

Z_GROUND = 91.05

N = 15
X_STAR = []
Y_STAR = []

for i in range(N):
    X_STAR.append(350+90*math.cos(i*2*math.pi/N))
    Y_STAR.append(90*math.sin(i*2*math.pi/N))

for i in range(N+1):
    idx = (i*(N//2)) % N
    arm.set_position(x=X_STAR[idx], y=Y_STAR[idx], z=Z_GROUND, roll=-180, pitch=0, yaw=0, speed=100, is_radian=False, wait=True)
    print(arm.get_position(), arm.get_position(is_radian=False))

arm.set_position(x=X_STAR[idx], y=Y_STAR[idx], z=Z_GROUND+10, roll=-180, pitch=0, yaw=0, speed=100, is_radian=False, wait=True)
print(arm.get_position(), arm.get_position(is_radian=False))

arm.reset(wait=True)
arm.disconnect()
