import random as rndm

def Calc(a0, a1, a2, a3):
    x1 = rndm.randint(0, 20)
    x2 = rndm.randint(0, 20)
    x3 = rndm.randint(0, 20)
    res = a0 + a1*x1 + a2*x2 + a3*x3
    return [x1, x2, x3, res]

def Table(a0, a1, a2, a3):
    tab = [[], [], [], []]
    for i in range(8):
        ln = Calc(a0, a1, a2, a3)
        for j in range(len(tab)):
            tab[j].append(ln[j])
    return tab

def X0_Dx(tab):
    x01 = (max(tab[0]) + min(tab[0])) / 2
    x02 = (max(tab[1]) + min(tab[1])) / 2
    x03 = (max(tab[2]) + min(tab[2])) / 2
    dx1 = max(tab[0]) - x01
    dx2 = max(tab[1]) - x02
    dx3 = max(tab[2]) - x03
    x0_dx = [[x01, x02, x03], [dx1, dx2, dx3]]
    return x0_dx

def Xn(tab, x0_dx):
    xnt = [[], [], []]
    for i in range(len(tab) - 1):
        for j in range(len(tab[i])):
            xn = (tab[i][j] - x0_dx[0][i])/x0_dx[1][i]
            xnt[i].append(round(xn, 4))
    return xnt

a0 = 4
a1 = 6
a2 = 9
a3 = 13

tab = Table(a0, a1, a2, a3)
for i in range(len(tab)):
    print("X1") if i==0 else print("X2") if i==1 else print("X3") if i==2 else print("Y")
    print(tab[i])
print("")

X0_Dx_out = X0_Dx(tab)
for i in range(len(X0_Dx_out)):
    print("X0") if i == 0 else print("Dx")
    print(X0_Dx_out[i])
print("")

Xn_tab = Xn(tab, X0_Dx_out)
for i in range(len(Xn_tab)):
    print("Xn1") if i==0 else print("Xn2") if i==1 else print("Xn3")
    print(Xn_tab[i])
print("")

g = tab[3].index(min(tab[3]))
print("min(Y): " + str(tab[0][g]) + ", " + str(tab[1][g]) + ", " + str(tab[2][g]))