import random

times = 730
zhiying = 0.5
zhisun = -0.8
_zhisun = None
totalProb = None
rate = None
def reset():
    global rate, totalProb, _zhisun
    _zhiying = zhiying * 10
    _zhisun = -zhisun * 10
    totalProb = _zhiying + _zhisun
    rate = _zhisun / totalProb
reset()
print(totalProb, _zhisun)

beilv = 75
mubiao = 3200
maxTouru = 130

def test():
    benjin = mubiao / (zhiying / 100 * beilv * times)
    print('本金', benjin)
    zhuitou = benjin

    for i in range(1, times+1):
        for _ in range(4):
            if random.randint(0, totalProb) < _zhisun:
                addMoney = zhiying/100 * beilv * benjin
                benjin += addMoney
                shouyi = benjin - zhuitou
                # print('WIN', benjin, shouyi)
                if shouyi >= mubiao:
                    print('SUCCESS', i, 'days. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
                    return True, shouyi
            else:
                addMoney = zhisun/100 * beilv * benjin
                benjin += addMoney
                # 失败之后追投
                shengyuDay = times + 1 - i
                if shengyuDay == 0:
                    break
                else:
                    needBenjin = mubiao / (zhiying / 100 * beilv * shengyuDay)
                    delta = needBenjin - benjin
                    if delta > 0:
                        zhuitou += delta
                        benjin = needBenjin
                        # print('FAIL', benjin, benjin - zhuitou)
                        if (zhuitou - benjin) >= maxTouru:
                            shouyi = benjin - zhuitou
                            print('FAIL', i, 'days. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
                            return False, shouyi

    shouyi = benjin - zhuitou
    print('FAIL. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
    return False, shouyi

def expectations():
    win = 0
    fail = 0
    allShouyi = []
    for i in range(1000):
        ret, shouyi = test()
        allShouyi.append(shouyi)
        if ret:
            win += 1
        else:
            fail += 1
    rate = win / (fail + win)
    exp = sum(allShouyi) / len(allShouyi)
    print('>>>>胜率', rate, exp, 'in', zhiying, zhisun)
    return rate, exp
expectations()
'''
zhiying = 0.1
zhisun = -0.8
bestZhiying = None
bestZhisun = None
bestRate = -1
while zhiying < 1:
    zhisun = -0.8
    while zhisun < -0.1:
        print('now test', zhiying, zhisun)
        reset()
        rate, exp = expectations()
        if rate > bestRate and exp > 1500:
            bestRate = rate
            bestZhisun = zhisun
            bestZhiying = zhiying
        zhisun += 0.1
    zhiying += 0.1

print(bestZhiying, bestZhisun, bestRate)
'''