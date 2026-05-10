def questaoA():
    num = int(input())
    div = num // 3
    res = num % 3
    print(div)
    print(res)



def questaoB():
    x = int(input())
    z = int(input())

    h = (x - 34)**2 + (z - 220)**2
    h = h**0.5
    k = x**2 + z**2
    k = k**0.5
    s = (x - 140)**2 + (z - 456)**2
    s = s**0.5

    print(f"Distancia para Hogsmeade: {h:.2f}")
    print(f"Distancia para Kakariko: {k:.2f}")
    print(f"Distancia para Solitude: {s:.2f}")



def questaoC():
    x = int(input())
    z = int(input())

    sum = (x*x*z)

    print(sum)



def questaoD():
    a = int(input())
    l = int(input())
    p = int(input())
    h = int(input())

    a = a * h
    l = l * h
    p = p * h


    valMax = (a + l + (abs(a - l))) // 2
    valMax = (valMax + p + (abs(valMax - p))) // 2

    print(valMax)
    


def questaoE():
    a = int(input())
    l = int(input())

    ticks = (a * 10800 * 10) // l
    print(ticks)



def questaoF():
    firstName = input()
    secondName = input()
    fullName = firstName + secondName
    print(fullName)
    
 
    
def questaoG():
    num = int(input())
    if (num >= 1) and (num <= 10):
        print("Arthur")
    elif (num <= 30):
        print("Luiz")
    elif (num <= 100):
        print("Pedro")
    else:
        print("Nenhum")