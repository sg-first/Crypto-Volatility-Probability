kuiRate = 1-0.495
benjin = 150
zhuitou = 150

for i in range(2,31):
    benjin *= kuiRate
    shengyuDay = 31-i
    needBenjin = 2500/(0.00666*75*shengyuDay)
    zhuitou += needBenjin - benjin
    print(i, zhuitou)
    benjin = needBenjin