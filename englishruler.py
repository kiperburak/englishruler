numberOfTickPerInch = 5
ticks = 2**(numberOfTickPerInch - 1) - 1

dict_tick = {}



def generateTick(tick_1, number_1):
    dict_tick[round(tick_1/2)] = round(number_1-1)

print(dict_tick)