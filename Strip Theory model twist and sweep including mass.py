#tapered wing
import math
import matplotlib.pyplot as plt
import openpyxl
#assume right wing is stationary
#include D5


# Define constants
tip_length = 0.210
diagonal = 0.2390237182
tip_chord=0.1141592654
root_chord=0.200
theta=math.radians(28.52919071)
g=root_chord
psi=math.radians(90)
T= math.radians(112.2330454)
O=math.radians(90)
D4=0.315
q = 0.5 * 1.225 * 144  # where 12 is velocity
K=math.radians(67.76695456)
A=math.radians(70)
pi=math.pi
alphas=list(range(-10,21,2))
distance_of_trapeziumcog=0.100
weight_of_morphing_section = 1.6677


for twist in range(-10, 16,5):

    momentbackwardsweep = []
    momentforwardsweep = []

    # d5 inclusion
    D5 = 0.307
    c = 0.220
    c = c / 2
    twistmoment1 = q * (0.0331480646 * twist) * (c * ((D4 ** 2) - (D5 ** 2)))

    for sweep in range(-40, 41, 10):
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet['A1'] = 'Roll(Mx)'
        worksheet['B1'] = 'exb.Inc'
        i=2
        momentbackwardsweep = []
        momentforwardsweep = []

        if sweep == 0:

            for alpha in alphas:
                Cl = (0.0331480646 * alpha) - 0.000429646

                # momentbackwardsweep = []
                # momentforwardsweep = []

                # compute initial moment at twist=0
                D1 = (D4 + tip_length)
                m = (tip_chord - root_chord) / (D1 - D4)
                c = tip_chord - m * (D1)
                if i==1:
                    print(str(m)+'   '+str(c))
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

                Moment =twistmoment1 + twistmoment - momentneutral
                worksheet['A'+str(i)]=Moment
                worksheet['B' + str(i)] = alpha
                i=i+1
                momentbackwardsweep.append(Moment)
                momentforwardsweep.append(Moment)

            plt.plot(alphas, momentbackwardsweep, label='line 0'+ str(twist) + 'twist')
            workbook.save('C:\\Users\\44786\\Documents\\University of Bristol\\dissertation\\data\\excel\\ 12ms' +str(sweep)+'sweep' + str(twist) +'twist.xlsx')

        elif sweep < 0 :
            storesweep1 = abs(sweep)
            storesweep = sweep
            sweep =abs(sweep)
            sweep = math.radians(sweep)
            Weightshiftrollingmoment = weight_of_morphing_section * ((distance_of_trapeziumcog)-(distance_of_trapeziumcog*(math.cos(sweep))))


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
                Cl = (0.0331480646 * (alpha + twist)) - 0.000429646

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
                overall_moment =  ( twistmoment1 + Moment2 + Moment1) - momentneutral + Weightshiftrollingmoment
                worksheet['A'+str(i)]=  overall_moment
                worksheet['B' + str(i)] = alpha
                i=i+1
                momentbackwardsweep.append(overall_moment)
            plt.plot(alphas, momentbackwardsweep, label='line' + str(storesweep))
            workbook.save('C:\\Users\\44786\\Documents\\University of Bristol\\dissertation\\data\\excel\\12ms' +str(storesweep1)+'backward sweep' + str(twist) +'twist.xlsx')


        else:
            storesweep = sweep
            sweep = math.radians(sweep)
            Weightshiftrollingmoment = weight_of_morphing_section * ((distance_of_trapeziumcog + D4) - (distance_of_trapeziumcog * (math.cos(sweep)) + D4))

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

                Cl = (0.0331480646 * (alpha + twist)) - 0.000429646

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
                overall_moment = (twistmoment1 + Moment2 + Moment1 + Moment3) - momentneutral +Weightshiftrollingmoment
                worksheet['A'+str(i)]=  overall_moment
                worksheet['B' + str(i)] = alpha
                i=i+1
                momentforwardsweep.append(overall_moment)
            plt.plot(alphas, momentforwardsweep, label='line' + str(storesweep))
            workbook.save('C:\\Users\\44786\\Documents\\University of Bristol\\dissertation\\data\\excel\\12ms' +str(storesweep)+' forward sweep' + str(twist) +'twist.xlsx')
    plt.legend()
    plt.show()
