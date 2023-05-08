import random

times = 30
zhiying = 0.1
zhisun = -0.8
_zhisun = None
totalProb = None
rate = None
def reset(zhiyingPar, zhisunPar):
    global rate, totalProb, _zhisun, zhiying, zhisun
    zhiying = zhiyingPar
    zhisun = zhisunPar
    _zhiying = zhiying * 1000
    _zhisun = -zhisun * 1000
    totalProb = _zhiying + _zhisun
    rate = _zhisun / totalProb
    print(rate, totalProb, _zhisun, _zhiying)
reset(zhiying, zhisun)

beilv = 75
mubiao = 3000
maxTouru = 1000

def test():
    benjin = mubiao / (zhiying / 100 * beilv * times)
    # print('本金', benjin)
    zhuitou = benjin

    for i in range(1, times+1):
        for _ in range(4):
            if random.randint(0, int(totalProb)) < _zhisun:
                addMoney = zhiying/100 * beilv * benjin
                benjin += addMoney
                shouyi = benjin - zhuitou
                # print('WIN', benjin, shouyi)
                if shouyi >= mubiao:
                    # print('SUCCESS', i, 'days. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
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
                            # print('FAIL', i, 'days. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
                            return False, shouyi

    shouyi = benjin - zhuitou
    # print('FAIL. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
    return False, shouyi

def expectations():
    win = 0
    fail = 0
    allShouyi = []
    for i in range(500):
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

zhiying = 0.1
bestZhiying = None
bestZhisun = None
bestRate = -1
while zhiying < 1:
    zhisun = -0.8
    while zhisun < -0.1:
        print('now test', zhiying, zhisun)
        reset(zhiying, zhisun)
        rate, exp = expectations()
        if rate > bestRate:
            bestRate = rate
            bestZhisun = zhisun
            bestZhiying = zhiying
        zhisun += 0.1
    zhiying += 0.1

print(bestZhiying, bestZhisun, bestRate)
