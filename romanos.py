valores = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50, 'D':500}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


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
        elif ultimoCaracter == ')':
            numArabigo = numArabigo * 1000

        else:
            return 0

        ultimoCaracter = letra

    return numArabigo


def arabigo_a_romano(numArabigo):
    numRomano = ''
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

    
    if numDescompuesto[0] == 0:
        pass
    elif numDescompuesto[0] == 1:
        numRomano += 'M'
    elif numDescompuesto[0] == 2:
        numRomano += 'MM'
    elif numDescompuesto[0] == 3:
        numRomano += 'MMM'
    else:
        return 0

    if numDescompuesto[1] == 0:
        pass
    elif numDescompuesto[1] == 1:
        numRomano += 'C'
    elif numDescompuesto[1] == 2:
        numRomano +='CC'
    elif numDescompuesto[1] == 3:
        numRomano += 'CCC'
    elif numDescompuesto[1] == 4:
        numRomano += 'CD'
    elif numDescompuesto[1] == 5:
        numRomano += 'D'
    elif numDescompuesto[1] == 6:
        numRomano += 'DC'
    elif numDescompuesto[1] == 7:
        numRomano += 'DCC'
    elif numDescompuesto[1] == 8:
        numRomano += 'DCCC'
    else:
        numRomano += 'CM'

    if numDescompuesto[2] == 0:
        pass
    elif numDescompuesto[2] == 1:
        numRomano += 'X'
    elif numDescompuesto[2] == 2:
        numRomano += 'XX'
    elif numDescompuesto[2] == 3:
        numRomano += 'XXX'
    elif numDescompuesto[2] == 4:
        numRomano += 'XL'
    elif numDescompuesto[2] == 5:
        numRomano += 'L'
    elif numDescompuesto[2] == 6:
        numRomano += 'LX'
    elif numDescompuesto[2] == 7:
        numRomano += 'LXX'
    elif numDescompuesto[2] == 8:
        numRomano += 'LXXX'
    else:
        numRomano += 'XC'
        
    if numDescompuesto[3] == 0:
        pass
    elif numDescompuesto[3] == 1:
        numRomano += 'I'
    elif numDescompuesto[3] == 2:
        numRomano += 'II'
    elif numDescompuesto[3] == 3:
        numRomano += 'III'
    elif numDescompuesto[3] == 4:
        numRomano += 'IV'
    elif numDescompuesto[3] == 5:
        numRomano += 'V'
    elif numDescompuesto[3] == 6:
        numRomano += 'VI'
    elif numDescompuesto[3] == 7:
        numRomano += 'VII'
    elif numDescompuesto[3] == 8:
        numRomano += 'VIII'
    else:
        numRomano += 'IX'
        
    return numRomano 
        


            

