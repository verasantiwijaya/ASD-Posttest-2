#fungsi mencari element x memakai Jump Search
def jumpSearch(var, x):
    n = len(var)
    step = int(n ** 0.5)

    prev = 0
    while var[min(step, n) - 1] < x:
        prev = step
        step += int(n ** 0.5)
        if prev >=n:
            return -1

    while var[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if var[prev] == x:
        return prev
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
        kolom = jumpSearch(varsorted[index], x)
        if kolom != -1 : print(f'{x} berada di index {index} kolom {kolom}')
    else :
        if varsorted[index] == x : print(f'{x} berada di index {index}')
print("-"*48)