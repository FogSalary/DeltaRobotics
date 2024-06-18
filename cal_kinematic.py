import os
import numpy as np
from deltaParam import DeltaParam

test_angles = [
    [0, 87.1, 60, 38, -147.4207, -55.0436, -396.4711],
    [1, 87.1, 4, 57, -210.5237, 120.2386, -323.8418],
    [2, 80, 24, 50, -165.8485, 66.2301, -371.905],
    [3, 70, 30, 10, -184.1114, -50.6553, -340.4092],
    [4, 60, 87.1, 6, -7.0798, -236.4796, -331.2253],
    [5, 48.9, 48.9, 87.1, 75.0503, 129.9908, -399.9427],
    [6, 27.2, 27.2, -22.6, -75.0752, -130.034, -310.0274],
    [7, 20, -10, 50, 7.8128, 168.5984, -320.0671],
    [8, 0, 0, 0, 4.8506, 0, -326.9174],
    [9, -22.6, 20, 20, 127.6965, 0, -311.4166]
]



R = 60
r = 35
L = 100
La = 350
theta1 = np.pi *  (-22.6)/180
theta2 = np.deg2rad(20)
theta3 = np.deg2rad(20)
deltaRobot = DeltaParam(R, r, L, La)
deltaRobot.cal_delta_forward_kinematic(theta1, theta2, theta3)
for cal_test in test_angles:
    index = cal_test[0]
    # X, Y, Z = deltaRobot.cal_delta_forward_kinematic(np.deg2rad(cal_test[1]), np.deg2rad(cal_test[2]), np.deg2rad(cal_test[3]))
    # print("Cal Test Cal %d: X = %f, Y = %f, Z = %f" % (index, X, Y, Z) )
    # print("Cal Test Ref %d: X = %f, Y = %f, Z = %f" % (index, cal_test[4], cal_test[5], cal_test[6]) )
    # print()

    theta1, theta2, theta3 = deltaRobot.cal_delta_inverse_kinematic(cal_test[4], cal_test[5], cal_test[6])
    print("Cal Test Cal %d: X = %f, Y = %f, Z = %f" % (index, theta1, theta2, theta3) )
    print("Cal Test Ref %d: X = %f, Y = %f, Z = %f" % (index, cal_test[1], cal_test[2], cal_test[3]) )
    print()


