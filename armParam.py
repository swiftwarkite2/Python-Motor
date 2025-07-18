# I created this file came from the following github https://github.com/byu-controlbook/controlbook_public
import numpy as np

# Physical parameters known to the controller
m = 0     # Mass kg
ell = 0    # Length m
g = 9.8       # Gravity, m/s**2
# This KD value was determined from the simulation results using my calculated KT and J 
# values. Given KT and J, this KD value is required to achieve 6600 RPM/volt specified by the 
# hobby motor data sheet. Functionally KD is the damping effect and it provides stability

KD  = 0.0000021    # /10 # value chosen so that measured RPM is 6600/v like the hobby motor
# J is moment of inertia (rotational motion) calculated by the following equation: 
# Mass*Radius^2 (KG*M^2)
J = 0.00000018772 #mass*radius^2 of wheel
# KT is the motor torque constant (KT= 60/2pi*KV; KV = 6600 rpm) multiplied by voltage
KT = 0.00144686311 #/100 # n.m/A motor torque constant    (= 60/2pi*KV; KV = 6600 rpm) multiplied by voltage
# parameters for animation
length = 5.0    # length of wheel in animation
width = 5.0   # width of wheel in animation

# Initial Conditions
theta0 = 0.0 *np.pi/180  # rads
thetadot0 = 0.0         # rads/s
thetaddot0 = 0.0       # rads/s^2

# Simulation Parameters
t_start = 0.0  # Start time of simulation
t_end = 11.0  # End time of simulation
Ts = 0.01  # sample time for simulation
t_plot = 0.1  # the plotting and animation is updated at this rate

# saturation limits
tau_max = 100.0                # Max torque, N-m

