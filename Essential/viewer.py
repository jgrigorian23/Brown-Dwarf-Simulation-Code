from matplotlib import pyplot as plt
import csv


colors=['b', 'g', 'r']
data=[[], [], []]
j=2
if j==0:
    stringy="Mass (Solar)"
    bins=[90, 95, 99]
if j==1:
    stringy="Age (GYR)"
    bins=[100, 100, 100]
if j==2:
    stringy="Temperature (Kelvin)"
    bins=[list(range(0, 2550, 150))+[2550], list(range(0, 2550, 150))+[2550], list(range(0, 2550, 150))+[2550]]
i="0.5"
model_string= "saumonmarley2008"
birthrate= "const"
s1=model_string+"_"+i+"_"+birthrate
string="/Users/yadukrishnaraghu/Files/Research/Brown-Dwarf-Simulation-Code-main/Essential-Simulation-Files/Bin/"+s1
string1=string+"_1.txt"
string2=string+"_2.txt"
string3=string+"_3.txt"
with open(string1, mode='r') as employee_file:
    read = csv.reader(employee_file)
    for i in read:
        data[0].append(float(i[j]))

with open(string2, mode='r') as employee_file:
    read = csv.reader(employee_file)
    for i in read:
         data[1].append(float(i[j]))

with open(string3, mode='r') as employee_file:
    read = csv.reader(employee_file)
    for i in read:
        data[2].append(float(i[j]))




plt.hist(data[0], histtype='step', bins=bins[0], color="black")
plt.hist(data[1], histtype='step', bins=bins[1], color="blue")
plt.hist(data[2], histtype='step', bins=bins[2], color="red")
plt.grid()
plt.xlabel(stringy)
plt.ylabel('Number')
plt.gca().invert_xaxis()
plt.title(s1)

plt.show()