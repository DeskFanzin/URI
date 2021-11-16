x = int(input())


def romuni(uni):
    if uni == 0:
        romana = ""
    if 1 <= uni <= 3:
        romana = ""
        for i in range(uni):
            romana += "I"
    if uni == 4:
        romana = "IV"
    if 5 <= uni <= 8:
        romana = "V"
        z = uni-5
        for i in range(z):
            romana += "I"
    if uni == 9:
        romana = "IX"
    return romana


def romdez(dez):
    if dez == 0:
        romana = ""
    if 1 <= dez <= 3:
        romana = ""
        for i in range(dez):
            romana += "X"
    if dez == 4:
        romana = "XL"
    if 5 <= dez <= 8:
        romana = "L"
        z = dez-5
        for i in range(z):
            romana += "X"
    if dez == 9:
        romana = "XC"
    return romana


def romcen(cen):
    if 1 <= cen <= 3:
        romana = ""
        for i in range(cen):
            romana += "C"
    if cen == 4:
        romana = "CD"
    if 5 <= cen <= 8:
        romana = "D"
        z = cen-5
        for i in range(z):
            romana += "C"
    if cen == 9:
        romana = "CM"
    return romana


y = [int(i) for i in str(x)]
if len(y) == 1:
    uni = y[0]
    print(romuni(uni))
elif len(y) == 2:
    dez = y[0]
    uni = y[1]
    print(romdez(dez) + romuni(uni))
else:
    cen = y[0]
    dez = y[1]
    uni = y[2]
    print(romcen(cen) + romdez(dez) + romuni(uni))
