import random

newDeck = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6]
numberOfTries = 1000000
totals = {}

def Deck():
    return list(newDeck)

def outputTotals():
    for n in range(6,20):
        print(n, "\t: ", totals[n]*100/numberOfTries)

tryNum = 0
while tryNum < numberOfTries:
    allJokers = False
    deck = Deck()
    draws = []
    for card in range(3):
        draw = random.choice(deck)
        deck.remove(draw)
        draws.append(draw)
        #print(draws, " : ", deck)
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