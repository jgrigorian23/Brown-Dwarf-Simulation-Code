import get_sm2018
import get_sonora
import get_baraffe
import get_2008
import late_burst_inverse
import inside_out_time_inverse
import const_time_inverse_cdf
import late_const_time_inverse_cdf
import inverse_power
import bilinear_interpolation



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
        reference_ages, reference_masses, reference_temperatures=get_sonora.main()
    elif model_string=="saumonmarley2008":
        reference_ages, reference_masses, reference_temperatures=get_2008.main()
    elif model_string=='saumonmarley2018':
        reference_ages, reference_masses, reference_temperatures=get_sm2018.main()
    elif model_string=='baraffe':
        reference_ages, reference_masses, reference_temperatures=get_baraffe.main()





    sampled_masses=inverse_power.main(float(alpha), n)

    if time=="const":
        sampled_ages = const_time_inverse_cdf.main(n)
    elif time=="late_const":
        sampled_ages = late_const_time_inverse_cdf.main(n)
    elif time=="inside_out":
        sampled_ages = inside_out_time_inverse.main(n)
    elif time=="late_burst":
        sampled_ages = late_burst_inverse.main(n)
    bool_list=[False, False, False]
    count_lst=[0,0,0]
    good_stars=[[],[],[]]
    ml, al, tl = [[], [], []], [[], [], []], [[], [], []]

    for j in list(range(3)):
        sampled_stars=[Star(sampled_ages[i], sampled_masses[j][i]) for i in list(range(n))]
        the_ages=sampled_ages
        the_masses=sampled_masses[j]
        the_temps=bilinear_interpolation.main(the_ages, the_masses, reference_ages, reference_masses, reference_temperatures)
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




