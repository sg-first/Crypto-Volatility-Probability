
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

start = 0
end = 0
allRetDict = []

for i in range(start, end+1):
    f = open('./data/'+str(i)+'.txt', encoding="utf-8")
    lines = f.read().split('\n')
    allRetDict.append(txtToDict(lines))