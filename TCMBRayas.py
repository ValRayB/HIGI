import numpy as np
import math as matplotlib.plt as plt
import constants as cons #Hay que descargar scipy.constants 

def Intesity(nu, T):
	h = 
	c =
	k =
	nu=nu*c*100
	fact = h*nu/(k*T)
	 
	I = ((h*nu**3)/c**2)*(1/(np.exp(fact)-1))

	#h cm 
	#v 1/cm
	return I

def SI_to_Jansky(value_Jy):
#1 Jy es x10-
	return value_SI/1e-26/1e6
	
data =np.loadtxt("IRCF.txt").T
nu=data[0]
I=data[1]
Ierr=data[3]

Intesity= SI_to_MJansky(Intensity(nu,5))
plt.plot(nu, Intensity(nu,5))
plt.show()
plt.errorbar(nu,I, Ierr)




#def Intensity_Jy(nu.T):
	

