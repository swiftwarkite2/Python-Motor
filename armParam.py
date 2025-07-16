# Inverted Pendulum Parameter File
import numpy as np
# import control as cnt

# Physical parameters of the arm known to the controller
m = 0     # Mass of the arm, kg
ell = 0    # Length of the arm, m
g = 9.8       # Gravity, m/s**2

KD  = 0.0000021    # /10 # value choosen so that measured RPM is 6600/v like the hobby motor
#KD  = 0.0000021

J = 0.00000018772 #mass*radius^2 of wheel

#b = 0.1 #n.m.s viscous friction coefficient
KT = 0.00144686311 #/100 # n.m/A motor torque constant    (= 60/2pi*KV; KV = 6600 rpm) multiplied by voltage
#KT = 0.00144686311
#R = 1 #ohm resistence; guess
#T = 0.0198708 #n.m external load torque        

# parameters for animation
length = 5.0    # length of arm in animation
width = 5.0   # width of arm in animation

# Initial Conditions
theta0 = 0.0 *np.pi/180  # ,rads
thetadot0 = 0.0         # ,rads/s
thetaddot0 = 0.0

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 11.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# saturation limits
tau_max = 100.0                # Max torque, N-m

