
def gasStation(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    diffSum = 0
    start = 0
    for pos in range(len(gas)):
        diffSum += gas[pos] - cost[pos]
        if diffSum < 0:
            start = pos + 1
            diffSum = 0
    return start

print gasStation([1,1,3,1],[2,2,1,1])
