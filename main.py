
def isCoinName(line:str):
    return line.find('/USDT')!=-1

def isVolatility(line:str):
    return line.find('%')!=-1

def getCoinName(line:str):
    last=0
    first=0
    cnt=0
    for i in line:
        if i.isalpha():
            first=cnt
            break
        cnt+=1
    cnt+=1
    for i in line[first:]:
        if i=='/':
            last=cnt-1
            break
        cnt+=1
    return line[first:last]

def txtToDict(lines:list):
    retDict = {}
    i = 0
    while i<len(lines):
        line = lines[i]
        if isCoinName(line):
            coinName = getCoinName(line)
            # 找涨幅
            i += 1
            while not isVolatility(lines[i]):
                i += 1
            volatilityStr = lines[i]
            volatilityStr = volatilityStr.replace(' ', '')
            volatility = float(volatilityStr.rstrip('%'))
            retDict[coinName] = volatility
        i += 1
    return retDict

def inquery(timePoint, low, high):
    matchCoinName = []
    for k, v in allRetDict[timePoint].items():
        if v <= high and v >= low:
            matchCoinName.append(k)
    if len(matchCoinName) == 0:
        return [], 0

    nextTimePoint = allRetDict[timePoint+1]
    winRet = []
    failNum = 0
    for k in matchCoinName:
        try:
            nextTimeVolatility = nextTimePoint[k]
            winRet.append(nextTimeVolatility)
        except KeyError:
            failNum += 1
    return winRet, len(winRet) / (len(winRet)+failNum)

start = 0
end = 1
allRetDict = []

for i in range(start, end+1):
    f = open('./data/'+str(i)+'.txt', encoding="utf-8")
    lines = f.read().split('\n')
    allRetDict.append(txtToDict(lines))

for i in range(0,6):
    print(i, inquery(0, i, i+1))


