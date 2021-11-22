import numpy as np

conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 10000
d = len(conversionRates)

X = np.zeros((N, d))

#preparing the data
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            X[i][j] = 1
    #print(X[i])

nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

#let's play
for i in range(N):
    selected = 0
    maxRandom = 0
    for j in range(d):
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            selected = j
            maxRandom = randomBeta

    if X[i][selected] == 1:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] += 1

#show results
nSelected = nPosReward + nNegReward
for i in range(d):
    print("Machine: " + str(i + 1) + " was selected: " + str(nSelected[i]) + " times")

print( "The best machine is: " + str(np.argmax(nSelected) + 1))




