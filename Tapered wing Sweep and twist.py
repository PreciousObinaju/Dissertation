#tapered wing
import math
import matplotlib.pyplot as plt

#assume right wing is stationary

'''the reason why the eliptical and tapered wing show different results is becaus sweeping the tapered wing inceases the root chord and chord along the wing
 as the chord sweeps toward the diagonal. however the eliptical wing reduces the chord facing the wind. it should make sense a bit'''
# that was wrong there was an error in the code

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

'''taperangle = 0
length = 360
r = 240  # length2
z = 322.432
theta = math.radians(37.14)
g = 227.248
psi = math.radians(85)
k = 195.413
T = math.radians(92.6)
O = math.radians(95)
D4 = length * math.cos(taperangle)
q = 0.5 * 1.225 * 100  # where 10 is velocity
K = math.radians(87.4)
A = math.radians(87)
pi = math.pi
alphas = list(range(-10, 11))'''

for sweep in range(-40, 41,10):
    momentbackwardsweep = []
    momentforwardsweep = []

   #note that this is the rolling moment caused by differential lift between a swept wing and a still wing.

   #no sweep first
    if sweep == 0:
        for alpha in alphas:
            Cl = 0.0331480646 * alpha -0.000429646

            # momentbackwardsweep = []
            # momentforwardsweep = []

            # compute initial moment at sweep=0
            D1 = (D4+ tip_length)
            m = (tip_chord - root_chord) / (D1 - D4)
            c = tip_chord - m * (D1)
            m = m / 3
            c = c / 2
            momentneutral = q * Cl * (m * ((D1 ** 3) - (D4 ** 3)) + c * ((D1 ** 2) - (D4 ** 2)))
            Moment=momentneutral-momentneutral
            momentbackwardsweep.append(Moment)
            momentforwardsweep.append(Moment)
        plt.plot(alphas, momentbackwardsweep, label='line 0')

    elif sweep < 0 :
        storesweep = sweep
        sweep =abs(sweep)
        sweep = math.radians(sweep)
        for alpha in alphas:
            Cl = 0.0331480646 * alpha -0.000429646

            # compute neutral wing moment at sweep=0
            D1 = (D4 + tip_length)
            m = (tip_chord - root_chord) / (D1 - D4)
            c = tip_chord - m * (D1)
            m = m / 3
            c = c / 2
            momentneutral = q * Cl * (m * ((D1 ** 3) - (D4 ** 3)) + c * ((D1 ** 2) - (D4 ** 2)))


            # Backward sweep analysis
            basechord = (root_chord * math.sin(K)) / math.sin(pi - sweep - K)
            phi = sweep
            D1 = tip_length * math.cos(phi)
            D2 = diagonal * math.cos(phi + theta)
            y = diagonal * math.sin(theta + phi) - D2 * math.tan(phi)
            D1 = D1 + D4
            D2 = D2 + D4
            m = (y - basechord) / (D2 - D4)
            c = y - m * (D2)
            m = m / 3
            c = c / 2
            Moment1 = q * Cl * (m * ((D2 ** 3) - (D4 ** 3)) + c * ((D2 ** 2) - (D4 ** 2)))
            m = -y / (D1 - D2)
            c = - m * (D1)
            m = m / 3
            c = c / 2
            Moment2 = q * Cl * (m * ((D1 ** 3) - (D2 ** 3)) + c * ((D1 ** 2) - (D2 ** 2)))
            overall_moment =  ( Moment2 + Moment1) - momentneutral
            momentbackwardsweep.append(overall_moment)
        plt.plot(alphas, momentbackwardsweep, label='line' + str(storesweep))

    else:
        storesweep = sweep
        sweep = math.radians(sweep)
        for alpha in alphas:
            Cl = 0.0331480646 * alpha - 0.000429646

            # compute neutral wing moment at sweep=0
            D1 = (D4 + tip_length)
            m = (tip_chord - root_chord) / (D1 - D4)
            c = tip_chord - m * (D1)
            m = m / 3
            c = c / 2
            momentneutral = q * Cl * (m * ((D1 ** 3) - (D4 ** 3)) + c * ((D1 ** 2) - (D4 ** 2)))

            # Forward sweep analysis
            basechord = (root_chord * math.sin(A)) / math.sin(pi - sweep - A)
            phi = sweep
            D1 = tip_length * math.cos(phi)
            D2 = diagonal * math.cos(theta - phi)
            D3 = root_chord * math.cos(psi - phi)
            x = (tip_chord * math.sin(T)) / math.sin(((3 / 2) * pi) - (T + O + phi)) #come back and check
            h = root_chord * math.sin(psi - phi) + D3 * math.tan(phi)
            D1 = D1 + D4
            D2 = D2 + D4
            D3 = D3 + D4
            m = (h - basechord) / (D3 - D4)
            c = h - m * (D3)
            m = m / 3
            c = c / 2
            Moment1 = q * Cl * (m * ((D3 ** 3) - (D4 ** 3)) + c * ((D3 ** 2) - (D4 ** 2)))
            m = (x - h) / (D1 - D3)
            c = x - m * (D1)
            m = m / 3
            c = c / 2
            Moment2 = q * Cl * (m * ((D1 ** 3) - (D3 ** 3)) + c * ((D1 ** 2) - (D3 ** 2)))
            m = -x / (D2 - D1)
            c = - m * (D2)
            m = m / 3
            c = c / 2
            Moment3 = q * Cl * (m * ((D2 ** 3) - (D1 ** 3)) + c * ((D2 ** 2) - (D1 ** 2)))
            overall_moment = (Moment2 + Moment1 + Moment3) - momentneutral
            momentforwardsweep.append(overall_moment)
        plt.plot(alphas, momentforwardsweep, label='line' + str(storesweep))

plt.legend()
plt.show()