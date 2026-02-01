# UVLO
vin = 12
i1 = 1e-6
ihys = 2.9e-6
resd = 10e3
ven = 1.22
vstart = 11
vstop = 10
vhys = vstart - vstop

r1 = (vhys * (ven - (i1 * resd)) - ihys * resd * vstart) / (ihys * ven)
r2 = r1 * (ven - (resd * (i1 + ihys))) / ((vstop - ven) + (i1 + ihys) * (r1 + resd))

print("UVLO R1: {:.2f} kOhm".format(r1 / 1e3))
print("UVLO R2: {:.2f} kOhm".format(r2 / 1e3))

# RT/CLK
fsw = 570

rrt = 206033 / fsw ** 1.092 # fsw in kHz, Rrt in kOhm

print("RT/CLK R: {:.2f} kOhm".format(rrt))

# Iadj and Isense
viadj = 1.8
iled = 1.5
visense = viadj / 6
risense = visense / iled
print("Isense R: {:.2f} Ohm".format(risense))

# PDIM
#low level below 0.79 and high level above 1.45
# f = 100 hz to 1 khz

# COMP
# Ccomp = 0.1 uF

# Minimum Pulse Width
vout = vin * fsw * 1e3 * 140e-9
print("Minimum Pulse Width Vout: {:.2f} V".format(vout)) # nichia min voltage is 3.7 V

# BOOT
# Cboot = 0.1 uF

# Inductor
vout = 5
ir = 75e-3 # min ripple current
l = vout * (vin - vout) / (ir * vin * fsw)
ripple = vout * (vin - vout) / (l/2 * vin * fsw)
print("Inductor L: {:.2f} uH".format(l * 1e3))
print("Ripple Current: {:.2f} mA".format(ripple * 1e3))

# Output Capacitor
# cout = 1 uF

# Rectifier Diode
# schottky diode with vr > vin and if > led current

## Fix rectifier voltage(s)
## Fix risense power dissipation