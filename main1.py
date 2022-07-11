import math
import random
import decimal

def nums(start, stop, num):
    start=decimal.Decimal(str(start))
    stop = decimal.Decimal(str(stop))
    num=decimal.Decimal(str(num))

    num_range=stop-start
    width=num_range/num
    count=0
    lst=[]
    while count<num_range:
        lst.append(float(start))
        start+=width
        count+=width
    return lst
#INTERPOLATION

def b_int(x1, x2, y1, y2, f1, f2, f3, f4, x, y):
    return ((f1*(x2-x)*(y2-y))+(f3*(x-x1)*(y2-y))+(f2*(x2-x)*(y-y1))+(f4*(x-x1)*(y-y1)))/((x2-x1)*(y2-y1))
def l_int(x,p1, p2):
    x1,x2,t1,t2=p1[0],p2[0],p1[1],p2[1]
    m=(t2-t1)/(x2-x1)
    b=t1-(m*x1)
    return (m*x)+b
def find(a1, a2, m1, m2, points):
    lower_age, upper_age=[], []
    p1, p2, p3, p4=[-1,-1, -1],[-1,-1, -1],[-1,-1, -1],[-1,-1, -1]
    for i in points:
        if i[0] == a1:
            lower_age.append(i)
    for i in points:
        if i[0] == a2:
            upper_age.append(i)
    q1,q2,q3,q4=0,0,0,0
    for i in lower_age:
        if i[1]==m1:
            p1=i
            q1+=1
        if i[1]==m2:
            p2=i
            q2+=1
    for i in upper_age:
        if i[1]==m1:
            p3=i
            q3+=1
        if i[1]==m2:
            p4=i
            q4+=1
    if not q1==q2==q3==q4==1:
        return -1,-1,-1,-1
    if not p1[0]==p2[0]:
        return -1,-1,-1,-1
    if not p3[0]==p4[0]:
        return -1,-1,-1,-1
    if not p1[1]==p3[1]:
        return -1,-1,-1,-1
    if not p2[1]==p4[1]:
        return -1,-1,-1,-1
    if not (p1==0 or p2==0 or p3==0 or p4==0):
        return p1, p2, p3, p4
    return -1,-1,-1,-1

def get_points(age, masses, x, y, points):
        age_lower, age_upper, mass_lower, mass_upper = 0, 11, 0, 0.1
        for i in age:
            if age_lower < i < x:
                age_lower=i
            if x < i < age_upper:
                age_upper=i
        for i in masses:
            if mass_lower < i < y:
                mass_lower=i
            if y < i < mass_upper:
                mass_upper=i

        p1, p2, p3, p4=find(age_lower, age_upper, mass_lower, mass_upper, points)
        return p1, p2, p3, p4

def bmain(ax, my, age, masses, temps):
    the_lst=[]
    for i in list(range(len(ax))):
        x=ax[i]
        y=my[i]
        bool1, bool2, bool3 = False, False, False
        if x>10 or y<0.0005 or x<0.001 or y>0.9:
            temp= -1
        points=[(age[i], masses[i], temps[i]) for i in list(range(len(age)))]



        for i in points:
            if i[0]==x:
                bool1=True

            if i[1]==y:
                bool2=True
        if bool1 and bool2:
                for i in points:
                    if i[0]==x and i[1]==y:
                        bool3=True
                        temp=i[2]
        if not bool3:
            age_lower, age_upper, mass_lower, mass_upper = 0, 11, 0, 0.1
            if bool1:
                two_points=[]
                for i in masses:
                    if mass_lower < i < y:
                        mass_lower=i
                    if y < i < mass_upper:
                        mass_upper=i
                list_check=[]
                check1 = 0
                check2 = 0
                for i in points:
                    if i[0]==x:
                        list_check.append(i)
                for i in list_check:
                    if i[0]>x:
                        check1+=1
                    if i[0]<x:
                        check2+=1
                if check1==0 or check2==0:
                    temp= -1
                for i in points:
                    if ((i[0]==x and i[1]==mass_lower)or(i[0]==x and i[1]==mass_upper)) :
                        two_points.append(i)

                temp=l_int(y, two_points[0], two_points[1])
            if bool2:
                two_points=[]
                for i in age:
                    if age_lower < i < x:
                        age_lower=i
                    if x < i < age_upper:
                        age_upper=i
                list_check=[]
                check1 = 0
                check2 = 0
                for i in points:
                    if i[1]==y:
                        list_check.append(i)
                for i in list_check:
                    if i[1]>y:
                        check1+=1
                    if i[1]<y:
                        check2+=1
                if check1==0 or check2==0:
                    temp= -1
                for i in points:
                    if ((i[1]==y and i[0]==age_lower)or(i[1]==y and i[0]==age_upper)) :
                        two_points.append(i)
                temp=l_int(y, two_points[0], two_points[1])
            else:
                p1, p2, p3, p4 = get_points(age, masses, x, y, points)
                if p1 == -1 or p2 == -1 or p3 == -1 or p4 == -1:
                    temp= -1
                else:
                    x1 = p1[0]
                    y1 = p1[1]
                    x2 = p4[0]
                    y2 = p4[1]
                    f1 = p1[2]
                    f2 = p2[2]
                    f3 = p3[2]
                    f4 = p4[2]
                    temp = b_int(x1, x2, y1, y2, f1, f2, f3, f4, x, y)
        the_lst.append(temp)
    return the_lst

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


#TIME FETCH


#*CONSTANT*

def constf(x, t1, t2):
    return ((t2-t1)*x)+t1

def const_time_inverse_cdf(n):
    t1=0
    t2=10

    lst=[constf(random.random(), t1, t2) for _ in list(range(n))]

    return lst

#*INSIDE OUT*

def ins_f(x, m, b):
    alpha=(50*m)+(10*b)
    return -(b/m)+math.sqrt(((b/m)**2)+((2*alpha*x)/m))

def inside_out_time_inverse(n):
    t1=0
    t2=10000000000

    lst1=[ins_f(random.random(), 0.03, 0.36) for _ in list(range(n))]
    return lst1

#*LATE BURST*

def lf1(x, m, b):
    alpha=(50*m)+(10*b)
    return -(b/m)+math.sqrt(((b/m)**2)+((2*alpha*x)/m))

def lf2(x, t1, t2):
    return ((t2-t1)*x)+t1

def late_burst_inverse(n):
    t1=0
    t2=10
    t3=2.65
    t4=5.1
    top = round(n*(1.7395/6.8395))
    bottom = round(n*(5.1/6.8395))

    lst1=[lf1(random.random(), 0.03, 0.36) for _ in list(range(bottom))]
    lst2=[lf2(random.random(), t3, t4) for _ in list(range(top))]
    lst=lst1+lst2
    random.shuffle(lst)
    return lst

#*LATE CONSTANT*

def lcf(x, t1, t2):
    return ((t2-t1)*x)+t1

def late_const_time_inverse_cdf(n):
    t1=8
    t2=10

    lst=[lcf(random.random(), t1, t2) for _ in list(range(n))]

    return lst

#MODEL FETCH


#*SONORA*
def get_sonora():
    file=open("nc+0.0_co1.0_age.txt")
    ages=[]
    masses=[]
    temperatures=[]
    lines=file.readlines()
    for i in list(range(len(lines))):
        ages.append(float(lines[i].split()[1]))
        masses.append(float(lines[i].split()[0]))
        temperatures.append(float(lines[i].split()[3]))
    return ages, masses, temperatures

#*SAUMON MARLEY 2008*
def get_2008():
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

"""#*SAUMON MARLEY 2018*
def get_sm2018():
    file=open("hybrid_solar_mass2018")
    ages=[]
    masses=[]
    temperatures=[]
    lines=file.readlines()
    for i in list(range(len(lines))):
        ages.append(float(lines[i].split()[1]))
        masses.append(float(lines[i].split()[0]))
        temperatures.append(float(lines[i].split()[3]))
    return ages, masses, temperatures
"""
#*BARAFFE*
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
    def __init__(self, age, mass, temp=0):
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
        reference_masses, reference_ages, reference_temperatures=get_sonora()
    elif model_string=="saumonmarley2008":
        reference_ages, reference_masses, reference_temperatures=get_2008()
    elif model_string=='saumonmarley2018':
        reference_ages, reference_masses, reference_temperatures=get_sm2018()
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
    bool_list=[False, False, False]
    count_lst=[0,0,0]
    good_stars=[[],[],[]]
    ml, al, tl = [[], [], []], [[], [], []], [[], [], []]

    for j in list(range(3)):
        sampled_stars=[Star(sampled_ages[i], sampled_masses[j][i]) for i in list(range(n))]
        the_ages=sampled_ages
        the_masses=sampled_masses[j]
        the_temps=bmain(the_ages, the_masses, reference_ages, reference_masses, reference_temperatures)
        for i in list(range(len(sampled_stars))):
            sampled_stars[i].set_temperature(the_temps[i])

        for i in sampled_stars:
            if i.get_temperature()>0:
                count_lst[j]+=1
                good_stars[j].append(i)
        if m<=count_lst[j]:
            bool_list[j]=True
        if bool_list[j]:
            for i in good_stars[j]:
                ml[j].append(i.get_mass())
            ml[j]=ml[j][:m]
            for i in good_stars[j]:
                al[j].append(i.get_age())
            al[j] = al[j][:m]
            for i in good_stars[j]:
                tl[j].append(i.get_temperature())
            tl[j] = tl[j][:m]

    drops=[n-(count_lst[0]),n-(count_lst[1]),n-(count_lst[2])]

    return ml, al, tl, drops