import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

volt = [0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0]

l1 = [0,0,0,0,0,0,0,0,0,0.3,1.1,2.1,3.1,4.1,5.2,6.2,7.3,8.3,9.4,10.5,11.6]
plt.plot(volt, l1, label = "100 Ω")

l2 = [0,0,0,0,0,0,0,0,0,0.3,0.9,1.7,2.5,3.3,4.1,4.9,5.7,6.6,7.4,8.3,9.1]
plt.plot(volt, l2, label = "150 Ω")

l3 = [0,0,0,0,0,0,0,0,0,0.2,0.7,1.3,1.9,2.5,3.2,3.8,4.4,5.1,5.7,6.4,7.0]
plt.plot(volt, l3, label = "200 Ω")

plt.xlim(0,4.4)
plt.ylim(0,12.5)

plt.legend()
plt.xlabel('Voltage (v)')
plt.ylabel('Current (mA)')
plt.title('V-I Characteristics of Laser Diode')

plt.show()

while True:
    dwn = input('Want to download graph (yes/no): ')
    if dwn == 'yes':
        with PdfPages('V-I Characteristics of Laser Diode.pdf') as pdf:
            pdf.savefig()
        print('Please check the directory, where you open this file')
        break
    elif dwn == 'no':
        break
    else:
        print('Please Select (yes/no): ')