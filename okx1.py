from okx_api import Market

market = Market()
allPriceList = []

def pull():
    result = market.get_tickers('SWAP')
    data = result['data']
    priceList = {}
    for i in data:
        coinName = i['instId']
        if '-USDT' in coinName:
            coinName = coinName.replace('-USDT-SWAP', '')
            price = i['askPx']
            priceList[coinName] = price
    allPriceList.append(priceList)
    return priceList
pull()

allIncreaseList = []
def pullAndCalc():
    print('>>>> NEW DATA')
    priceList2 = pull()
    priceList1 = allPriceList[len(allPriceList)-2]

    increaseList = {}
    increaseListFull = {}
    for k,v in priceList2.items():
        try:
            v = float(v)
            v1 = float(priceList1[k])
            increase = (v - v1) / v1
            if increase<0 and increase>-0.01:
                increaseList[k] = increase
            increaseListFull[k] = increase
        except ValueError:
            continue
    allIncreaseList.append(increaseList)

    increaseList1 = allIncreaseList[len(allIncreaseList)-2]
    risingV = []
    fallingV = []
    for k, _ in increaseList1.items():
        try:
            v = increaseListFull[k]
            if v > 0:
                risingV.append(v)
                print(k, v, 'RISE')
            else:
                fallingV.append(v)
                print(k, v, 'FALL')
        except KeyError:
            continue
    if len(risingV)!=0:
        val = sum(risingV) / len(risingV)
        print('rising AVG:', val*100)
    if len(fallingV)!=0:
        val = sum(fallingV) / len(fallingV)
        print('falling AVG:', val*100)
    print('RATE', len(risingV) / (len(risingV) + len(fallingV)))

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)
while True:
    scheduler.enter(60*60, 0, pullAndCalc)
    scheduler.run()