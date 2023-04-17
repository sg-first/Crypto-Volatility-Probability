zhiying = 0.5
zhisun = -0.8
times = 25
mubiao = 2500
beilv = 75
benjin = mubiao / (zhiying / 100 * beilv * times)
kuiRate = 1 - (-zhisun/100 * beilv)
print(benjin, kuiRate)
zhuitou = benjin

for i in range(2, times + 1):
    benjin *= kuiRate
    shengyuDay = times + 1 - i
    needBenjin = mubiao / (zhiying / 100 * beilv * shengyuDay)
    print(i, needBenjin, 'needMoney')
    zhuitou += needBenjin - benjin
    # print(i, zhuitou, 'zhuitou')
    benjin = needBenjin