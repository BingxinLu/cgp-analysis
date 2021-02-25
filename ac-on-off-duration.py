import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
sns.set(color_codes=True)

energy = pd.read_csv('energydata.csv',delimiter = ',')
energy['DateTime'] = pd.to_datetime(energy['DateTime'], format = '%Y-%m-%d %H:%M:%S')
energy.index = energy['DateTime']

off = energy[energy['coolnomix'] == 'off']
on = energy[energy['coolnomix'] == 'on']

day_off = []
import datetime

for j in range(31):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 1, j+1)]
    c1_day = energy_day['c1']
    count = 0
    for k in range(len(c1_day)-1):
        if c1_day.iloc[k] != c1_day.iloc[k+1]:
            lst_off.append(count)
            count = 0
        else:
            count+=1
    day_off.append(np.mean(lst_off))
    
for j in range(29):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 2, j+1)]
    c1_day = energy_day['c1']
    count = 0
    for k in range(len(c1_day)-1):
        if c1_day.iloc[k] != c1_day.iloc[k+1]:
            lst_off.append(count)
            count = 0
        else:
            count+=1
    day_off.append(np.mean(lst_off))
    
for j in range(12):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 3, j+1)]
    c1_day = energy_day['c1']
    count = 0
    for k in range(len(c1_day)-1):
        if c1_day.iloc[k] != c1_day.iloc[k+1]:
            lst_off.append(count)
            count = 0
        else:
            count+=1
    day_off.append(np.mean(lst_off))

day_off = pd.DataFrame(day_off)
date = pd.date_range('1/1/2020','3/12/2020')
day_off['dt'] = date

on_index = [2,4,6,8,12,14,16,18,20,22,25,27,29,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,63,64,66,68,70,72]

day_off['mode'] = 'on'
for i in range(len(day_off)):
    if (i+1) in on_index:
        day_off.iloc[i, 2] = 'on' 
    else:
        day_off.iloc[i, 2] = 'off' 

on_c1 = day_off[day_off['mode'] == 'on']
on_c1.index = on_c1['dt']
off_c1 = day_off[day_off['mode'] == 'off']
off_c1.index = off_c1['dt']

fig, axes = plt.subplots(figsize=(8,4))
plt.plot(on_c1['dt'],on_c1[0], color='blue', linewidth=1.0, linestyle='-', label='on')
plt.plot(off_c1['dt'],off_c1[0], color='red', linewidth=1.0, linestyle='-', label='off')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.title('Compressor1 Duration')
plt.xlabel('date')
plt.ylabel('duration (seconds)')
plt.legend()
plt.savefig('c1.png')

#------------------------------------------------------------------


day_off2 = []

for j in range(31):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 1, j+1)]
    c2_day = energy_day['c2']
    count = 0
    for k in range(len(c2_day)-1):
        if c2_day.iloc[k] != c2_day.iloc[k+1]:
            lst_off.append(count)
            count = 0
        else:
            count+=1
    day_off2.append(np.mean(lst_off))
    
for j in range(29):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 2, j+1)]
    c2_day = energy_day['c2']
    count = 0
    for k in range(len(c2_day)-1):
        if c2_day.iloc[k] != c2_day.iloc[k+1]:
            lst_off.append(count)
            count = 0
        else:
            count+=1
    day_off2.append(np.mean(lst_off))
    
for j in range(12):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 3, j+1)]
    c2_day = energy_day['c2']
    count = 0
    for k in range(len(c2_day)-1):
        if c2_day.iloc[k] != c2_day.iloc[k+1]:
            lst_off.append(count)
            count = 0
        else:
            count+=1
    day_off2.append(np.mean(lst_off))
    
day_off2 = pd.DataFrame(day_off2)
day_off2['dt'] = date

day_off2['mode'] = 'on'
for i in range(len(day_off2)):
    if (i+1) in on_index:
        day_off2.iloc[i, 2] = 'on' 
    else:
        day_off2.iloc[i, 2] = 'off' 

on_c2 = day_off2[day_off2['mode'] == 'on']
on_c2.index = on_c2['dt']
off_c2 = day_off2[day_off2['mode'] == 'off']
off_c2.index = off_c2['dt']

fig, axes = plt.subplots(figsize=(8,4))
plt.plot(on_c2['dt'],on_c2[0], color='green', linewidth=1.0, linestyle='-', label='on')
plt.plot(off_c2['dt'],off_c2[0], color='red', linewidth=1.0, linestyle='-', label='off')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.title('Compressor2 Duration')
plt.xlabel('date')
plt.ylabel('duration (seconds)')
plt.legend()
plt.savefig('c2.png')



#-------------------------------------------------------------------

day_off3 = []

for j in range(31):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 1, j+1)]
    fan_day = energy_day['f']
    count = 1
    for k in range(len(fan_day)-1):
        if fan_day.iloc[k] != fan_day.iloc[k+1]:
            lst_off.append(count)
            count = 1
        else:
            count+=1
    day_off3.append(np.mean(lst_off))
    
for j in range(29):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 2, j+1)]
    fan_day = energy_day['f']
    count = 1
    for k in range(len(fan_day)-1):
        if fan_day.iloc[k] != fan_day.iloc[k+1]:
            lst_off.append(count)
            count = 1
        else:
            count+=1
    day_off3.append(np.mean(lst_off))
    
for j in range(12):
    lst_off = []
    energy_day = energy[energy.index.date == datetime.date(2020, 3, j+1)]
    fan_day = energy_day['f']
    count = 1
    for k in range(len(fan_day)-1):
        if fan_day.iloc[k] != fan_day.iloc[k+1]:
            lst_off.append(count)
            count = 1
        else:
            count+=1
    day_off3.append(np.mean(lst_off))
    
day_off3 = pd.DataFrame(day_off3)
day_off3['dt'] = date

day_off3['mode'] = 'on'
for i in range(len(day_off3)):
    if (i+1) in on_index:
        day_off3.iloc[i, 2] = 'on' 
    else:
        day_off3.iloc[i, 2] = 'off' 

on_f = day_off3[day_off3['mode'] == 'on']
on_f.index = on_f['dt']
off_f = day_off3[day_off3['mode'] == 'off']
off_f.index = off_f['dt']

fig, axes = plt.subplots(figsize=(8,4))
plt.plot(on_f['dt'],on_f[0], color='blue', linewidth=1.0, linestyle='-', label='on')
plt.plot(off_f['dt'],off_f[0], color='orange', linewidth=1.0, linestyle='-', label='off')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.title('Fan Duration')
plt.xlabel('date')
plt.ylabel('duration (seconds)')
plt.legend()
plt.savefig('f.png')

    
            
            
            
        












