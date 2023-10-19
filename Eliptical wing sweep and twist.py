#actuated wing
import math
import matplotlib.pyplot as plt
import openpyxl



#assume right wing is stationary
alphas=list(range(-10,21))
ya1=la1=root_chord=0.200
xa1=0.315
lb3=0.210

la3=0.205595
la2=0.200482
xto=0.307
xti = 0.315
q = 0.5 * 1.225 * 144  # where 12 is velocity
pi=math.pi

angle_oa1b1=math.radians(81.3)
angle_oa2b2=math.radians(71.207)
angle_oa3b3=math.radians(70.9)
angle_a1ob1=math.radians(18)
angle_a2ob2=math.radians(36)
angle_a3ob3=math.radians(36)
taper_a2=math.radians(77)
taper_a3=math.radians(41)
maxplate1=math.radians(30)

cog1= 0.1482
cog2= 0.1422
cog3= 0.1458
tcog1=math.radians(81)
tcog2=math.radians(54)
tcog3=math.radians(18)
Assumedweight=0.050


for twist in range(-10, 16,5):
    for sweep in range(0,41,10):
        storesweep = sweep
        sweep = abs(sweep)
        sweep = math.radians(sweep)

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet['A1'] = 'Roll(Mx)'
        worksheet['B1'] = 'exb.Inc'
        i = 2

        momentbackwardsweep = []




        if sweep == 0:



            for alpha in alphas:
                Cl1 = (0.0331480646 * alpha) - 0.000429646
                Cl2 = (0.0331480646 * alpha) - 0.000429646

                #constant wing
                xb3 = lb3 + xa1
                yb3 = 0.0015
                xa3 = la3 * math.cos(taper_a3) + xa1
                ya3 = la3 * math.sin(taper_a3)
                '''xb2 = lb2 * math.cos(taper_b2) + xa1
                yb2 = lb2 * math.sin(taper_b2)'''
                xa2 = la2 * math.cos(taper_a2) + xa1
                ya2 = la2 * math.sin(taper_a2)
                # compute initial moment at twist=0

                #section1
                c=0.220
                c = c/2
                moment1 = q * Cl1 * ( c * (( xti ** 2) - (xto ** 2)))

                #section2

                m = (ya2 - ya1) / (xa2 - xa1)
                c = ya2 - m * (xa2)

                m = m / 3
                c = c / 2
                moment2 = q * Cl2 * (m * ((xa2 ** 3) - (xa1 ** 3)) + c * ((xa2 ** 2) - (xa1 ** 2)))

                #section3

                m = (ya3 - ya2) / (xa3 - xa2)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment3 = q * Cl2 * (m * ((xa3 ** 3) - (xa2 ** 3)) + c * ((xa3 ** 2) - (xa2 ** 2)))

                #section4

                m = (yb3 - ya3) / (xb3 - xa3)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment4 = q * Cl2 * (m * ((xb3 ** 3) - (xa3 ** 3))+ c * ((xb3 ** 2) - (xa3 ** 2)))

                moment_neutral = moment1 + moment2 + moment3 + moment4

                Cl1 = (0.0331480646 * (alpha + twist)) - 0.000429646
                Cl2 = (0.0331480646 * (alpha + twist)) - 0.000429646

                # section1
                c = 0.220
                c = c / 2
                moment1 = q * Cl1 * (c * ((xti ** 2) - (xto ** 2)))

                # section2

                m = (ya2 - ya1) / (xa2 - xa1)
                c = ya2 - m * (xa2)

                m = m / 3
                c = c / 2
                moment2 = q * Cl2 * (m * ((xa2 ** 3) - (xa1 ** 3)) + c * ((xa2 ** 2) - (xa1 ** 2)))

                # section3

                m = (ya3 - ya2) / (xa3 - xa2)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment3 = q * Cl2 * (m * ((xa3 ** 3) - (xa2 ** 3)) + c * ((xa3 ** 2) - (xa2 ** 2)))

                # section4

                m = (yb3 - ya3) / (xb3 - xa3)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment4 = q * Cl2 * (m * ((xb3 ** 3) - (xa3 ** 3)) + c * ((xb3 ** 2) - (xa3 ** 2)))

                overallmoment = moment1 + moment2 + moment3 + moment4- moment_neutral

                worksheet['A' + str(i)] = overallmoment
                worksheet['B' + str(i)] = alpha
                i = i + 1

                momentbackwardsweep.append(overallmoment)
            plt.plot(alphas, momentbackwardsweep, label='line' + str(storesweep))
            workbook.save('C:\\Users\\44786\\Documents\\University of Bristol\\dissertation\\data\\excelactuatedwing\\ 12ms' + str(storesweep) + 'sweep' + str(twist) + 'twist.xlsx')

                #pretty much everything has fixed dimensions
        elif sweep > 0 and sweep <= maxplate1:
            Weightshiftrollingmoment = Assumedweight * (math.cos(tcog3)-math.cos(tcog3 + sweep))



            for alpha in alphas:
                # compute initial moment at sweep and twist=0
                Cl1 = (0.0331480646 * alpha) - 0.000429646
                Cl2 = (0.0331480646 * alpha) - 0.000429646

    # constant wing
                xb3 = lb3 + xa1
                yb3 = 0.0015
                xa3 = la3 * math.cos(taper_a3) + xa1
                ya3 = la3 * math.sin(taper_a3)
                '''xb2 = lb2 * math.cos(taper_b2) + xa1
                yb2 = lb2 * math.sin(taper_b2)'''
                xa2 = la2 * math.cos(taper_a2) + xa1
                ya2 = la2 * math.sin(taper_a2)
                # compute initial moment at twist=0

                # section1
                c = 0.220
                c = c / 2
                moment1 = q * Cl1 * (c * ((xti ** 2) - (xto ** 2)))

                # section2

                m = (ya2 - ya1) / (xa2 - xa1)
                c = ya2 - m * (xa2)

                m = m / 3
                c = c / 2
                moment2 = q * Cl2 * (m * ((xa2 ** 3) - (xa1 ** 3)) + c * ((xa2 ** 2) - (xa1 ** 2)))

                # section3

                m = (ya3 - ya2) / (xa3 - xa2)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment3 = q * Cl2 * (m * ((xa3 ** 3) - (xa2 ** 3)) + c * ((xa3 ** 2) - (xa2 ** 2)))

                # section4

                m = (yb3 - ya3) / (xb3 - xa3)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment4 = q * Cl2 * (m * ((xb3 ** 3) - (xa3 ** 3)) + c * ((xb3 ** 2) - (xa3 ** 2)))

                moment_neutral = moment1 + moment2 + moment3 + moment4

    #part that actually sweeps
                xb3 = lb3 * math.cos(sweep)
            #    yb3 = lb3 * math.sin(sweep) - xb3 * math.tan(sweep)
                yb3 = 0.0015
                xb3 = lb3 * math.cos(sweep) + xa1
                print('xb3=' +str(xb3)+' yb3='+ str(yb3))
                xa3 = la3 * math.cos(taper_a3 + sweep)
                ya3 = la3 * math.sin(taper_a3 + sweep) - xa3 * math.tan(sweep)
                xa3 = la3 * math.cos(taper_a3 + sweep) + xa1
                angle_a2oa3 = angle_a2ob2 - sweep
                lx23 = (la2 * math.sin(angle_oa2b2)) / (math.sin(pi - angle_oa2b2 - angle_a2oa3))
                xx23 = lx23 * math.cos(taper_a3 + sweep)
                yx23 = lx23 * math.sin(taper_a3 + sweep) - xx23 * math.tan(sweep)#xb3 might have to be changed for the sake of this line (check) i think to xx23. i think this issue repeats itself throughout the code hence all calculations need to be rechecked
                xx23 = lx23 * math.cos(taper_a3 + sweep) + xa1
                # plate 2 and 1 stay fixed
                print('xx23= ' +str(xx23) + ' xa3= '+str(xa3))

                Cl1 = (0.0331480646 * (alpha + twist)) - 0.000429646
                Cl2 = (0.0331480646 * (alpha + twist)) - 0.000429646
                # section1
                c = 0.220
                c = c / 2
                moment1 = q * Cl1 * (c * ((xti ** 2) - (xto ** 2)))

                # section2

                m = (ya2 - ya1) / (xa2 - xa1)
                c = ya2 - m * (xa2)

                m = m / 3
                c = c / 2
                moment2 = q * Cl2 * (m * ((xa2 ** 3) - (xa1 ** 3)) + c * ((xa2 ** 2) - (xa1 ** 2)))

                # section3

                m = (yx23 - ya2) / (xx23 - xa2)
                c = yx23 - m * (xx23)

                m = m / 3
                c = c / 2
                moment3 = q * Cl2 * (m * ((xx23 ** 3) - (xa2 ** 3)) + c * ((xx23 ** 2) - (xa2 ** 2)))

                # section4

                m = (ya3 - yx23) / (xa3 - xx23)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment4 = q * Cl2 * (m * ((xa3 ** 3) - (xx23 ** 3)) + c * ((xa3 ** 2) - (xx23 ** 2)))

                # section5

                m = (yb3 - ya3) / (xb3 - xa3)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment5 = q * Cl2 * (m * ((xb3 ** 3) - (xa3 ** 3)) + c * ((xb3 ** 2) - (xa3 ** 2)))

                overallmoment = moment1 + moment2 + moment3 + moment4 + moment5 - moment_neutral + Weightshiftrollingmoment

                worksheet['A' + str(i)] = overallmoment
                worksheet['B' + str(i)] = alpha
                i = i + 1

                momentbackwardsweep.append(overallmoment)
            plt.plot(alphas, momentbackwardsweep, label='line' + str(storesweep) + 'twist' + str(twist))
            workbook.save('C:\\Users\\44786\\Documents\\University of Bristol\\dissertation\\data\\excelactuatedwing\\ 12ms' + str(storesweep) + 'sweep' + str(twist) + 'twist.xlsx')


        else:

            Weightshiftrollingmoment = Assumedweight *((math.cos(tcog3) - math.cos(tcog3 + sweep))+ (math.cos(tcog2) - math.cos(tcog2 + (sweep-maxplate1))))

            for alpha in alphas:
                # compute initial moment at sweep and twist=0

                Cl1 = (0.0331480646 * alpha) - 0.000429646
                Cl2 = (0.0331480646 * alpha) - 0.000429646

    # constant wing
                xb3 = lb3 + xa1
                yb3 = 0.0015
                xa3 = la3 * math.cos(taper_a3) + xa1
                ya3 = la3 * math.sin(taper_a3)
                '''xb2 = lb2 * math.cos(taper_b2) + xa1
                yb2 = lb2 * math.sin(taper_b2)'''
                xa2 = la2 * math.cos(taper_a2) + xa1
                ya2 = la2 * math.sin(taper_a2)
                # compute initial moment at twist=0

                # section1
                c = 0.220
                c = c / 2
                moment1 = q * Cl1 * (c * ((xti ** 2) - (xto ** 2)))

                # section2

                m = (ya2 - ya1) / (xa2 - xa1)
                c = ya2 - m * (xa2)

                m = m / 3
                c = c / 2
                moment2 = q * Cl2 * (m * ((xa2 ** 3) - (xa1 ** 3)) + c * ((xa2 ** 2) - (xa1 ** 2)))

                # section3

                m = (ya3 - ya2) / (xa3 - xa2)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment3 = q * Cl2 * (m * ((xa3 ** 3) - (xa2 ** 3)) + c * ((xa3 ** 2) - (xa2 ** 2)))

                # section4

                m = (yb3 - ya3) / (xb3 - xa3)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment4 = q * Cl2 * (m * ((xb3 ** 3) - (xa3 ** 3))+ c * ((xb3 ** 2) - (xa3 ** 2)))

                moment_neutral = moment1 + moment2 + moment3 + moment4

    # part that actually sweeps

                xb3=lb3*math.cos(sweep)
                yb3=0.0015
                xb3 = lb3 * math.cos(sweep) + xa1
                xa3=la3*math.cos(taper_a3+sweep)
                ya3=la3*math.sin(taper_a3+sweep)- xa3*math.tan(sweep)
                xa3 = la3 * math.cos(taper_a3 + sweep) + xa1
                '''xb2=lb2*math.cos(taper_b2+ sweep -maxplate1) + xa1
                yb2=lb2*math.sin(taper_b2+ sweep -maxplate1)- xb2*math.tan(sweep)'''
                xa2=la2*math.cos(taper_a2+ sweep -maxplate1)
                ya2=la2*math.sin(taper_a2+ sweep -maxplate1)- xa2*math.tan(sweep)
                xa2 = la2 * math.cos(taper_a2 + sweep - maxplate1) + xa1
                angle_a2oa3=angle_a2ob2-maxplate1
                angle_a1oa2 = angle_a1ob1 - sweep + maxplate1
                lx23 = (la2 * math.sin(angle_oa2b2))/(math.sin(pi-angle_oa2b2-angle_a2oa3))
                lx12 = (la1 * math.sin(angle_oa1b1))/(math.sin(pi-angle_oa1b1-angle_a1oa2))
                xx23=lx23*math.cos(taper_a3+sweep)
                yx23=lx23*math.sin(taper_a3+sweep) - xx23*math.tan(sweep)
                xx23 = lx23 * math.cos(taper_a3 + sweep) + xa1
                xx12=lx12*math.cos(taper_a2+ sweep -maxplate1)
                yx12=lx12*math.sin(taper_a2+ sweep -maxplate1) - xx12*math.tan(sweep)
                xx12 = lx12 * math.cos(taper_a2 + sweep - maxplate1) + xa1

                Cl1 = (0.0331480646 * (alpha + twist)) - 0.000429646
                Cl2 = (0.0331480646 * (alpha + twist)) - 0.000429646

                # section1
                c = 0.220
                c = c / 2
                moment1 = q * Cl1 * (c * ((xti ** 2) - (xto ** 2)))

                # section2

                m = (yx12 - ya1) / (xx12 - xa1)
                c = ya1 - m * (xa1)

                m = m / 3
                c = c / 2
                moment2 = q * Cl2 * (m * ((xx12 ** 3) - (xa1 ** 3)) + c * ((xx12 ** 2) - (xa1 ** 2)))

                # section3

                m = (ya2 - yx12) / (xa2 - xx12)
                c = ya2 - m * (xa2)

                m = m / 3
                c = c / 2
                moment3 = q * Cl2 * (m * ((xa2 ** 3) - (xx12 ** 3)) + c * ((xa2 ** 2) - (xx12 ** 2)))

                # section4

                m = (yx23 - ya2) / (xx23 - xa2)
                c = yx23 - m * (xx23)

                m = m / 3
                c = c / 2
                moment4 = q * Cl2 * (m * ((xx23 ** 3) - (xa2 ** 3)) + c * ((xx23 ** 2) - (xa2 ** 2)))

                # section5
                m = (ya3 - yx23) / (xa3 - xx23)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment5 = q * Cl2 * (m * ((xa3 ** 3) - (xx23 ** 3)) + c * ((xa3 ** 2) - (xx23 ** 2)))

                # section6

                m = (yb3 - ya3) / (xb3 - xa3)
                c = ya3 - m * (xa3)

                m = m / 3
                c = c / 2
                moment6 = q * Cl2 * (m * ((xb3 ** 3) - (xa3 ** 3)) + c * ((xb3 ** 2) - (xa3 ** 2)))

                overallmoment = moment1 + moment2 + moment3 + moment4 + moment5 + moment6 - moment_neutral + Weightshiftrollingmoment

                worksheet['A' + str(i)] = overallmoment
                worksheet['B' + str(i)] = alpha
                i = i + 1

                momentbackwardsweep.append(overallmoment)
            plt.plot(alphas, momentbackwardsweep, label='line' + str(storesweep))
            workbook.save('C:\\Users\\44786\\Documents\\University of Bristol\\dissertation\\data\\excelactuatedwing\\ 12ms' + str(storesweep) + 'sweep' + str(twist) + 'twist.xlsx')
    plt.legend()
    plt.show()

# Define constants

'''tip_length = 210
diagonal = 239.0237182
tip_chord=114.1592654
root_chord=0.200
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
distance_of_trapeziumcog=100
weight_of_morphing_section = 0.60


for twist in range(-10, 16,5):
    momentbackwardsweep = []
    momentforwardsweep = []

    for sweep in range(-40, 41, 10):
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
                m = m / 3
                c = c / 2
                momentneutral = q * Cl * (m * ((D1 ** 3) - (D4 ** 3) + c * ((D1 ** 2) - (D4 ** 2))))

                Cl = (0.0331480646 * (alpha + twist)) - 0.000429646

                # momentbackwardsweep = []
                # momentforwardsweep = []

                # compute initial moment at twist=0
                D1 = (D4 + tip_length)
                m = (tip_chord - root_chord) / (D1 - D4)
                c = tip_chord - m * (D1)
                m = m / 3
                c = c / 2
                twistmoment = q * Cl * (m * ((D1 ** 3) - (D4 ** 3) + c * ((D1 ** 2) - (D4 ** 2))))

                Moment = twistmoment - momentneutral
                momentbackwardsweep.append(Moment)
                momentforwardsweep.append(Moment)
            plt.plot(alphas, momentbackwardsweep, label='line 0 twist'+ str(twist))

        elif sweep < 0 :
            storesweep = sweep
            sweep =abs(sweep)
            sweep = math.radians(sweep)
            Weightshiftrollingmoment = weight_of_morphing_section * ((distance_of_trapeziumcog+D4)-(distance_of_trapeziumcog*(math.cos(sweep))+D4))


            for alpha in alphas:
                Cl = 0.0331480646 * alpha -0.000429646

                # compute neutral wing moment at sweep=0
                D1 = (D4 + tip_length)
                m = (tip_chord - root_chord) / (D1 - D4)
                c = tip_chord - m * (D1)
                m = m / 3
                c = c / 2
                momentneutral = q * Cl * (m * ((D1 ** 3) - (D4 ** 3) + c * ((D1 ** 2) - (D4 ** 2))))


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
                Moment1 = q * Cl * (m * ((D2 ** 3) - (D4 ** 3) + c * ((D2 ** 2) - (D4 ** 2))))
                m = -y / (D1 - D2)
                c = - m * (D1)
                m = m / 3
                c = c / 2
                Moment2 = q * Cl * (m * ((D1 ** 3) - (D2 ** 3) + c * ((D1 ** 2) - (D2 ** 2))))
                overall_moment =  ( Moment2 + Moment1) - momentneutral + Weightshiftrollingmoment
                momentbackwardsweep.append(overall_moment)
            plt.plot(alphas, momentbackwardsweep, label='line' + str(storesweep))


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
                momentneutral = q * Cl * (m * ((D1 ** 3) - (D4 ** 3) + c * ((D1 ** 2) - (D4 ** 2))))

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
                overall_moment = (Moment2 + Moment1 + Moment3) - momentneutral +Weightshiftrollingmoment
                momentforwardsweep.append(overall_moment)
            plt.plot(alphas, momentforwardsweep, label='line' + str(storesweep))
plt.legend()
plt.show()'''
