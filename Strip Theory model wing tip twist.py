#eliptical wing
import math
import matplotlib.pyplot as plt

#assume right wing is stationary

# include d5

# Define constants
tip_length = 210
diagonal = 239.0237182
tip_chord=114.1592654
root_chord=200
theta=math.radians(28.52919071)
g=root_chord
psi=math.radians(90)
T= math.radians(112.2330454)
O=math.radians(90)
D4=315
q = 0.5 * 1.225 * 100  # where 10 is velocity
K=math.radians(67.76695456)
A=math.radians(70)
pi=math.pi
alphas=list(range(-10,31))
distance_of_trapeziumcog=105


for twist in range(-10,16,5):
    momenttwist = []
   #note that this is the rolling moment caused by differential lift between a twisted wing and a still wing.

   #no twist first
    if twist == 0:
        for alpha in alphas:
            Cl = 0.0331480646 * alpha -0.000429646

            # momentbackwardsweep = []
            # momentforwardsweep = []

            # compute initial moment at twist=0
            D1 = (D4+ tip_length)
            m = (tip_chord - root_chord) / (D1 - D4)
            c = tip_chord - m * (D1)
            m = m / 3
            c = c / 2
            momentneutral = q * Cl * (m * ((D1 ** 3) - (D4 ** 3) )+ c * ((D1 ** 2) - (D4 ** 2)))
            Moment=momentneutral-momentneutral
            momenttwist.append(Moment)
        plt.plot(alphas, momenttwist, label='line 0')

    else :
        for alpha in alphas:
            Cl = (0.0331480646 * alpha) - 0.000429646

            # momentbackwardsweep = []
            # momentforwardsweep = []

            # compute initial moment at twist=0
            D1 = (D4 + tip_length)
            m = (tip_chord - root_chord) / (D1 - D4)
            c = tip_chord - m * (D1)
            m = m / 3
            c = c / 2
            momentneutral = q * Cl * (m * ((D1 ** 3) - (D4 ** 3)) + c * ((D1 ** 2) - (D4 ** 2)))

            Cl = (0.0331480646 * (alpha + twist)) - 0.000429646

            # momentbackwardsweep = []
            # momentforwardsweep = []

            # compute initial moment at twist=0
            D1 = (D4 + tip_length)
            m = (tip_chord - root_chord) / (D1 - D4)
            c = tip_chord - m * (D1)
            m = m / 3
            c = c / 2
            twistmoment = q * Cl * (m * ((D1 ** 3) - (D4 ** 3)) + c * ((D1 ** 2) - (D4 ** 2)))


            Moment = twistmoment - momentneutral
            momenttwist.append(Moment)

        plt.plot(alphas, momenttwist, label='line'+ str(twist))



plt.legend()
plt.show()