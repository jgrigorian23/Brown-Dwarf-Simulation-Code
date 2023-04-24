import math
import random

#INTERPOLATION

def b_int(x1, x2, y1, y2, f1, f2, f3, f4, x, y):
    return ((f1*(x2-x)*(y2-y))+(f3*(x-x1)*(y2-y))+(f2*(x2-x)*(y-y1))+(f4*(x-x1)*(y-y1)))/((x2-x1)*(y2-y1))

def bmain(ax, my, age, masses, temps):
    final=[]
    sm=sorted(masses)
    ref_lst=list(zip(age, masses, temps))
    sample_lst=list(zip(ax, my))
    nsl=[]
    for i in sample_lst:
        if i[1]<sm[-1]:
            nsl.append(i)
    sample_lst=nsl
    split_mass_lst=[]

    for i in ref_lst:
        b = False
        for j in split_mass_lst:
            if j[0]==i[1]:
                j[1].append(i)
                b=True
        if not b:
            split_mass_lst.append((i[1], [i]))


    split_mass_lst.sort(key = lambda tuple: tuple[0])
    split_mass_lst[0][1].sort(key= lambda tuple: tuple[0])
    split_mass_lst[1][1].sort(key=lambda tuple: tuple[0])
    l=len(split_mass_lst)
    for i in list(range(l)):

        if not i==len(split_mass_lst)-1:
            if i < len(split_mass_lst)-2:
                split_mass_lst[i+2][1].sort(key=lambda tuple: tuple[0])


            min_m = split_mass_lst[i][0]
            max_m = split_mass_lst[i+1][0]
            bot=[k for k in split_mass_lst[i][1]]
            top=[k for k in split_mass_lst[i+1][1]]
            loc_tuple=[]
            new_sample=[]
            for k in sample_lst:
                if min_m<k[1]<max_m:
                    loc_tuple.append(k)
                else:
                    new_sample.append(k)
            sample_lst=new_sample
            if bot[0][0]<top[0][0]:
                while not bot[0][0]==top[0][0]:
                    bot.pop(0)

            if top[0][0]<bot[0][0]:
                while not bot[0][0]==top[0][0]:
                    top.pop(0)
            if bot[-1][0]>top[-1][0]:
                while not bot[-1][0]==top[-1][0]:
                    bot.pop(-1)
            if top[-1][0]>bot[-1][0]:
                while not bot[-1][0]==top[-1][0]:
                    top.pop(-1)
            for j in list(range(len(bot))):
                if not j==len(bot)-1:
                    p11=bot[j]
                    p21=bot[j+1]
                    p12=top[j]
                    p22=top[j+1]
                    bound_lst=[]
                    new_loc=[]
                    for k in loc_tuple:
                        if p11[0]<k[0]<p21[0]:
                            bound_lst.append(k)
                        else:
                            new_loc.append(k)

                    loc_tuple=new_loc
                    for k in bound_lst:
                        final.append((k[0], k[1], b_int(p11[0], p21[0], p11[1], p12[1], p11[2],p12[2],p21[2],p22[2], k[0], k[1])))
            sample_lst=sample_lst+loc_tuple
    return final

#MASS FETCH

def mass_f(x, m1, m2, alpha):
    if alpha == 1:
        return math.exp((x*(math.log(m2/m1)))+math.log(m1))
    else:
        return ((x*(((m2)**(1-alpha))-((m1)**(1-alpha))))+((m1)**(1-alpha)))**(1/(1-alpha))

def inverse_power(alpha, n):
    m1_a=0.01
    m1_b=0.005
    m1_c=0.001
    m2=0.1
    lst_1=[mass_f(random.random(), m1_a, m2, alpha) for _ in list(range(n))]
    lst_2=[mass_f(random.random(), m1_b, m2, alpha) for _ in list(range(n))]
    lst_3=[mass_f(random.random(), m1_c, m2, alpha) for _ in list(range(n))]
    return [lst_1, lst_2, lst_3]

#AGE FETCH

def constf(x, a1, a2):
    return ((a2-a1)*x)+a1

def const_time_inverse_cdf(n):
    a1=0
    a2=10

    lst=[constf(random.random(), a1, a2) for _ in list(range(n))]

    return lst

def ins_f(x, m, b):
    alpha=(50*m)+(10*b)
    return -(b/m)+math.sqrt(((b/m)**2)+((2*alpha*x)/m))

def inside_out_time_inverse(n):


    lst1=[ins_f(random.random(), 0.03, 0.36) for _ in list(range(n))]
    return lst1

def late_burst_inverse(n):
    t3=2.65
    t4=5.1
    top = round(n*(1.7395/6.8395))
    bottom = round(n*(5.1/6.8395))

    lst1=[ins_f(random.random(), 0.03, 0.36) for _ in list(range(bottom))]
    lst2=[constf(random.random(), t3, t4) for _ in list(range(top))]
    lst=lst1+lst2
    random.shuffle(lst)
    return lst

def late_const_time_inverse_cdf(n):
    t1=8
    t2=10

    lst=[constf(random.random(), t1, t2) for _ in list(range(n))]

    return lst

#MODEL FETCH

def get_sonora():
    file=open("nc+0.0_co1.0_age.txt")
    ages=[]
    masses=[]
    temperatures=[]
    lines=file.readlines()
    for i in list(range(len(lines))):
        masses.append(float(lines[i].split()[1]))
        ages.append(float(lines[i].split()[0]))
        temperatures.append(float(lines[i].split()[3]))
    return ages, masses, temperatures

def get_2008():
    file=open("sm_hybrid_age.txt")
    ages=[]
    masses=[]
    temperatures=[]
    lines=file.readlines()
    for i in list(range(len(lines))):
        ages.append(float(lines[i].split()[0]))
        masses.append(float(lines[i].split()[1]))
        temperatures.append(float(lines[i].split()[3]))
    return ages, masses, temperatures

def get_baraffe():
    file=open("baraffe.txt")
    ages=[]
    masses=[]
    temperatures=[]
    switch_lst=[]
    read=file.readlines()
    for i in list(range(len(read))):
        if ' ' not in read[i]:
            switch_lst.append(i)
    q=0
    for i in list(range(len(read))):
        if ' ' in read[i]:
            if not len(switch_lst)==q+1:
                if switch_lst[q+1]<i:
                    q+=1
            ages.append(float(read[switch_lst[q]]))
            masses.append(float(read[i].split()[0]))
            temperatures.append(float(read[i].split()[1]))
    return ages, masses, temperatures

class Star:
    def __init__(self, age, mass, temp):
        self.age = age
        self.mass = mass
        self.temperature = temp

    def __repr__(self):
        return "This is a star that is " + str(self.age) + " Gigayears, with a mass of " + str(
            self.mass) + " solar masses, and is " + str(self.temperature) +" Kelvin."

    def get_age(self):
        return self.age

    def get_mass(self):
        return self.mass

    def get_temperature(self):
        return self.temperature

    def set_age(self, new_age):
        self.age = new_age

    def set_mass(self, new_mass):
        self.mass = new_mass

    def set_temperature(self, new_temperature):
        self.temperature = new_temperature

def main(model_string, alpha, time, n, m):
    if model_string=='sonora':
        reference_ages,reference_masses, reference_temperatures=get_sonora()
    elif model_string=="saumonmarley2008":
        reference_ages, reference_masses, reference_temperatures=get_2008()
    elif model_string=='baraffe':
        reference_ages, reference_masses, reference_temperatures=get_baraffe()




    sampled_masses=inverse_power(float(alpha), n)

    if time=="const":
        sampled_ages = const_time_inverse_cdf(n)
    elif time=="late_const":
        sampled_ages = late_const_time_inverse_cdf(n)
    elif time=="inside_out":
        sampled_ages = inside_out_time_inverse(n)
    elif time=="late_burst":
        sampled_ages = late_burst_inverse(n)
    drops=[0,0,0]
    ml, al, tl = [[], [], []], [[], [], []], [[], [], []]

    for j in list(range(3)):
        the_ages=sampled_ages
        the_masses=sampled_masses[j]
        tuples=bmain(the_ages, the_masses, reference_ages, reference_masses, reference_temperatures)
        sampled_stars=[Star(i[0], i[1], i[2]) for i in tuples]
        random.shuffle(sampled_stars)
        for i in sampled_stars:
            ml[j].append(i.get_mass())
        ml[j]=ml[j][:m]
        for i in sampled_stars:
            al[j].append(i.get_age())
        al[j] = al[j][:m]
        for i in sampled_stars:
            tl[j].append(i.get_temperature())
        tl[j] = tl[j][:m]
        drops[j]= n-len(sampled_stars)

    return ml, al, tl, drops
