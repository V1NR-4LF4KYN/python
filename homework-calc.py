'''
A program I will mostly write while doing homework

'''
# imports
import math

# global vars
# physics constants
c = speedOfLight = 299792458 # m/s
h = plancksConstant = 6.62607004E-34 # m²kg/s
q = electronMass = 1.6021766208E-19 # Coloumb

# funcs
def nanoMetresToElectronVolt(nm):
    # func would be used to convert nanometres into E-Photons
    global q, h, c
    
    print("Amount of nm: ", nm)
    
    nm = nm * 1E-9
    ePHinJoule = (h * (c/nm))
    print(ePHinJoule, "Joule")
    
    ePHinEV = (ePHinJoule / q)
    print(ePHinEV, "eV")


def frequencyToJoule(f):
    global h
    ePHinJoule = (h*f)
    return ePHinJoule

def convertJouleToeV(j):
    global q
    eV = j * q
    return eV
    
# main-loop
def main():
    #print(frequencyToJoule(900E3), "Joule")
    #print(convertJouleToeV(frequencyToJoule(900E3)), " eV")
    nanoMetresToElectronVolt(300)

# calling main
main()

 