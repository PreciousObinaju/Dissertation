import pandas as pd
import matplotlib.pyplot as plt


# Read the CSV file into a DataFrame
tennw = pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\10ms normal wing.csv")
tententen= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\10ms 10 backward wing 10 twist.csv")
tentennten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\10ms 10 backward wing 20 twist.csv")
tenten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\10ms 10 backward wing(-2 twice).csv")
tenthirtyten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\10ms 30 backward wing 10 twist.csv")
tenthirty= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\10ms 30 backward wing.csv")
tenbar= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\10ms bar.csv")
twelvetenten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 10 backward wing 10 twist.csv")
twelvetennten = pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 10 backward wing 20 twist.csv")
twelveten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 10 backward wing.csv")
twelvethirtyten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 30 backward wing 10 twist.csv")
twelvethirty= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms 30 backward wing.csv")
twelvebar= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms bar.csv")
twelvenw= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\12ms normal wing.csv")

ntwelvetenten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\Normalised data\12ms 10 backward wing 10 twist.csv")
ntwelvetennten = pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\Normalised data\12ms 10 backward wing 20 twist.csv")
ntwelveten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\Normalised data\12ms 10 backward wing.csv")
ntwelvethirtyten= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\Normalised data\12ms 30 backward wing 10 twist.csv")
ntwelvethirty= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\Normalised data\12ms 30 backward wing.csv")
ntwelvebar= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\Normalised data\12ms bar.csv")
ntwelvenw= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\Normalised data\12ms normal wing.csv")

fourteententen= pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\14ms 10 backward wing 10 twist.csv")
fourteentennten = pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\14ms 10 backward wing 20 twist.csv")
fourteenten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\14ms 10 backward wing.csv")
fourteenthirtyten=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\14ms 30 backward wing 10 twist.csv")
fourteenthirty=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\14ms 30 backward wing.csv")
fourteenbar=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\14ms bar.csv")
fourteennw=pd.read_csv(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\14ms normal wing.csv")
striptwelvetenten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep10twist.xlsx")
striptwelvetennten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep-10twist.xlsx")
striptwelveten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms10backward sweep0twist.xlsx")
striptwelvethirtyten=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30backward sweep10twist.xlsx")
striptwelvethirty=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\12ms30backward sweep0twist.xlsx")
striptwelvenw=pd.read_excel(r"C:\Users\44786\Documents\University of Bristol\dissertation\data\excel\ 12ms0sweep0twist.xlsx")
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
#speedsweeptwist


#plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.plot(twelveten['exb.Inc'], ntwelveten['Roll(Mx)'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Roll(Mx)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Roll(Mx)'], color='brown', label='-10° sweep -10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx) ')
#plt.title('Rolling Moment (Nm)  vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Roll(Mx)'], color='black', label='Symmetric wing')
plt.plot(twelveten['exb.Inc'], ntwelveten['Roll(Mx)'],linestyle=':' , label='-10° sweep ',color='red')
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Roll(Mx)'], color='cyan', label='-30° sweep')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Roll(Mx)'], color='black', label='Symmetric wing')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Roll(Mx)'], color='brown', label='-10° sweep -10° twist')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Roll(Mx)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Roll(Mx)'], color='blue', label='-30° sweep 10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()


'''plt.plot(tennw['exb.Inc'], tennw['Roll(Mx)'], label='tennw')
plt.plot(twelvenw['exb.Inc'], ntwelvenw['Roll(Mx)'], label='twelvenw')
plt.plot(fourteennw['exb.Inc'], fourteennw['Roll(Mx)'], label='fourteennw')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()'''


plt.plot(twelveten['exb.Inc'], ntwelveten['Pitch(My)'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Pitch(My)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Pitch(My)'], color='brown', label='-10° sweep -10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Pitching Moment (My)')
#plt.title('Pitching Moment (Nm) vs Angle of attack (α) (°)  at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Pitch(My)'], color='black', label='Symmetric wing')
plt.plot(twelveten['exb.Inc'], ntwelveten['Pitch(My)'],linestyle=':' , label='-10° sweep ',color='red')
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Pitch(My)'], color='cyan', label='-30° sweep ')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Pitching Moment (My)')
#plt.title('Pitch(Nm) vs Angle of attack (α) (°)  at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Pitch(My)'], color='black', label='Symmetric wing')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Pitch(My)'], color='brown', label='-10° sweep -10° twist')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Pitch(My)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Pitch(My)'], color='blue', label='-30° sweep 10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Pitching Moment (My)')
#plt.title('Pitching Moment (Nm) vs Angle of attack (α) (°)  at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

'''plt.plot(tennw['exb.Inc'], tennw['Pitch(My)'], label='tennw')
plt.plot(twelvenw['exb.Inc'], ntwelvenw['Pitch(My)'], label='twelvenw')
plt.plot(fourteennw['exb.Inc'], fourteennw['Pitch(My)'], label='fourteennw')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Pitching Moment (My)')
#plt.title('Pitching Moment (Nm) vs Angle of attack (α) (°)  at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()'''



plt.plot(twelveten['exb.Inc'], ntwelveten['Yaw(Mz)'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Yaw(Mz)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Yaw(Mz)'], color='brown', label='-10° sweep -10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Yawing Moment (Mz)')
#plt.title('Yawing Moment (Nm) vs Angle of attack (α) (°)  at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Yaw(Mz)'], color='black', label='Symmetric wing')
plt.plot(twelveten['exb.Inc'], ntwelveten['Yaw(Mz)'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Yaw(Mz)'], color='cyan', label='-30° sweep')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Yawing Moment (Mz)')
#plt.title('Yawing Moment (Nm) vs Angle of attack (α) (°)  at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Yaw(Mz)'], color='black', label='Symmetric wing')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Yaw(Mz)'], color='brown', label='-10° sweep -10° twist')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Yaw(Mz)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Yaw(Mz)'], color='blue', label='-30° sweep 10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Yawing Moment (Mz)')
#plt.title('Yaw(Nm) vs Angle of attack (α) (°)  at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

'''plt.plot(tennw['exb.Inc'], tennw['Yaw(Mz)'], label='tennw')
plt.plot(twelvenw['exb.Inc'], ntwelvenw['Yaw(Mz)'], label='twelvenw')
plt.plot(fourteennw['exb.Inc'], fourteennw['Yaw(Mz)'], label='fourteennw')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Yawing Moment (Mz)')
#plt.title('Yawing Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()'''


'''
plt.plot(twelveten['exb.Inc'], ntwelveten['Side(Fy)'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Side(Fy)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Side(Fy)'], color='brown', label='-10° sweep -10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Side Force (Fy)')
#plt.title('Side Force (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Side(Fy)'], color='black', label='Symmetric wing')
plt.plot(twelveten['exb.Inc'], ntwelveten['Side(Fy)'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Side(Fy)'], color='cyan', label='-30° sweep ')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Side Force (Fy)')
#plt.title('Side Force (N)vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Side(Fy)'], color='black', label='Symmetric wing')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Side(Fy)'], color='brown', label='-10° sweep -10° twist')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Side(Fy)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Side(Fy)'], color='blue', label='-30° sweep 10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Side Force (Fy)')
#plt.title('Side Force (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(tennw['exb.Inc'], tennw['Side(Fy)'], label='tennw')
plt.plot(twelvenw['exb.Inc'], ntwelvenw['Side(Fy)'], label='twelvenw')
plt.plot(fourteennw['exb.Inc'], fourteennw['Side(Fy)'], label='fourteennw')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Side Force (Fy)')
#plt.title('Side Force (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
'''


plt.plot(twelveten['exb.Inc'], ntwelveten['Drag(Fx)'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Drag(Fx)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Drag(Fx)'], color='brown', label='-10° sweep -10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Drag(Fx)')
#plt.title('Drag (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Drag(Fx)'], color='black', label='Symmetric wing')
plt.plot(twelveten['exb.Inc'], ntwelveten['Drag(Fx)'],linestyle=':' , label='-10° sweep ',color='red')
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Drag(Fx)'], color='cyan', label='-30° sweep ')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Drag(Fx)')
#plt.title('Drag (N)vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Drag(Fx)'], color='black', label='Symmetric wing')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Drag(Fx)'], color='brown', label='-10° sweep -10° twist')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Drag(Fx)'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Drag(Fx)'], color='blue', label='-30° sweep 10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Drag(Fx)')
#plt.title('Drag (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

'''plt.plot(tennw['exb.Inc'], tennw['Drag(Fx)'], label='tennw')
plt.plot(twelvenw['exb.Inc'], ntwelvenw['Drag(Fx)'], label='twelvenw')
plt.plot(fourteennw['exb.Inc'], fourteennw['Drag(Fx)'], label='fourteennw')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Drag(Fx)')
#plt.title('Drag (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
'''



plt.plot(twelvenw['exb.Inc'], ntwelvenw['Roll(Mx)'], color='black', label='Symmetric wing')
plt.plot(striptwelvenw['exb.Inc'], striptwelvenw['Roll(Mx)'], color='black', label='Symmetric wing strip' ,linestyle='--' )
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Roll(Mx)'], color='brown', label='-10° sweep -10° twist')
plt.plot(striptwelvetennten['exb.Inc'], striptwelvetennten['Roll(Mx)'], color='brown', label='-10° sweep -10° twist strip' ,linestyle='--' )
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Roll(Mx)'], color='orange', label='-10° sweep 10° twist')
plt.plot(striptwelvetenten['exb.Inc'], striptwelvetenten['Roll(Mx)'], color='orange', label='-10° sweep 10° twist strip' ,linestyle='--' )
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Roll(Mx)'], color='blue', label='-30° sweep 10° twist')
plt.plot(striptwelvethirtyten['exb.Inc'], striptwelvethirtyten['Roll(Mx)'], color='blue', label='-30° sweep 10° twist strip' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend(loc='upper right', prop={'size': 8})

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Roll(Mx)'], color='black', label='Symmetric wing')
plt.plot(striptwelvenw['exb.Inc'], striptwelvenw['Roll(Mx)'], color='black', label='Symmetric wing strip' ,linestyle='--' )
plt.plot(twelveten['exb.Inc'], ntwelveten['Roll(Mx)'],linestyle=':' , label='-10° sweep ',color='red')
plt.plot(striptwelveten['exb.Inc'], striptwelveten['Roll(Mx)'], label='-10° sweep strip' ,color='red',linestyle='--' )
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Roll(Mx)'], color='cyan', label='-30° sweep')
plt.plot(striptwelvethirty['exb.Inc'], striptwelvethirty['Roll(Mx)'], color='cyan', label='-30° sweep strip' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend(loc='upper right', prop={'size': 8})

# Show the plot
plt.show()
#remember to plot how the 3 models fared against each other

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Roll(Mx)'], color='black', label='Symmetric wing')
plt.plot( flowtwelvenw['Alpha'],  flowtwelvenw['L_(N.m)'], color='black', label='Symmetric wing  Flow5' ,linestyle='--' )
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Roll(Mx)'], color='brown', label='-10° sweep -10° twist')
plt.plot( flowtwelvetennten['Alpha'],  flowtwelvetennten['L_(N.m)'], color='brown', label='-10° sweep -10° twist  Flow5' ,linestyle='--' )
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Roll(Mx)'], color='orange', label='-10° sweep 10° twist')
plt.plot( flowtwelvetenten['Alpha'],  flowtwelvetenten['L_(N.m)'], color='orange', label='-10° sweep 10° twist  Flow5' ,linestyle='--' )
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Roll(Mx)'], color='blue', label='-30° sweep 10° twist')
plt.plot( flowtwelvethirtyten['Alpha'],  flowtwelvethirtyten['L_(N.m)'], color='blue', label='-30° sweep 10° twist  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend(loc='upper right', prop={'size': 8})

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Roll(Mx)'], color='black', label='Symmetric wing')
plt.plot( flowtwelvenw['Alpha'],  flowtwelvenw['L_(N.m)'], color='black', label='Symmetric wing  Flow5' ,linestyle='--' )
plt.plot(twelveten['exb.Inc'], ntwelveten['Roll(Mx)'], linestyle=':' , label='-10° sweep ',color='red')
plt.plot( flowtwelveten['Alpha'],  flowtwelveten['L_(N.m)'],  color='red', label='-10° sweep  Flow5' ,linestyle='--' )
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Roll(Mx)'], color='cyan', label='-30° sweep')
plt.plot( flowtwelvethirty['Alpha'],  flowtwelvethirty['L_(N.m)'], color='cyan', label='-30° sweep  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Rolling Moment (Mx)')
#plt.title('Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend(loc='upper right', prop={'size': 8})

# Show the plot
plt.show()
#remember to plot how the 3 models fared against each other




plt.plot(twelveten['exb.Inc'], ntwelveten['C_D'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['C_D'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['C_D'], color='brown', label='-10° sweep -10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel( '$C_D$')
#plt.title('Drag (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['C_D'], color='black', label='Symmetric wing')
plt.plot(twelveten['exb.Inc'], ntwelveten['C_D'],linestyle=':' , label='-10° sweep ',color='red')
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['C_D'], color='cyan', label='-30° sweep ')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel( '$C_D$')
#plt.title('Drag (N)vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()


plt.plot(twelveten['exb.Inc'], ntwelveten['C_L'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['C_L'], color='orange', label='-10° sweep 10° twist')
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['C_L'], color='brown', label='-10° sweep -10° twist')
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel( '$C_L$')
#plt.title('Drag (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['C_L'], color='black', label='Symmetric wing')
plt.plot(twelveten['exb.Inc'], ntwelveten['C_L'],linestyle=':' , label='-10° sweep ',color='red')
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['C_L'], color='cyan', label='-30° sweep ')

# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel( '$C_L$')
#plt.title('Drag (N)vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()









plt.plot(twelveten['exb.Inc'], ntwelveten['C_D'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot( flowtwelveten['Alpha'],  flowtwelveten['CD'],  color='red', label='-10° sweep  Flow5' ,linestyle='--' )
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['C_D'], color='orange', label='-10° sweep 10° twist')
plt.plot( flowtwelvetenten['Alpha'],  flowtwelvetenten['CD'], color='orange', label='-10° sweep 10° twist  Flow5' ,linestyle='--' )
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['C_D'], color='brown', label='-10° sweep -10° twist')
plt.plot( flowtwelvetennten['Alpha'],  flowtwelvetennten['CD'], color='brown', label='-10° sweep -10° twist  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel( '$C_D$')
#plt.title('Drag (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['C_D'], color='black', label='Symmetric wing')
plt.plot( flowtwelvenw['Alpha'],  flowtwelvenw['CD'], color='black', label='Symmetric wing  Flow5' ,linestyle='--' )
plt.plot(twelveten['exb.Inc'], ntwelveten['C_D'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot( flowtwelveten['Alpha'],  flowtwelveten['CD'],  color='red', label='-10° sweep  Flow5' ,linestyle='--' )
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['C_D'], color='cyan', label='-30° sweep ')
plt.plot( flowtwelvethirty['Alpha'],  flowtwelvethirty['CD'], color='cyan', label='-30° sweep  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel( '$C_D$')
#plt.title('Drag (N)vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()


plt.plot(twelveten['exb.Inc'], ntwelveten['C_L'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot( flowtwelveten['Alpha'],  flowtwelveten['CL'],  color='red', label='-10° sweep  Flow5' ,linestyle='--' )
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['C_L'], color='orange', label='-10° sweep 10° twist')
plt.plot( flowtwelvetenten['Alpha'],  flowtwelvetenten['CL'], color='orange', label='-10° sweep 10° twist  Flow5' ,linestyle='--' )
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['C_L'], color='brown', label='-10° sweep -10° twist')
plt.plot( flowtwelvetennten['Alpha'],  flowtwelvetennten['CL'], color='brown', label='-10° sweep -10° twist  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel( '$C_L$')
#plt.title('Drag (N) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['C_L'], color='black', label='Symmetric wing')
plt.plot( flowtwelvenw['Alpha'],  flowtwelvenw['CL'], color='black', label='Symmetric wing  Flow5' ,linestyle='--' )
plt.plot(twelveten['exb.Inc'], ntwelveten['C_L'],linestyle=':' , label='-10° sweep ',color='red')
plt.plot( flowtwelveten['Alpha'],  flowtwelveten['CL'],  color='red', label='-10° sweep  Flow5' ,linestyle='--' )
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['C_L'], color='cyan', label='-30° sweep ')
plt.plot( flowtwelvethirty['Alpha'],  flowtwelvethirty['CL'], color='cyan', label='-30° sweep  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel( '$C_L$')
#plt.title('Drag (N)vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()


plt.plot(twelvenw['exb.Inc'], ntwelvenw['Pitch(My)'], color='black', label='Symmetric wing')
plt.plot( flowtwelvenw['Alpha'],  flowtwelvenw['M_(N.m)'], color='black', label='Symmetric wing  Flow5' ,linestyle='--' )
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Pitch(My)'], color='brown', label='-10° sweep -10° twist')
plt.plot( flowtwelvetennten['Alpha'],  flowtwelvetennten['M_(N.m)'], color='brown', label='-10° sweep -10° twist  Flow5' ,linestyle='--' )
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Pitch(My)'], color='orange', label='-10° sweep 10° twist')
plt.plot( flowtwelvetenten['Alpha'],  flowtwelvetenten['M_(N.m)'], color='orange', label='-10° sweep 10° twist  Flow5' ,linestyle='--' )
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Pitch(My)'], color='blue', label='-30° sweep 10° twist')
plt.plot( flowtwelvethirtyten['Alpha'],  flowtwelvethirtyten['M_(N.m)'], color='blue', label='-30° sweep 10° twist  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Pitching Moment (My)')
#plt.title('Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend(loc='upper right', prop={'size': 8})

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Pitch(My)'], color='black', label='Symmetric wing')
plt.plot( flowtwelvenw['Alpha'],  flowtwelvenw['M_(N.m)'], color='black', label='Symmetric wing  Flow5' ,linestyle='--' )
plt.plot(twelveten['exb.Inc'], ntwelveten['Pitch(My)'], linestyle=':' ,label='-10° sweep ',color='red')
plt.plot( flowtwelveten['Alpha'],  flowtwelveten['M_(N.m)'],  color='red', label='-10° sweep  Flow5' ,linestyle='--' )
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Pitch(My)'], color='cyan', label='-30° sweep')
plt.plot( flowtwelvethirty['Alpha'],  flowtwelvethirty['M_(N.m)'], color='cyan', label='-30° sweep  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Pitching Moment (My)')
#plt.title('Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend(loc='upper right', prop={'size': 8})

# Show the plot
plt.show()
#remember to plot how the 3 models fared against each other

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Yaw(Mz)'], color='black', label='Symmetric wing')
plt.plot( flowtwelvenw['Alpha'],  flowtwelvenw['N_(N.m)'], color='black', label='Symmetric wing  Flow5' ,linestyle='--' )
plt.plot(twelvetennten['exb.Inc'], ntwelvetennten['Yaw(Mz)'], color='brown', label='-10° sweep -10° twist')
plt.plot( flowtwelvetennten['Alpha'],  flowtwelvetennten['N_(N.m)'], color='brown', label='-10° sweep -10° twist  Flow5' ,linestyle='--' )
plt.plot(twelvetenten['exb.Inc'], ntwelvetenten['Yaw(Mz)'], color='orange', label='-10° sweep 10° twist')
plt.plot( flowtwelvetenten['Alpha'],  flowtwelvetenten['N_(N.m)'], color='orange', label='-10° sweep 10° twist  Flow5' ,linestyle='--' )
plt.plot(twelvethirtyten['exb.Inc'], ntwelvethirtyten['Yaw(Mz)'], color='blue', label='-30° sweep 10° twist')
plt.plot( flowtwelvethirtyten['Alpha'],  flowtwelvethirtyten['N_(N.m)'], color='blue', label='-30° sweep 10° twist  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel(' Angle of attack (α) (°)')
plt.ylabel('Yawing Moment (Mz)')
#plt.title('Rolling Moment (Nm) vs Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend(loc='upper right', prop={'size': 8})

# Show the plot
plt.show()

plt.plot(twelvenw['exb.Inc'], ntwelvenw['Yaw(Mz)'], color='black', label='Symmetric wing')
plt.plot( flowtwelvenw['Alpha'],  flowtwelvenw['N_(N.m)'], color='black', label='Symmetric wing  Flow5' ,linestyle='--' )
plt.plot(twelveten['exb.Inc'], ntwelveten['Yaw(Mz)'],linestyle=':' , label='-10° sweep ',color='red')
plt.plot( flowtwelveten['Alpha'],  flowtwelveten['N_(N.m)'],  color='red', label='-10° sweep  Flow5' ,linestyle='--' )
plt.plot(twelvethirty['exb.Inc'], ntwelvethirty['Yaw(Mz)'], color='cyan', label='-30° sweep')
plt.plot( flowtwelvethirty['Alpha'],  flowtwelvethirty['N_(N.m)'], color='cyan', label='-30° sweep  Flow5' ,linestyle='--' )
# ... (add plots for other DataFrames)

# Customize the plot
plt.xlabel('Angle of attack (α) (°)')
plt.ylabel('Yawing Moment (Mz)')
#plt.title('Rolling Moment (Nm) vs  Angle of attack (°) at 12m/s')
plt.grid(True)
plt.legend(loc='upper right', prop={'size': 8})

# Show the plot
plt.show()
#remember to plot how the 3 models fared against each other