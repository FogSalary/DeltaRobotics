import numpy as np


class DeltaParam:
    def __init__(self, R, r, L, La):
        self.R = R
        self.r = r
        self.L = L
        self.La = La

    def cal_delta_forward_kinematic(self, theta1, theta2, theta3):
        A1 = self.R + self.L * np.cos(theta1) - self.r
        B1 = 1
        C1 = self.L * np.sin(theta1)
        A2 = -(1/2) * (self.R + self.L*np.cos(theta2)-self.r)
        B2 = (np.sqrt(3)/2) * (self.R + self.L*np.cos(theta2) - self.r)
        C2 = self.L * np.sin(theta2)
        A3 = -(1/2) * (self.R + self.L*np.cos(theta3) - self.r)
        B3 = -(np.sqrt(3)/2) * (self.R + self.L*np.cos(theta3) - self.r)
        C3 = self.L * np.sin(theta3)
        D1 = (1/2) * (A2**2 - A1**2 + C2**2 - C1**2 + B2**2)
        A21 = A2 - A1
        C21 = C2 - C1
        D2 = (1/2) * (A3**2 - A1**2 + C3**2 - C1**2 + B3**2)
        A31 = A3 - A1
        C31 = C3 - C1
        E1 = (B3 * C21 - B2 * C31) / (A21 * B3 - A31 * B2)
        F1 = (B3 * D1 - B2 * D2) / (A21 * B3 - A31 * B2)
        E2 = (A31 * C21 - A21 * C31) / (A31 * B2 - A21 * B3)
        F2 = (A31 * D1 - A21 * D2) / (A31 * B2 - A21 * B3)
        a = E1**2 + E2**2 + 1
        b = 2*E2*F2 + 2*C1 - 2*E1*(A1-F1)
        c = (A1 - F1)**2 + F2**2 + C1**2 - self.La**2
        Z = (-b - np.sqrt(b**2-4*a*c)) / (2*a)
        X = E1*Z + F1
        Y = E2*Z + F2
        # print("X localtion: %f" % X)
        # print("Y localtion: %f" % Y)
        # print("Z localtion: %f" % Z)

        # print("Prove")
        result1 = (A1-X)**2 + Y**2 + (C1+Z)**2 - self.La**2
        result2 = (A2-X)**2 + (B2-Y)**2 + (C2+Z)**2 - self.La**2
        result3 = (A3-X)**2 + (B3-Y)**2 + (C3+Z)**2 - self.La**2
        # print("(A1-X)**2 + (B1-Y)**2+ (C1+Z)**2 - La**2 = %f" % result1)
        # print("(A2-X)**2 + (B2-Y)**2 + (C2+Z)**2 - La**2 = %f" % result2)
        # print("(A3-X)**2 + (B3-Y)**2 + (C3+Z)**2 - La**2 = %f" % result3)

        error = result1**2 +result2**2 + result3**2
        if error < 1e-5:
            print("Prove Pass!!!!")

        return X, Y, Z
    
    def cal_delta_inverse_kinematic(self, x, y, z):
        A1 = (x**2 + y**2 + z**2 + self.L**2 - self.La**2 + (self.R-self.r)**2 - 2*x*(self.R-self.r)) / (2*self.L)
        B1 = -(self.R - self.r - x)
        C1 = z
        A2 = (x**2 + y**2 + z**2 + self.L**2 - self.La**2 + (self.R-self.r)**2 + (x-np.sqrt(3)*y)*(self.R-self.r)) / self.L
        B2 = -2 * (self.R-self.r) - (x-np.sqrt(3)*y)
        C2 = 2 * z
        A3 = (x**2 + y**2 + z**2 + self.L**2 - self.La**2 + (self.R-self.r)**2 + (x+np.sqrt(3)*y)*(self.R-self.r)) / self.L
        B3 = -2 * (self.R-self.r) - (x + np.sqrt(3)*y)
        C3 = 2 * z
        K1 = A1 + B1
        U1 = 2*C1
        V1 = A1 - B1
        K2 = A2 + B2
        U2 = 2*C2
        V2 = A2 - B2
        K3 = A3 + B3
        U3 = 2 * C3
        V3 = A3 - B3
        theta1 = 2 * np.rad2deg(np.arctan((-U1-np.sqrt(U1**2-4*K1*V1))/(2*K1)))
        theta2 = 2 * np.rad2deg(np.arctan((-U2-np.sqrt(U2**2-4*K2*V2))/(2*K2)))
        theta3 = 2 * np.rad2deg(np.arctan((-U3-np.sqrt(U3**2-4*K3*V3))/(2*K3)))
        return theta1, theta2, theta3