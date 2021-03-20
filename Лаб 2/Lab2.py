import random as rand
from numpy import linalg as lg
import math as mt

x1_min = 20     #-1
x1_max = 70     #1
x2_min = 25     #-1
x2_max = 65     #1

y_max = (30-117)*10
y_min = (20-117)*10

Romanovsky_kriteria = {2: 1.69, 6: 2, 8: 2.17, 10: 2.29, 12: 2.39, 15: 2.49, 20: 2.62}

while True:
    m = 5


    print("y_max: "+str(y_max))
    print("y_min: "+str(y_min))
    print(" ")
    a1 = [rand.randint(y_min, y_max) for i in range(m)]
    a2 = [rand.randint(y_min, y_max) for i in range(m)]
    a3 = [rand.randint(y_min, y_max) for i in range(m)]
    print("Експеримент1 Y: "+str(a1))
    print("Експеримент2 Y: "+str(a2))
    print("Експеримент3 Y: "+str(a3))
    print(" ")
    y_aver1 = sum(a1) / len(a1)
    y_aver2 = sum(a2) / len(a2)
    y_aver3 = sum(a3) / len(a3)
    print("y_aver1: "+str(y_aver1))
    print("y_aver2: "+str(y_aver2))
    print("y_aver3: "+str(y_aver3))
    print(" ")
    a1_vidhul = [y_aver1 - a1[i] for i in range(len(a1))]
    a2_vidhul = [y_aver1 - a2[i] for i in range(len(a2))]
    a3_vidhul = [y_aver1 - a3[i] for i in range(len(a3))]
    print("a1_vidhul: "+str(a1_vidhul))
    print("a2_vidhul: "+str(a2_vidhul))
    print("a3_vidhul: "+str(a3_vidhul))
    print(" ")
    a1_vidh_kvad = []
    a2_vidh_kvad = []
    a3_vidh_kvad = []
    for i in range(len(a1)):
        a1_vidh_kvad.append(a1_vidhul[i] ** 2)
        a2_vidh_kvad.append(a2_vidhul[i] ** 2)
        a3_vidh_kvad.append(a3_vidhul[i] ** 2)
    print("a1_vidh_kvad: "+str(a1_vidh_kvad))
    print("a2_vidh_kvad: "+str(a2_vidh_kvad))
    print("a3_vidh_kvad: "+str(a3_vidh_kvad))
    print(" ")
    a1_disp = sum(a1_vidh_kvad) / len(a1_vidh_kvad)
    a2_disp = sum(a2_vidh_kvad) / len(a2_vidh_kvad)
    a3_disp = sum(a3_vidh_kvad) / len(a3_vidh_kvad)
    print("a1_disp: "+str(a1_disp))
    print("a2_disp: "+str(a2_disp))
    print("a3_disp: "+str(a3_disp))
    print(" ")
    a1_disp_perc = a1_disp / (a1_disp + a2_disp + a3_disp)
    a2_disp_perc = a2_disp / (a1_disp + a2_disp + a3_disp)
    a3_disp_perc = a3_disp / (a1_disp + a2_disp + a3_disp)
    print("a1_disp_perc: "+str(a1_disp_perc))
    print("a2_disp_perc: "+str(a2_disp_perc))
    print("a3_disp_perc: "+str(a3_disp_perc))
    print(" ")

    disp0 = mt.sqrt(2*(2*m-2)/m*(m-4))
    keys = list(Romanovsky_kriteria.keys())
    key = 0
    for i in keys:
        if m <= i:
            key = i
            break
    Rkr = Romanovsky_kriteria.get(key)

    Fuv1 = a1_disp / a2_disp
    Fuv2 = a3_disp / a1_disp
    Fuv3 = a3_disp / a2_disp
    print("Fuv1: "+str(Fuv1))
    print("Fuv2: "+str(Fuv2))
    print("Fuv3: "+str(Fuv3))
    print(" ")
    Ouv1 = ((m-2)/m)*Fuv1
    Ouv2 = ((m-2)/m)*Fuv2
    Ouv3 = ((m-2)/m)*Fuv3
    print("Ouv1: "+str(Ouv1))
    print("Ouv2: "+str(Ouv2))
    print("Ouv3: "+str(Ouv3))
    print(" ")
    Ruv1 = abs(Ouv1 - 1)/disp0
    Ruv2 = abs(Ouv2 - 1)/disp0
    Ruv3 = abs(Ouv3 - 1)/disp0
    if Ruv1 < Rkr and Ruv2 < Rkr and Ruv3 < Rkr:
        break
    if m < 20:
        m += 1

print("Ruv1: "+str(Ruv1))
print("Ruv2: "+str(Ruv2))
print("Ruv3: "+str(Ruv3))
print(str(Ruv1)+"<Rkr = " + str(Rkr))
print(str(Ruv2)+"<Rkr = " + str(Rkr))
print(str(Ruv3)+"<Rkr = " + str(Rkr))
print(" ")
mx1 = (-1+1+(-1))/3
mx2 = (-1+(-1)+1)/3
my = (y_aver1 + y_aver2+ y_aver3)/3
print("mx1: "+str(mx1))
print("mx2: "+str(mx2))
print("my: "+str(my))
print(" ")
A1 = (1+1+1)/3
A2 = (1-1-1)/3
A3 = (1+1+1)/3
print("A1: "+str(A1))
print("A2: "+str(A2))
print("A3: "+str(A3))
print(" ")
A11 =(-1*y_aver1+1*y_aver2-1*y_aver3)/3
A22 =(-1*y_aver1-1*y_aver2+1*y_aver3)/3
print("A11: "+str(A11))
print("A22: "+str(A22))
print(" ")
b0 = (lg.det([[my, mx1, mx2],
                 [A11, A1, A2],
                 [A22, A2, A3]]))/(lg.det([[1, mx1, mx2],
                                               [mx1, A1, A2],
                                               [mx2, A2, A3]]))
b1 = (lg.det([[1, my, mx2],
                 [mx1, A11, A2],
                 [mx2, A22, A3]]))/(lg.det([[1, mx1, mx2],
                                               [mx1, A1, A2],
                                               [mx2, A2, A3]]))
b2 = (lg.det([[1, mx1, my],
                 [mx1, A1, A11],
                 [mx2, A2, A22]]))/(lg.det([[1, mx1, mx2],
                                               [mx1, A1, A2],
                                               [mx2, A2, A3]]))
print("b0: "+str(b0))
print("b1: "+str(b1))
print("b2: "+str(b2))
print("Y1 = : "+str(b0 + b1*-1 + b2*(-1)))
print("Y2 = : "+str(b0 + b1*1 + b2*(-1)))
print("Y3 = : "+str(b0 + b1*(-1) + b2*1))
print("Y = "+str(b0)+" + "+str(b1)+"*x1 + "+str(b2)+"*x2")
print(" ")
Dx1 = abs(x1_max-x1_min)/2
Dx2 = abs(x2_max-x2_min)/2
x10 = (x1_max+x1_min)/2
x20 = (x2_max+x2_min)/2
print("Dx1: "+str(Dx1))
print("Dx2: "+str(Dx2))
print("x10: "+str(x10))
print("x20: "+str(x20))
print(" ")
a0 = b0-b1*(x10/Dx1)-b2*(x20/Dx2)
a1 = b1/Dx1
a2 = b2/Dx2
print("a0: "+str(a0))
print("a1: "+str(a1))
print("a2: "+str(a2))
print(" ")
print("Ynat1 = : "+str(a0 + a1*x1_min + a2*x2_min))
print("Ynat2 = : "+str(a0 + a1*x1_max + a2*x2_min))
print("Ynat3 = : "+str(a0 + a1*x1_min + a2*x2_max))
print("Ynat = "+str(a0)+" + "+str(a1)+"*x1 + "+str(a2)+"*x2")
print(" ")