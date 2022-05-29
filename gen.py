from scipy.stats import chisquare,kstest

gens1 = [0]
gens2 = [0]
f1="0"
f2="1"
while len(f2)<1000:
    f1, f2 = f2, f1 + f2
C = [int(x) for x in list(f2)]
for i in range(1000):
    gens1.append(((30-17)*gens1[-1] + 71) % (10+17))

for i in range(1000):
    gens2.append(((30-3)*gens2[-1] + 71) % (13))    

C = [gens1[i]*C[i]+gens2[i]*(1-C[i]) for i in range(1000)]



#chi^2 test
def chi(D):
    n,p = chisquare(D)
    if p <= 0.05:
        return("X^2 значениея не случайны")
    else:
        return("X^2 значениея случайны")

#kstest test
def kst(D):
    n,p = kstest(D,'norm')
    if p <= 0.05:
        return("КолмогоровСмирнов значениея не случайны")
    else:
        return("КолмогоровСмирнов значениея случайны") 

#gaptest
def gap_test(D):
    vv = {}
    for i in range(1000):
        k = D[i]
        if k in vv:
            vv[k].append(i - vv[k][0])
            vv[k][0] = i
        else:
            vv[k] = [i]
    return vv

#frequency_test
def freq(D):
    f = {}
    for i in range(1000):
        if D[i] in f:
            f[D[i]] += 1
        else:
            f[D[i]] = 0
    return f
print("A:" + chi(gens1))
print("B:" + chi(gens2))
print("C:" + chi(C))

print("A:" + kst(gens1))
print("B:" + kst(gens2))
print("C:" + kst(C))

print("gap:")
print("A:" + gap_test(gens1).__str__())
print("B:" + gap_test(gens2).__str__())
print("C:" + gap_test(C).__str__())

print("freq:")
print("A:" + freq(gens1).__str__())
print("B:" + freq(gens2).__str__())
print("C:" + freq(C).__str__())




