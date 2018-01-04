import random

newDeck = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
numberOfTries = 1000
totals = {}
attributes = ['str','dex','con','int','wis','cha']

def Deck():
    return list(newDeck)

def outputTotals():
    for n in range(6,20):
        if n in totals:
            print(n, "\t: ", totals[n]*100/numberOfTries/len(attributes))

def outputAvg():
    runningSum = 0
    runningTotal = 0
    for n in range(6, 20):
        if n in totals:
            runningSum += n * totals[n]
            runningTotal += totals[n]
    if runningTotal != numberOfTries * len(attributes):
        print("error in total")
    print("average: ", runningSum/runningTotal)

print("Rolling",numberOfTries,"characters using card draw...")
print("distribution of attributes:")
tryNum = 0
while tryNum < numberOfTries:
    deck = Deck()
    for attribute in attributes:
        allJokers = False

        draws = []
        for card in range(3):
            draw = random.choice(deck)
            deck.remove(draw)
            draws.append(draw)
            #print(tryNum, attribute, draws, " : ", deck)
        while 1 in draws:
            if max(draws) == 1:
                allJokers = True
                break
            draws.remove(1)
            draws.append(max(draws))
        if allJokers:
            attr = 19
        else:
            attr = sum(draws)
        #print(attr)
        if not attr in totals:
            totals[attr] = 1
        else:
            totals[attr] += 1
    tryNum += 1

outputTotals()
outputAvg()