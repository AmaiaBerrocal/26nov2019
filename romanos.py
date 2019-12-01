valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50, 'D':500}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
valor = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''

    for letra in numRomano:
        if letra in valores:
            numArabigo += valores[letra]
            if ultimoCaracter == '':
                pass
            elif valores[ultimoCaracter] > valores[letra]:
                numRepes = 1
            elif valores[ultimoCaracter] == valores[letra]:
                numRepes += 1

                if letra in valores5:
                    return 0

                if numRepes > 3:
                    return 0
            elif valores[ultimoCaracter] < valores[letra]:    
                if numRepes > 1:
                    return 0
                
                if ultimoCaracter in valores5:
                    return 0

                distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter)
                if distancia > 2:
                        return 0

                numArabigo -= valores[ultimoCaracter]*2
                numRepes = 1
        else:
            return 0

        ultimoCaracter = letra

    return numArabigo


def arabigo_a_romano(numArabigo):
   
    numDescompuesto = []

    millares = numArabigo // 1000
    numDescompuesto.append(millares)

    restoC = numArabigo % 1000 

    centenas = restoC // 100 
    numDescompuesto.append(centenas)
   
    restoD = restoC % 100 

    decenas = restoD // 10 
    numDescompuesto.append(decenas)

    unidades = restoD % 10 
    numDescompuesto.append(unidades)


arabigo_a_romano(456)