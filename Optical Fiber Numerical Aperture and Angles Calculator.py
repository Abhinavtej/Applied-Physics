n1=float(input('Enter n1 value: '))
n2=float(input('Enter n2 value: '))
import math
NA = math.sqrt((n1**2)-(n2**2))
ɑ = math.asin(NA)
𝞱 = math.asin(n2/n1)
print('Numerical aperture', NA)
print('Acceptance Angle',math.degrees(ɑ))
print('Critical Angle',math.degrees(𝞱))