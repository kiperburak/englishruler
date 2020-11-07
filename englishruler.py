numberOfTickPerInch = 4
ticks = 2(numberOfTickPerInch - 1) - 1

dict_tick = {}


def generateTick(tick_1, number_1):
    if number_1-1 > 0 and round(tick_1/2) > 0:
        dict_tick[round(tick_1/2)] = round(number_1-1)
        number_1 = number_1 - 1
        if (number_1 > 0):
            generateTick(2(number_1 - 1) - 1, number_1)

def getmod(number):
    for i in dict_tick.keys():
        if i != 0 and i % number == 0:
            return number
    return -1

for i in range(1, ticks):
    generateTick(2**(numberOfTickPerInch - 1) - 1, numberOfTickPerInch)

print(dict_tick)