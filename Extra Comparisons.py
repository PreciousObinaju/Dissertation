import pandas as pd
import matplotlib.pyplot as plt

flowtwelvenw=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\Symmetric wing.csv")
flowtwelvenwfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\5 twist.csv")
flowtwelvenwnfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\-5 twist.csv")
flowtwelvenwthirtynfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\10 twist.csv")
flowtwelvenwthirtyfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\flow 5 tapered wing models\-10 twist.csv")
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


fatwelvenw=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\Symmetric wing.csv")
fatwelvenwfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\5 twist.csv")
fatwelvenwnfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\-5 twist.csv")
fatwelvenwthirtyfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\10 twist.csv")
fatwelvenwthirtynfive=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excelactuatedwing\-10 twist.csv")
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


plt.plot(fatwelvenw['Alpha'], fatwelvenw['M_(N.m)'], label='Symmetric wing fls', color='blue')
plt.plot(fatwelvenwfive['Alpha'], fatwelvenwfive['M_(N.m)'], label='5° twist fls', color='orange')
plt.plot(fatwelvenwnfive['Alpha'], fatwelvenwnfive['M_(N.m)'], label='-5° twist fls', color='green')
plt.plot(fatwelvenwthirtyfive['Alpha'], fatwelvenwthirtyfive['M_(N.m)'], label='-30° sweep 5° twist fls', color='Magenta')
plt.plot(fatwelvenwthirtynfive['Alpha'], fatwelvenwthirtynfive['M_(N.m)'], label='-30° sweep -5° twist fls', color='brown')
plt.plot(flowtwelvenw['Alpha'], flowtwelvenw['M_(N.m)'], label='Symmetric wing', color='blue',linestyle='--')
plt.plot(flowtwelvenwfive['Alpha'], flowtwelvenwfive['M_(N.m)'], label='5° twist ', color='orange',linestyle='--')
plt.plot(flowtwelvenwnfive['Alpha'], flowtwelvenwnfive['M_(N.m)'], label='-5° twist ', color='green',linestyle='--')
plt.plot(flowtwelvenwthirtynfive['Alpha'], flowtwelvenwthirtynfive['M_(N.m)'], label='-30° sweep -5° twist', color='Magenta',linestyle='--')
plt.plot(flowtwelvenwthirtyfive['Alpha'], flowtwelvenwthirtyfive['M_(N.m)'], label='-30° sweep 5° twist ', color='brown',linestyle='--')



# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Pitching Moment (My)')
#plt.title('fa Theory Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(fatwelvenw['Alpha'], fatwelvenw['N_(N.m)'], label='Symmetric wing fls', color='blue')
plt.plot(fatwelvenwfive['Alpha'], fatwelvenwfive['N_(N.m)'], label='5° twist fls', color='orange')
plt.plot(fatwelvenwnfive['Alpha'], fatwelvenwnfive['N_(N.m)'], label='-5° twist fls', color='green')
plt.plot(fatwelvenwthirtyfive['Alpha'], fatwelvenwthirtyfive['N_(N.m)'], label='-30° sweep 5° twist fls', color='magenta')
plt.plot(fatwelvenwthirtynfive['Alpha'], fatwelvenwthirtynfive['N_(N.m)'], label='-30° sweep -5° twist fls', color='brown')
plt.plot(flowtwelvenw['Alpha'], flowtwelvenw['N_(N.m)'], label='Symmetric wing', color='blue',linestyle='--')
plt.plot(flowtwelvenwfive['Alpha'], flowtwelvenwfive['N_(N.m)'], label='5° twist ', color='orange',linestyle='--')
plt.plot(flowtwelvenwnfive['Alpha'], flowtwelvenwnfive['N_(N.m)'], label='-5° twist ', color='green',linestyle='--')
plt.plot(flowtwelvenwthirtynfive['Alpha'], flowtwelvenwthirtynfive['N_(N.m)'], label='-30° sweep -5° twist', color='magenta',linestyle='--')
plt.plot(flowtwelvenwthirtyfive['Alpha'], flowtwelvenwthirtyfive['N_(N.m)'], label='-30° sweep 5° twist ', color='brown',linestyle='--')



# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Yawing Moment (Mz)')
#plt.title('fa Theory Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

