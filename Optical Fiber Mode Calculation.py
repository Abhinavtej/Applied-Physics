n1 = float(input('Enter n1 value: '))
n2 = float(input('Enter n2 value: '))
d = float(input('Enter diameter value: '))
l = float(input('Enter wavelength value: '))
import math
NA = math.sqrt((n1**2)-(n2**2))
v= (d*math.pi)*NA/l
print(v)
print('Number of modes in SIF',(v**2)/2)