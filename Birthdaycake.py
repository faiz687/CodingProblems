def cakess(candles):
    # return candles.count(max(candles))
    maxi = 0
    frequency = 1 
    for i in range(len(candles)):
        if candles[i] > maxi:
            maxi = candles[i]
            frequency = 1
        elif candles[i] == maxi:
            frequency += 1
    return  frequency
 print(cakess("")
