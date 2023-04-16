import random

zhiying = 0.5
zhisun = -0.85
zhiyingDistance = 1-zhiying
zhisunDistance = 1+zhisun
rate = zhiyingDistance / zhisunDistance * 100
print(rate, rate + 100)

beilv = 75
mubiao = 2500

def test():
    benjin = mubiao / (zhiying / 100 * beilv * 30)
    # print('本金', benjin)
    zhuitou = benjin

    for i in range(1,31):
        if random.randint(0, int(rate) + 100) < rate:
            addMoney = zhiying/100 * beilv * benjin
            benjin += addMoney
            shouyi = benjin - zhuitou
            if shouyi >= mubiao:
                print('SUCCESS', i, 'days. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
                return True, shouyi
        else:
            addMoney = zhisun/100 * beilv * benjin
            benjin += addMoney
            # 失败之后追投
            shengyuDay = 31 - i
            if shengyuDay == 0:
                break
            else:
                needBenjin = mubiao / (zhiying / 100 * beilv * shengyuDay)
                delta = needBenjin - benjin
                if delta > 0:
                    zhuitou += delta
                    benjin = needBenjin
                    if (zhuitou - benjin) >= mubiao:
                        print('FAIL', i, 'days. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
                        return False, benjin - zhuitou

    shouyi = benjin - zhuitou
    print('FAIL. Need money', zhuitou, '剩余', benjin, '收益', shouyi)
    return False, shouyi

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
print(win, fail)
print(sum(allShouyi)/len(allShouyi))