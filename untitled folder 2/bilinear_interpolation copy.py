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

def main(ax, my, age, masses, temps):
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

