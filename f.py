import math
import matplotlib.pyplot as plt


# Define constants
taperangle =math.radians(5)
length = 360
r = 240  #length2
z = 322.432
theta = math.radians(37.14)
g =227.248
psi = math.radians(85)
k=195.413
T = math.radians(92.6)
O = math.radians(95)
D4 = length * math.cos(taperangle)
q = 0.5*1.225*100 # where 10 is velocity
K = math.radians(87.4)
A = math.radians(87)
pi = math.pi
alphas=list(range(-10,11))



for sweep in range(0,20):
    momentbackwardsweep = []
    momentforwardsweep = []
    if sweep==0:
        for alpha in alphas:
            Cl= 0.1 * alpha + 0.5

           # momentbackwardsweep = []
            #momentforwardsweep = []

            #compute initial moment at sweep=0
            D1=(length+r)*math.cos(taperangle)
            m = (k - g) / (D1 - D4)
            c = k - m * (D1)
            m = m / 3
            c = c / 2
            Moment1 = q * Cl * (m * ((D1 ** 3) - (D4 ** 3) + c * ((D1 ** 2) - (D4 ** 2))))
            momentbackwardsweep.append(Moment1)
            momentforwardsweep.append(Moment1)
        plt.plot(alphas, momentbackwardsweep, label='line 0')

    else:
        storesweep=sweep
        sweep = math.radians(sweep)
        for alpha in alphas:
            Cl = 0.1 * alpha + 0.5
            
            # Backward sweep analysis
            basechord = (g * math.sin(K)) / math.sin(pi - sweep - K)
            phi = sweep + taperangle
            D1 = r * math.cos(phi)
            D2 = z * math.cos(phi + theta)
            y = z * math.sin(theta + phi) - D2 * math.tan(phi)
            D1 = D1 + D4
            D2 = D2 + D4
            m = (y - basechord) / (D2 - D4)
            c = y - m * (D2)
            m = m / 3
            c = c / 2
            Moment1 = q * Cl * (m * ((D2 ** 3) - (D4 ** 3) + c * ((D2 ** 2) - (D4 ** 2))))
            m = -y / (D1 - D2)
            c = - m * (D1)
            m = m / 3
            c = c / 2
            Moment2 = q * Cl * (m * ((D1 ** 3) - (D2 ** 3) + c * ((D1 ** 2) - (D2 ** 2))))
            overall_moment = Moment2 + Moment1
            momentbackwardsweep.append(overall_moment)

            # Forward sweep analysis
            basechord = (g * math.sin(A)) / math.sin(pi - sweep - A)
            phi = sweep - taperangle
            D1 = r * math.cos(phi)
            D2 = z * math.cos(theta - phi)
            D3 = g * math.cos(psi - phi)
            x = (k * math.sin(T)) / math.sin(((3 / 2) * pi) - (T + O + phi))
            h = g * math.sin(psi - phi) + D3 * math.tan(phi)
            D1 = D1 + D4
            D2 = D2 + D4
            D3 = D3 + D4
            m = (h - basechord) / (D3 - D4)
            c = h - m * (D3)
            m = m / 3
            c = c / 2
            Moment1 = q * Cl * (m * ((D3 ** 3) - (D4 ** 3) + c * ((D3 ** 2) - (D4 ** 2))))
            m = (x - h) / (D1 - D3)
            c = x - m * (D1)
            m = m / 3
            c = c / 2
            Moment2 = q * Cl * (m * ((D1 ** 3) - (D3 ** 3) + c * ((D1 ** 2) - (D3 ** 2))))
            m = -x / (D2 - D1)
            c = - m * (D2)
            m = m / 3
            c = c / 2
            Moment3 = q * Cl * (m * ((D2 ** 3) - (D1 ** 3) + c * ((D2 ** 2) - (D1 ** 2))))
            overall_moment = Moment2 + Moment1 + Moment3
            momentforwardsweep.append(overall_moment)
        plt.plot(alphas, momentbackwardsweep, label='line'+str(storesweep))


plt.legend()
plt.show()
