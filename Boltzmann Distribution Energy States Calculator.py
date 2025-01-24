wl=int(input('Enter the value of Wavelength (in Å): '))
t=int(input('Enter the value of Temperature (in K): '))
h=6.62*(10**(-34))
c=3*(10**8)
k=1.38*(10**(-23))
l=10**(-10)
e=(h*c)/(wl*l)
x=e/(k*t)
#from boltzmann distribution law
#Ni = No x e**(d_e/kt)
#n=n2/n1
import math
n=math.e**(-x)
print('The relative population of two states is',n)