numberOfTickPerInch = 5
ticks = 2(numberOfTickPerInch - 1) - 1

dict_tick = {}


def generateTick(tick_1, number_1):
    dict_tick[round(tick_1/2)] = round(number_1-1)
    number_1 = number_1 - 1
    if (number_1 > 0):
        generateTick(2(number_1 - 1) - 1, number_1)



for i in range(2):
    generateTick(2(numberOfTickPerInch - 1) - 1, numberOfTickPerInch)

for i in range(ticks):
    for j in range(dict_tick.keys().count()):
        print(dict_tick.get()