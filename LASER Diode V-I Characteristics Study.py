# LASER Diode Characteristics Study
# Aim: To study the V-I characteristics of a semiconductor diode laser.
# Apparatus: Laser diode, Photo Detector, 0-5V DC power supply, Voltmeter (0-20 V), Milliammeter (0-20 mA).
# Formula: λ = hc / Eg = 12400 / Eg (in Å)

import matplotlib.pyplot as plt

# Input Voltage (V) values
voltage_input = input("Enter Voltage (V) values (separated by commas): ")
voltage = [float(value) for value in voltage_input.split(',')]

# Input Current (mA) for different resistances
c1_input = input("Enter Current (mA) values for R = 100Ω (separated by commas): ")
current_1 = [float(value) for value in c1_input.split(',')]

c2_input = input("Enter Current (mA) values for R = 150Ω (separated by commas): ")
current_2 = [float(value) for value in c2_input.split(',')]

c3_input = input("Enter Current (mA) values for R = 220Ω (separated by commas): ")
current_3 = [float(value) for value in c3_input.split(',')]

plt.plot(voltage, current_1, marker='o', label='R = 100Ω')
plt.plot(voltage, current_2, marker='o', label='R = 150Ω')
plt.plot(voltage, current_3, marker='o', label='R = 220Ω')

plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('V-I Characteristics Graph of LASER Diode')
plt.legend()

plt.grid(True)
plt.show()
