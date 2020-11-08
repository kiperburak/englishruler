'English Ruler'
'390626 Burak Kiper'
'348398 Muhammed Halim Güleşen'


'İki inch arası boşluk sayısına göre tickler bu fonksiyonda hesaplanıp ayrılır'
'Mesela 5 tickli bi inch gösterimi düşünürsek iki inch birimi arasında(2**(5-1)-1)=15 boşluk olacaktır.'
'generateTick fonksiyonu da bu boşluklar arasının ortalarını bularak onları tick_dictionary içine atar.'
'Örneğin 8:4,4:3,2:2... olacak şekilde'
def generateTick(tick, number, tick_dictionary):
    if number-1 > 0 and round(tick/2) > 0:
        tick_dictionary[round(tick/2)] = round(number-1)
        number = number - 1
        if (number > 0):
            generateTick(2**(number - 1) - 1, number, tick_dictionary)
    return tick_dictionary

def getmod(number, tick_dictionary):
    for i in tick_dictionary.keys():
        if number % i == 0:
            return tick_dictionary.get(i)
    return -1
'Görüldüğü üzere fonksiyon kendini çağırmaktadır(tick_directionary).Bu yüzden fonksiyon lineer recursion"a sahiptir.'
def printLine(tick_dictionary, numberOfTickPerInch, rulerSize):
    for j in range(0, rulerSize):
        print("-"*numberOfTickPerInch, j)
        for i in range(1, ticks+1):
            mode = getmod(i, tick_dictionary)
            if i in tick_dictionary.keys():
                print("-"*tick_dictionary.get(i))
            elif mode != -1:
                print("-"*mode)
            else:
                print("-")
    print("-"*numberOfTickPerInch, rulerSize)
'Fonksiyonun karmaşıklık analizine bakar isek,görüldüğü üzere iki for döngüsünün değişkenleri bize karmaşıklığı vermektedir'
'Bunlar da rulerSize ve ticks değişkenleridir(ticks değişkeni de numberofTickPerInch değişkenine bağlıdır.)'
'O yüden karmaşıklık O(rulerSize*numberOfTickPerInch) olacaktır.'
if __name__ == '__main__':
    rulerSize = 2
    numberOfTickPerInch = 5
    ticks = 2**(numberOfTickPerInch - 1) - 1
    tick_dictionary = {}

    generateTick(ticks, numberOfTickPerInch, tick_dictionary)
    printLine(tick_dictionary, numberOfTickPerInch, rulerSize)
