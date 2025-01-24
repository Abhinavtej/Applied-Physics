e1=float(input('Enter the value of E1 (in eV): '))
e2=float(input('Enter the value of E2 (in eV): '))
h=6.62*(10**(-34))
c=3*(10**8)
l=10**(-10)
j=6.24*(10**18)
e=e2-e1
wl=(h*c*j)/(e*l)
print('The Wavelength of Energy Levels is',wl)
wl1=int(wl)
if wl1 in range(4000,8001):
    print('It is Visible')
else:
    print('It is Not Visible')