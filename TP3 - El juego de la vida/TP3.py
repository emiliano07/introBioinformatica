#DESAFIO I

"""
Algunas diferencias entre las celulas procariotas y eucariotas:
- Las célular eucariotas tienen nucleo, las procariotas no.
- Las células eucariotas pueden ser multicelulares, y las procariotas son siempre unicelulares.
- La forma de las células eucariotas es circular, la de las procariotas es alargada.
- El material genetico en las células eucariotas esta dentro del nucleo, y en las procariotas disperso por el citoplasma
"""

print("------------------------------------")

#DESAFIO II

sec = "ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA"
ARN = "AUG" #Met

for i in sec:
    if i == "A": #Ala
        ARN += "GCU"
    elif i == "R": #Arg
            ARN += "AGA"
    elif i == "N": #Asn
            ARN += "AAU"
    elif i == "D": #Asp
            ARN += "GAU"
    elif i == "C": #Cys
            ARN += "UGU"
    elif i == "Q": #Gln
            ARN += "CAA"
    elif i == "E": #Glu
            ARN += "GAA"
    elif i == "G": #Gly
            ARN += "GGU"
    elif i == "H": #His
            ARN += "CAU"
    elif i == "I": #Iso
            ARN += "AUU"
    elif i == "L": #Leu
            ARN += "UUA"
    elif i == "K": #Lys
            ARN += "AAA"
    elif i == "M": #Met
            raise ValueError("La cadena esta mal formada")
    elif i == "F": #Phe
            ARN += "UUU"
    elif i == "P": #Pro
            ARN += "CCU"
    elif i == "S": #Ser
            ARN += "UCU"
    elif i == "T": #Thr
            ARN += "ACU"
    elif i == "W": #Try
            ARN += "UGG"
    elif i == "Y": #Tyr
            ARN += "UAU"
    elif i == "V": #Val
            ARN += "GUU"
    else:
        raise ValueError("Se ha ingresado un aminoacido inexistente")

ARN += "UAA"; #STOP

print(ARN)

print("Tenga en cuenta que se imprime una sola de las variantes posibles.")
print("Para los casos de mas de un codon se eligio el tercer nucleotico en este orden de prioridad:")
print("U > C > A > G")

print("------------------------------------")

#DESAFIO III

sec = "AGGTTTGGACCACTTGTATAAACTAGCTGACTAGCATACGTAGCTCAGTACGTATAAAAACTAGTACCATACGTGACTAGCAGTACGTATAAAACTAGCAGCTTAGCATACGTAGTACGTATAAAACGT"

cond = True
secAux = sec

while cond:
    
    gen = ""
    genAux = ""

    caja_tata_inicio = secAux.find("TATAAA")

    genAux = secAux[(caja_tata_inicio+6):len(secAux)]

    caja_tata_fin = genAux.find("TATAAA")

    gen = genAux[0:caja_tata_fin]

    if caja_tata_fin == -1:
        cond = False
    else:
        secAux = genAux[caja_tata_fin:len(genAux)]
        print(gen)

print("------------------------------------")
