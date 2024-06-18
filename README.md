# Delta Robot


## Kinematics


### Forward Kinematics

Joint angles to position of the end effector.

Given $(\theta_1, \theta_2, \theta_3)$, find $(x, y, z)$

$$
[(R+Lcos\theta_i-r)cos\varphi_i-x]^2 + [(R+Lcos\theta_i-r)sin\varphi_i-y]^2 + [-Lsin\theta_i-z]^2 = La^2
$$


### Inverse Kinemtaics

Position of the end effector to required joint angles.

Given $(x, y, z)$, find $(\theta_1, \theta_2, \theta_3)$, wherein $(\varphi_i=\frac{2(i-1)}{3}\pi), (i=1,2,3)$



## Dynamics


## Workspace


## Appendix
[Open Source Delta-X](https://www.deltaxrobot.com/)
[工作空间](https://www.bilibili.com/video/BV1uY4y167Fv/?spm_id_from=333.788&vd_source=6164de2a185f949293fb3064a50fdb40)
