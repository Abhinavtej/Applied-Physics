d = int(input('Distance between Screen and Grating (in cm): '))
n = [1,2,3]
N = 2500/2.54
import math
for i in range(0,3):
    x2= float(input(f'Distance between Corresponding Maxima of Order {n[i]} (in cm): '))
    x=x2/2
    sin𝞱 = x/math.sqrt((x**2)+(d**2))
    λ = sin𝞱*(10**8)/(N*n[i])
    print(f'Wavelength of Laser Beam of Order {n[i]} =','%.f'%λ)