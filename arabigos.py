def descomponerNumero(numArabigo):
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

    return numDescompuesto

def tratarMillares(millares):
    numRomano = ''
    
    if millares == 0:
        pass
    elif millares == 1:
        numRomano += 'M'
    elif millares == 2:
        numRomano += 'MM'
    elif millares == 3:
        numRomano += 'MMM'
    else:
        resultMil = arabigo_a_romano(millares)
        if '(' == resultMil[0]:
            numRomano = resultMil[0:resultMil.rindex(")")+1] + "(" + resultMil[resultMil.rindex(")")+1:] + ")"
          
        else:
            numRomano = "({})".format(resultMil)
    
    return numRomano

def tratarCentenas(centenas):
    numRomano = ''
   
    if centenas == 0:
        pass
    elif centenas == 1:
        numRomano += 'C'
    elif centenas == 2:
        numRomano +='CC'
    elif centenas == 3:
        numRomano += 'CCC'
    elif centenas == 4:
        numRomano += 'CD'
    elif centenas == 5:
        numRomano += 'D'
    elif centenas == 6:
        numRomano += 'DC'
    elif centenas == 7:
        numRomano += 'DCC'
    elif centenas == 8:
        numRomano += 'DCCC'
    else:
        numRomano += 'CM'

    return numRomano

def tratarDecenas(decenas):
    numRomano =''

    if decenas == 0:
        pass
    elif decenas == 1:
        numRomano += 'X'
    elif decenas == 2:
        numRomano += 'XX'
    elif decenas == 3:
        numRomano += 'XXX'
    elif decenas == 4:
        numRomano += 'XL'
    elif decenas == 5:
        numRomano += 'L'
    elif decenas == 6:
        numRomano += 'LX'
    elif decenas == 7:
        numRomano += 'LXX'
    elif decenas == 8:
        numRomano += 'LXXX'
    else:
        numRomano += 'XC'
    
    return numRomano

def tratarUnidades(unidades):
    numRomano = ''
    if unidades == 0:
        pass
    elif unidades == 1:
        numRomano += 'I'
    elif unidades == 2:
        numRomano += 'II'
    elif unidades == 3:
        numRomano += 'III'
    elif unidades == 4:
        numRomano += 'IV'
    elif unidades == 5:
        numRomano += 'V'
    elif unidades == 6:
        numRomano += 'VI'
    elif unidades == 7:
        numRomano += 'VII'
    elif unidades == 8:
        numRomano += 'VIII'
    else:
        numRomano += 'IX'
        
    return numRomano 
        

def arabigo_a_romano(numArabigo):
    numRomano = ''
    numDescompuesto = descomponerNumero(numArabigo) 
    
    numRomano = tratarMillares(numDescompuesto[0]) + tratarCentenas(numDescompuesto[1]) + tratarDecenas(numDescompuesto[2]) + tratarUnidades(numDescompuesto[3])

    return numRomano

