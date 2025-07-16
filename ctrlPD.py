import numpy as np
import armParam as P

class ctrlPD:
    def __init__(self):
        #  tuning parameters
        tr = 0.4  # tuned for faster rise time before saturation.
        zeta = 0.707
        # desired natural frequency
        wn = 2.2 / tr
        alpha1 = 2.0 * zeta * wn
        alpha0 = wn**2
        # compute PD gains
        self.kp = alpha0*(P.J/P.KT)
        self.kd = P.J/(P.KT)*(alpha1-(P.KD/P.J))
        print('kp: ', self.kp)
        print('kd: ', self.kd)        

    def update(self, r, state):
        theta = state[0][0]
        thetadot = state[1][0]
        thetaddot = state[2][0]
        # compute feedback linearizing torque tau_fl
        voltage_eq = thetadot*P.KD/P.KT
        voltage_tilde = self.kp * (r - thetadot) \
                     - self.kd 
        # compute total torque
        total_voltage = voltage_eq + voltage_tilde
        out = saturate(total_voltage, P.tau_max)
        return out

def saturate(u, limit):
    if abs(u) > limit:
        u = limit * np.sign(u)
    return u








