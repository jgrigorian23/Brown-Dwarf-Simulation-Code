import main1
import csv
alphas=["0.4", "0.5", "0.6"]
b=["const", "inside_out", "late_burst"]
ticker=0
for i in alphas:
    for b_string in b:
        n=1500000
        m=1000000
        model_string = "sonora"
        masses, ages, temps, drops = main1.main(model_string, i,b_string, n, m)
        string=model_string+"_"+i+"_"+b_string
        string1=string+"_1.txt"
        string2=string+"_2.txt"
        string3=string+"_3.txt"
        with open("drops.txt", 'a') as employee_file:
                writer=csv.writer(employee_file)
                writer.writerow([string]+drops)

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