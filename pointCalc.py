b = float(input('本金'))
a = float(input('现价'))
print(a*1.01)
print(a*0.98)
print(int(b/a)*30)

while True:
    c = float(input('倍率'))
    print(int(b / a) * c)