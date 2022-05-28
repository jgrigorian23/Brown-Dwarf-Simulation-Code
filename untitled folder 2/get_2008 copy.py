from matplotlib import pyplot as plt

def main():
    file=open("sm_hybrid_age (1).txt")
    ages=[]
    masses=[]
    temperatures=[]
    lines=file.readlines()
    for i in list(range(len(lines))):
        ages.append(float(lines[i].split()[0]))
        masses.append(float(lines[i].split()[1]))
        temperatures.append(float(lines[i].split()[3]))
    return ages, masses, temperatures
plt.scatter(main()[0],main()[1], s=10)
plt.xlabel("Age")
plt.ylabel("Mass")

plt.title("Saumon & Marley 2008")
plt.show()