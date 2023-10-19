import pandas as pd
import matplotlib.pyplot as plt

striptwelvenw=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\ 12ms0sweep0twist.xlsx")
striptwelvenwfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\ 12ms0sweep5twist.xlsx")
striptwelvenwnfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\ 12ms0sweep-5twist.xlsx")
striptwelvenwten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\ 12ms0sweep10twist.xlsx")
striptwelvenwnten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\ 12ms0sweep-10twist.xlsx")
striptwelvenwfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\ 12ms0sweep15twist.xlsx")

striptwelveten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep0twist.xlsx")
striptwelvetenfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep5twist.xlsx")
striptwelvetennfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep-5twist.xlsx")
striptwelvetenten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep10twist.xlsx")
striptwelvetennten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep-10twist.xlsx")
striptwelvetenfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep15twist.xlsx")

striptwelvetwenty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20backward sweep0twist.xlsx")
striptwelvetwentyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20backward sweep5twist.xlsx")
striptwelvetwentynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20backward sweep-5twist.xlsx")
striptwelvetwentyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20backward sweep10twist.xlsx")
striptwelvetwentynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20backward sweep-10twist.xlsx")
striptwelvetwentyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20backward sweep15twist.xlsx")

striptwelvethirty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30backward sweep0twist.xlsx")
striptwelvethirtyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30backward sweep5twist.xlsx")
striptwelvethirtynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30backward sweep-5twist.xlsx")
striptwelvethirtyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30backward sweep10twist.xlsx")
striptwelvethirtynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30backward sweep-10twist.xlsx")
striptwelvethirtyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30backward sweep15twist.xlsx")

striptwelveforty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40backward sweep0twist.xlsx")
striptwelvefortyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40backward sweep5twist.xlsx")
striptwelvefortynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40backward sweep-5twist.xlsx")
striptwelvefortyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40backward sweep10twist.xlsx")
striptwelvefortynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40backward sweep-10twist.xlsx")
striptwelvefortyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40backward sweep15twist.xlsx")

fstriptwelveten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10 forward sweep0twist.xlsx")
fstriptwelvetenfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10 forward sweep5twist.xlsx")
fstriptwelvetennfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10 forward sweep-5twist.xlsx")
fstriptwelvetenten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10 forward sweep10twist.xlsx")
fstriptwelvetennten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10 forward sweep-10twist.xlsx")
fstriptwelvetenfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10 forward sweep15twist.xlsx")

fstriptwelvetwenty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20 forward sweep0twist.xlsx")
fstriptwelvetwentyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20 forward sweep5twist.xlsx")
fstriptwelvetwentynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20 forward sweep-5twist.xlsx")
fstriptwelvetwentyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20 forward sweep10twist.xlsx")
fstriptwelvetwentynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20 forward sweep-10twist.xlsx")
fstriptwelvetwentyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms20 forward sweep15twist.xlsx")

fstriptwelvethirty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30 forward sweep0twist.xlsx")
fstriptwelvethirtyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30 forward sweep5twist.xlsx")
fstriptwelvethirtynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30 forward sweep-5twist.xlsx")
fstriptwelvethirtyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30 forward sweep10twist.xlsx")
fstriptwelvethirtynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30 forward sweep-10twist.xlsx")
fstriptwelvethirtyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30 forward sweep15twist.xlsx")

fstriptwelveforty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40 forward sweep0twist.xlsx")
fstriptwelvefortyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40 forward sweep5twist.xlsx")
fstriptwelvefortynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40 forward sweep-5twist.xlsx")
fstriptwelvefortyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40 forward sweep10twist.xlsx")
fstriptwelvefortynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40 forward sweep-10twist.xlsx")
fstriptwelvefortyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms40 forward sweep15twist.xlsx")

 
plt.plot(striptwelvenw['exb.Inc'], striptwelvenw['Roll(Mx)'], label='Symmetric wing', color='blue')
plt.plot(striptwelvenwfive['exb.Inc'], striptwelvenwfive['Roll(Mx)'], label='5°_twist ')
plt.plot(striptwelvenwnfive['exb.Inc'], striptwelvenwnfive['Roll(Mx)'], label='-5° twist ', color='green')
plt.plot(striptwelvenwten['exb.Inc'], striptwelvenwten['Roll(Mx)'], label='10° twist ', color='magenta')
plt.plot(striptwelvenwnten['exb.Inc'], striptwelvenwnten['Roll(Mx)'], label='-10° twist ', color='brown')
plt.plot(striptwelvenwfifteen['exb.Inc'], striptwelvenwfifteen['Roll(Mx)'], label='15° twist ', color='purple')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Strip Theory Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(striptwelvenw['exb.Inc'], striptwelvenw['Roll(Mx)'], label='Symmetric wing', color='blue')
plt.plot(striptwelveten['exb.Inc'], striptwelveten['Roll(Mx)'], label='-10° sweep')
plt.plot(striptwelvetwenty['exb.Inc'], striptwelvetwenty['Roll(Mx)'], label='-20° sweep')
plt.plot(striptwelvethirty['exb.Inc'], striptwelvethirty['Roll(Mx)'], label='-30° sweep')
plt.plot(striptwelveforty['exb.Inc'], striptwelveforty['Roll(Mx)'], label='-40° sweep')
plt.plot(fstriptwelveten['exb.Inc'], fstriptwelveten['Roll(Mx)'], label='10° sweep')
plt.plot(fstriptwelvetwenty['exb.Inc'], fstriptwelvetwenty['Roll(Mx)'], label='20° sweep')
plt.plot(fstriptwelvethirty['exb.Inc'], fstriptwelvethirty['Roll(Mx)'], label='30° sweep')
plt.plot(fstriptwelveforty['exb.Inc'], fstriptwelveforty['Roll(Mx)'], label='40° sweep')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Strip Theory Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
 


flowtwelvenw=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\Symmetric wing.csv")
flowtwelvenwfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\5 twist.csv")
flowtwelvenwnfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\-5 twist.csv")
flowtwelvenwten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\10 twist.csv")
flowtwelvenwnten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\-10 twist.csv")
flowtwelvenwfifteen=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\15 twist.csv")

flowtwelveten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\10 sweep.csv")
flowtwelvetenfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\10 sweep 5 twist.csv")
flowtwelvetennfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\10 sweep -5 twist.csv")
flowtwelvetenten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\10 sweep 10 twist.csv")
flowtwelvetennten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\10 sweep -10twist.csv")
flowtwelvetenfifteen=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\10 sweep 15 twist.csv")

flowtwelvetwenty=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\20 sweep.csv")
flowtwelvetwentyfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\20 sweep 5 twist.csv")
flowtwelvetwentynfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\20 sweep -5 twist.csv")
flowtwelvetwentyten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\20 sweep 10 twist.csv")
flowtwelvetwentynten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\20 sweep -10twist.csv")
flowtwelvetwentyfifteen=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\20 sweep 15 twist.csv")

flowtwelvethirty=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\30 sweep.csv")
flowtwelvethirtyfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\30 sweep 5 twist.csv")
flowtwelvethirtynfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\30 sweep -5 twist.csv")
flowtwelvethirtyten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\30 sweep 10 twist.csv")
flowtwelvethirtynten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\30 sweep -10twist.csv")
flowtwelvethirtyfifteen=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\30 sweep 15 twist.csv")

flowtwelveforty=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\40 sweep.csv")
flowtwelvefortyfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\40 sweep 5 twist.csv")
flowtwelvefortynfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\40 sweep -5 twist.csv")
flowtwelvefortyten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\40 sweep 10 twist.csv")
flowtwelvefortynten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\40 sweep -10twist.csv")
flowtwelvefortyfifteen=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\40 sweep 15 twist.csv")


 
plt.plot(flowtwelvenw['Alpha'], flowtwelvenw['L_(N.m)'], label='Symmetric wing', color='blue')
plt.plot(flowtwelvenwfive['Alpha'], flowtwelvenwfive['L_(N.m)'], label='5° twist ', color='orange')
plt.plot(flowtwelvenwnfive['Alpha'], flowtwelvenwnfive['L_(N.m)'], label='-5° twist ', color='green')
plt.plot(flowtwelvenwten['Alpha'], flowtwelvenwten['L_(N.m)'], label='10° twist ', color='magenta')
plt.plot(flowtwelvenwnten['Alpha'], flowtwelvenwnten['L_(N.m)'], label='-10° twist ', color='brown')
plt.plot(flowtwelvenwfifteen['Alpha'], flowtwelvenwfifteen['L_(N.m)'], label='15° twist ', color='purple')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Flow Theory Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(flowtwelvenw['Alpha'], flowtwelvenw['L_(N.m)'], label='Symmetric wing', color='blue')
plt.plot(flowtwelveten['Alpha'], flowtwelveten['L_(N.m)'], label='-10° sweep')
plt.plot(flowtwelvetwenty['Alpha'], flowtwelvetwenty['L_(N.m)'], label='-20° sweep')
plt.plot(flowtwelvethirty['Alpha'], flowtwelvethirty['L_(N.m)'], label='-30° sweep')
plt.plot(flowtwelveforty['Alpha'], flowtwelveforty['L_(N.m)'], label='-40° sweep')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Flow 5 Theory Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show() 

astriptwelvenw=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms0sweep0twist.xlsx")
astriptwelvenwfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms0sweep5twist.xlsx")
astriptwelvenwnfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms0sweep-5twist.xlsx")
astriptwelvenwten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms0sweep10twist.xlsx")
astriptwelvenwnten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms0sweep-10twist.xlsx")
astriptwelvenwfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms0sweep15twist.xlsx")

astriptwelveten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms10sweep0twist.xlsx")
astriptwelvetenfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms10sweep5twist.xlsx")
astriptwelvetennfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms10sweep-5twist.xlsx")
astriptwelvetenten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms10sweep10twist.xlsx")
astriptwelvetennten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms10sweep-10twist.xlsx")
astriptwelvetenfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms10sweep15twist.xlsx")

astriptwelvetwenty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms20sweep0twist.xlsx")
astriptwelvetwentyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms20sweep5twist.xlsx")
astriptwelvetwentynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms20sweep-5twist.xlsx")
astriptwelvetwentyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms20sweep10twist.xlsx")
astriptwelvetwentynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms20sweep-10twist.xlsx")
astriptwelvetwentyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms20sweep15twist.xlsx")

astriptwelvethirty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms30sweep0twist.xlsx")
astriptwelvethirtyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms30sweep5twist.xlsx")
astriptwelvethirtynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms30sweep-5twist.xlsx")
astriptwelvethirtyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms30sweep10twist.xlsx")
astriptwelvethirtynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms30sweep-10twist.xlsx")
astriptwelvethirtyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms30sweep15twist.xlsx")

astriptwelveforty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms40sweep0twist.xlsx")
astriptwelvefortyfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms40sweep5twist.xlsx")
astriptwelvefortynfive=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms40sweep-5twist.xlsx")
astriptwelvefortyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms40sweep10twist.xlsx")
astriptwelvefortynten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms40sweep-10twist.xlsx")
astriptwelvefortyfifteen=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\ 12ms40sweep15twist.xlsx")


plt.plot(astriptwelvenw['exb.Inc'], astriptwelvenw['Roll(Mx)'], label='Symmetric wing fls', color='blue')
plt.plot(astriptwelvenwfive['exb.Inc'], astriptwelvenwfive['Roll(Mx)'], label='5° twist fls', color='orange')
plt.plot(astriptwelvenwnfive['exb.Inc'], astriptwelvenwnfive['Roll(Mx)'], label='-5° twist fls', color='green')
plt.plot(astriptwelvenwten['exb.Inc'], astriptwelvenwten['Roll(Mx)'], label='10° twist fls', color='magenta')
plt.plot(astriptwelvenwnten['exb.Inc'], astriptwelvenwnten['Roll(Mx)'], label='-10° twist fls', color='brown')
plt.plot(astriptwelvenwfifteen['exb.Inc'], astriptwelvenwfifteen['Roll(Mx)'], label='15° twist fls', color='purple')
plt.plot(striptwelvenw['exb.Inc'], striptwelvenw['Roll(Mx)'], label='Symmetric wing', color='blue',linestyle='--')
plt.plot(striptwelvenwfive['exb.Inc'], striptwelvenwfive['Roll(Mx)'], label='5°_twist ', color='orange',linestyle='--')
plt.plot(striptwelvenwnfive['exb.Inc'], striptwelvenwnfive['Roll(Mx)'], label='-5° twist ', color='green',linestyle='--')
plt.plot(striptwelvenwten['exb.Inc'], striptwelvenwten['Roll(Mx)'], label='10° twist ', color='magenta',linestyle='--')
plt.plot(striptwelvenwnten['exb.Inc'], striptwelvenwnten['Roll(Mx)'], label='-10° twist ', color='brown',linestyle='--')
plt.plot(striptwelvenwfifteen['exb.Inc'], striptwelvenwfifteen['Roll(Mx)'], label='15° twist ', color='purple',linestyle='--')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Strip Theory Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(astriptwelvenw['exb.Inc'], astriptwelvenw['Roll(Mx)'], label='Symmetric wing', color='blue')
plt.plot(astriptwelveten['exb.Inc'], astriptwelveten['Roll(Mx)'], label='-10° sweep fls', color='red')
plt.plot(astriptwelvetwenty['exb.Inc'], astriptwelvetwenty['Roll(Mx)'], label='-20° sweep fls',color='pink')
plt.plot(astriptwelvethirty['exb.Inc'], astriptwelvethirty['Roll(Mx)'], label='-30° sweep fls',color='brown')
plt.plot(astriptwelveforty['exb.Inc'], astriptwelveforty['Roll(Mx)'], label='-40° sweep fls',color='orange')
plt.plot(striptwelveten['exb.Inc'], striptwelveten['Roll(Mx)'], label='-10° sweep',linestyle='--', color='red')
plt.plot(striptwelvetwenty['exb.Inc'], striptwelvetwenty['Roll(Mx)'], label='-20° sweep',linestyle='--',color='pink')
plt.plot(striptwelvethirty['exb.Inc'], striptwelvethirty['Roll(Mx)'], label='-30° sweep',linestyle='--',color='brown')
plt.plot(striptwelveforty['exb.Inc'], striptwelveforty['Roll(Mx)'], label='-40° sweep',linestyle='--',color='orange')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Strip Theory Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(astriptwelvenw['exb.Inc'], astriptwelvenw['Roll(Mx)'], label='Symmetric wing', color='blue')
plt.plot(astriptwelveforty['exb.Inc'], astriptwelveforty['Roll(Mx)'], label='-40° sweep')
plt.plot(astriptwelveten['exb.Inc'], astriptwelveten['Roll(Mx)'], label='-10° sweep')
plt.plot(astriptwelvetwenty['exb.Inc'], astriptwelvetwenty['Roll(Mx)'], label='-20° sweep')
plt.plot(astriptwelvethirty['exb.Inc'], astriptwelvethirty['Roll(Mx)'], label='-30° sweep')


# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Strip Theory Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

fatwelvenw=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\Symmetric wing.csv")
fatwelvenwfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\5 twist.csv")
fatwelvenwnfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\-5 twist.csv")
fatwelvenwten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\10 twist.csv")
fatwelvenwnten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\-10 twist.csv")
fatwelvenwfifteen=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\15 twist.csv")


fatwelveten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\10 sweep.csv")
fatwelvetwenty=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\20 sweep.csv")
fatwelvethirty=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\30 sweep.csv")
fatwelveforty=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\40 sweep.csv")

fatwelvetenfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\10 sweep 5 twist.csv")
fatwelvetennfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\10 sweep -5 twist.csv")
fatwelvethirtyfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\30 sweep 5 twist.csv")
fatwelvethirtynfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\30 sweep -5 twist.csv")
fatwelvefortyten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\40 sweep 10 twist.csv")
fatwelvefortynten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\40 sweep -10 twist.csv")

plt.plot(fatwelvenw['Alpha'], fatwelvenw['L_(N.m)'], label='Symmetric wing fls', color='blue')
plt.plot(fatwelvenwfive['Alpha'], fatwelvenwfive['L_(N.m)'], label='5° twist fls', color='orange')
plt.plot(fatwelvenwnfive['Alpha'], fatwelvenwnfive['L_(N.m)'], label='-5° twist fls', color='green')
plt.plot(fatwelvenwten['Alpha'], fatwelvenwten['L_(N.m)'], label='10° twist fls', color='magenta')
plt.plot(fatwelvenwnten['Alpha'], fatwelvenwnten['L_(N.m)'], label='-10° twist fls', color='brown')
plt.plot(fatwelvenwfifteen['Alpha'], fatwelvenwfifteen['L_(N.m)'], label='15° twist fls', color='purple')
plt.plot(flowtwelvenw['Alpha'], flowtwelvenw['L_(N.m)'], label='Symmetric wing', color='blue',linestyle='--')
plt.plot(flowtwelvenwfive['Alpha'], flowtwelvenwfive['L_(N.m)'], label='5° twist ', color='orange',linestyle='--')
plt.plot(flowtwelvenwnfive['Alpha'], flowtwelvenwnfive['L_(N.m)'], label='-5° twist ', color='green',linestyle='--')
plt.plot(flowtwelvenwten['Alpha'], flowtwelvenwten['L_(N.m)'], label='10° twist ', color='magenta',linestyle='--')
plt.plot(flowtwelvenwnten['Alpha'], flowtwelvenwnten['L_(N.m)'], label='-10° twist ', color='brown',linestyle='--')
plt.plot(flowtwelvenwfifteen['Alpha'], flowtwelvenwfifteen['L_(N.m)'], label='15° twist ', color='purple',linestyle='--')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('fa Theory Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(fatwelvenw['Alpha'], fatwelvenw['L_(N.m)'], label='Symmetric wing', color='blue')
plt.plot(fatwelveten['Alpha'], fatwelveten['L_(N.m)'], label='-10° sweep')
plt.plot(fatwelvetwenty['Alpha'], fatwelvetwenty['L_(N.m)'], label='-20° sweep')
plt.plot(fatwelvethirty['Alpha'], fatwelvethirty['L_(N.m)'], label='-30° sweep')
plt.plot(fatwelveforty['Alpha'], fatwelveforty['L_(N.m)'], label='-40° sweep')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('fa 5 Theory Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(fatwelvenw['Alpha'], fatwelvenw['L_(N.m)'], label='Symmetric wing', color='blue')
plt.plot(fatwelveten['Alpha'], fatwelveten['L_(N.m)'], label='10° sweep fls', color='red')
plt.plot(fatwelvetwenty['Alpha'], fatwelvetwenty['L_(N.m)'],  label='-20° sweep  fls', color='pink')
plt.plot(fatwelvethirty['Alpha'], fatwelvethirty['L_(N.m)'], label='-30° sweep  fls',color='brown')
plt.plot(fatwelveforty['Alpha'], fatwelveforty['L_(N.m)'], label='-40° sweep  fls',color='orange')
plt.plot(flowtwelveten['Alpha'], flowtwelveten['L_(N.m)'], label='-10° sweep',linestyle='--', color='red')
plt.plot(flowtwelvetwenty['Alpha'], flowtwelvetwenty['L_(N.m)'], label='-20° sweep',linestyle='--', color='pink')
plt.plot(flowtwelvethirty['Alpha'], flowtwelvethirty['L_(N.m)'], label='-30° sweep',linestyle='--',color='brown')
plt.plot(flowtwelveforty['Alpha'], flowtwelveforty['L_(N.m)'], label='-40° sweep',linestyle='--',color='orange')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Strip Theory Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(fatwelvenw['Alpha'], fatwelvenw['M_(N.m)'], label='Symmetric wing', color='blue')
plt.plot(fatwelveten['Alpha'], fatwelveten['M_(N.m)'], label='-10° sweep fls', color='red')
plt.plot(fatwelvetwenty['Alpha'], fatwelvetwenty['M_(N.m)'],  label='-20° sweep  fls', color='pink')
plt.plot(fatwelvethirty['Alpha'], fatwelvethirty['M_(N.m)'], label='-30° sweep  fls',color='brown')
plt.plot(fatwelveforty['Alpha'], fatwelveforty['M_(N.m)'], label='-40° sweep  fls',color='orange')
plt.plot(flowtwelveten['Alpha'], flowtwelveten['M_(N.m)'], label='-10° sweep',linestyle='--', color='red')
plt.plot(flowtwelvetwenty['Alpha'], flowtwelvetwenty['M_(N.m)'], label='-20° sweep',linestyle='--', color='pink')
plt.plot(flowtwelvethirty['Alpha'], flowtwelvethirty['M_(N.m)'], label='-30° sweep',linestyle='--',color='brown')
plt.plot(flowtwelveforty['Alpha'], flowtwelveforty['M_(N.m)'], label='-40° sweep',linestyle='--',color='orange')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Pitching Moment (Mx)')
#plt.title('Strip Theory Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(fatwelvenw['Alpha'], fatwelvenw['N_(N.m)'], label='Symmetric wing', color='blue')
plt.plot(fatwelveten['Alpha'], fatwelveten['N_(N.m)'], label='-10° sweep fls', color='red')
plt.plot(fatwelvetwenty['Alpha'], fatwelvetwenty['N_(N.m)'],  label='-20° sweep  fls', color='pink')
plt.plot(fatwelvethirty['Alpha'], fatwelvethirty['N_(N.m)'], label='-30° sweep  fls',color='brown')
plt.plot(fatwelveforty['Alpha'], fatwelveforty['N_(N.m)'], label='-40° sweep  fls',color='orange')
plt.plot(flowtwelveten['Alpha'], flowtwelveten['N_(N.m)'], label='-10° sweep',linestyle='--', color='red')
plt.plot(flowtwelvetwenty['Alpha'], flowtwelvetwenty['N_(N.m)'], label='-20° sweep',linestyle='--', color='pink')
plt.plot(flowtwelvethirty['Alpha'], flowtwelvethirty['N_(N.m)'], label='-30° sweep',linestyle='--',color='brown')
plt.plot(flowtwelveforty['Alpha'], flowtwelveforty['N_(N.m)'], label='-40° sweep',linestyle='--',color='orange')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Yawing Moment (Mx)')
#plt.title('Strip Theory Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()