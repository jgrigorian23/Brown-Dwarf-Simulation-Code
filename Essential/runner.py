import main01
import csv
alphas=["0.4", "0.5", "0.6", "0.7", "0.8"]
b=["const", "inside_out", "late_burst"]
model_lst=["saumonmarley2008", "sonora", "baraffe"]
ticker=0
for mod in model_lst:
    for i in alphas:
        for b_string in b:
            n=2000000
            m=1000000
            masses, ages, temps, drops = main01.main(mod, i,b_string, n, m)
            s1=mod+"_"+i+"_"+b_string
            string="/Users/yadukrishnaraghu/Files/Research/Brown-Dwarf-Simulation-Code-main/Essential-Simulation-Files/Bin/"+s1
            string1=string+"_1.txt"
            string2=string+"_2.txt"
            string3=string+"_3.txt"
            with open("/Users/yadukrishnaraghu/Files/Research/Brown-Dwarf-Simulation-Code-main/Essential-Simulation-Files/Bin/drops.txt", 'a') as employee_file:
                    writer=csv.writer(employee_file)
                    writer.writerow([s1]+drops)

            with open(string1, 'w') as employee_file:
                writer=csv.writer(employee_file)
                for j in list(range(m)):
                    writer.writerow([masses[0][j],  ages[0][j], temps[0][j]])
            with open(string2, 'w') as employee_file:
                writer=csv.writer(employee_file)
                for j in list(range(m)):
                    writer.writerow([masses[1][j], ages[1][j], temps[1][j]])
            with open(string3, 'w') as employee_file:
                writer=csv.writer(employee_file)
                for j in list(range(m)):
                    writer.writerow([masses[2][j], ages[2][j], temps[2][j]])
            ticker+=1
            print(str(ticker) + " done "+ string)