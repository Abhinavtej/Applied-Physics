import numpy as np
import matplotlib.pyplot as plt

Tc = np.array([75,70,65,60,55,50,45,40,35])
Tk = [x + 273 for x in Tc]
Is = np.array([29,25,23,22,21,21,20,19,18])

import math
x = [1000/x for x in Tk]
y = [math.log10(x*(10**-6)) for x in Is]

f = np.polyfit(x, y, 1)
slope = f[0]
plt.scatter(x, y, label='Experimental Data')
plt.plot(x, np.polyval(fit, x), label='Linear Fit') # type: ignore

plt.legend()
plt.xlabel('Log Is')
plt.ylabel('1000/T')
plt.title('Linear Fit of Experimental Data')

Eg = 0.198*slope
print("Slope of the linear fit: ", slope)
print('Energy Band Gap of Semiconductor =',Eg)
plt.show()

from matplotlib.backends.backend_pdf import PdfPages
while True:
    dwn = input('Want to download graph (yes/no): ')
    if dwn == 'yes':
        with PdfPages('Linear Fit of Experimental Data.pdf') as pdf:
            pdf.savefig()
        print('Please check the directory, where you open this file')
        break
    elif dwn == 'no':
        break
    else:
        print('Please Select (yes/no): ')