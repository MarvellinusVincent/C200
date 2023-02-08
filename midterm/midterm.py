########
########
# Write you code for midterm problems in this file.
# Do not change the name of this file.
########
def f(xlst,n):
    list = []
    for each_list in xlst:
        if len(each_list) > n:
            list.append(each_list)
    return list

def gravity (m1,m2,d):
    law = ((6.67*(10**(-11)))*m1*m2)/(d**2) 
    return law

tip = {"bad":15, "good":20, "great":25}
def tip_amt(t):
    bill = t[0]
    evaluation = t[1]
    final_bill = bill+(bill*tip[evaluation]/100)
    return final_bill