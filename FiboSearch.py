#fungsi mencari element x memakai FibonacciSearch
def fib(n):
    if n < 1 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

def Fibonaccisearch(var,x):
    n = 0
    while fib(n) < len(var):
        n = n + 1
    offset = -1
    while (fib(n) > 1):
        i = min(offset + fib(n-2), len(var) - 1)
        if (x > var[i]):
            n = n -1
            offset = i
        elif (x < var[i]):
            n = n - 2
        else :
            return i
    if(fib(n-1) and var[offset + 1] == x):
        return offset + 1
    return -1

#fungsi memisahkan antara list dan string
def pemisah(var) :
    varsorted = []
    varbersarang = {} 
    for i in range(len(var)) :
        if type(var[i]) == str :
            varsorted.append(var[i])
        else :
            varbersarang[i] = var[i]

    for i in varbersarang :
        varsorted.insert(i, varbersarang[i])

    return varsorted    

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
varsorted = pemisah(var)

print("-"*48)
print(var)
print("-"*48)
x = str(input("Silahkan Masukkan Nama: "))

#index dan kolom dari element x
for index in range(len(varsorted)) :
    if type(varsorted[index]) == list :
        kolom = Fibonaccisearch(varsorted[index], x)
        if kolom != -1 : print(f'{x} berada di index {index} kolom {kolom}')
    else :
        if varsorted[index] == x : print(f'{x} berada di index {index}')
print("-"*48)