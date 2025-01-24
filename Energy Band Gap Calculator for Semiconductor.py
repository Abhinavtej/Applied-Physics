Tc = int(input('Enter the value of Temperature (in ℃): '))
Is = int(input('Enter the value of current (in 𝞵A): '))
Tk = Tc + 273
import math
Slope = math.log10(Is*(10**-6)) / (1000/Tk)
Eg = 0.198*Slope
print('Energy Band Gap of Semiconductor =',Eg)