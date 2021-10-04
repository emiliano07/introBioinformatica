#!/usr/bin/env python3
import time

# DESAFIO IV

print("El Juego de la Vida")
time.sleep(2)
print("Bienvenido al juego interactivo en donde vas a aprender sobre expresión génica")
time.sleep(4)
print("Comencemos...")
time.sleep(2)

print("A partir de este momento usted es una cadena de ADN")
time.sleep(2)
print("Su objetivo en este mundo es lograr generar la proteina correspondiente para la cual usted codifica")
time.sleep(2)
print("Seleccione que tipo de cadena quiere ser:")
time.sleep(2)

sec1 = "GACGTTCAAGTC"
sec2 = "CTTGGCCAAGTA"
sec3 = "AGTACCATATGC"

print("1- " + sec1)
print("2- " + sec2)
print("3- " + sec3)
print("Elija la opción que desee y presione enter")

numero = input()

adn = ""
cond = True
while cond:
    if numero == "1":
        adn = sec1
        arn = "CUGCAAGUUCAG"
        cond = False
    elif numero == "2":
        adn = sec2
        arn = "GAACCGGUUCAU"
        cond = False
    elif numero == "3":
        adn = sec3
        arn = "UCAUGGUAUACG"
        cond = False
    else:
        print("Error: El valor ingresado no es correcto. Por favor ingrese uno correcto")
        numero = input()

print("--------------------")
print("Usted es la siguiente cadena de ADN: " + adn)
time.sleep(2)
print("Comienza su camino..")
time.sleep(2)
print("El primer paso que debe realizar es la transcripción")
time.sleep(2)
print("¿Donde quiere que vayamos a realizarla?")
time.sleep(2)

org1 = "Ribosomas"
org2 = "ARN Polimerasas"
org3 = "Mitocondias"

print("1- " + org1)
print("2- " + org2)
print("3- " + org3)
print("Elija la opción que desee y presione enter")

numero = input()

cond = True
while cond:
    if numero == "1":
        print("Tranquilo! Demasiado pronto para ir al Ribosoma ;)")
        print("Elijamos mejor otro camino")
        numero = input()
    elif numero == "2":
        print("Muy Bien!!! Las enzimas llamadas ARN polimerasas realizan la transcripción, estas unen nucleótidos para formar una cadena de ARN (usando una cadena de ADN como molde). La transcripción tiene tres etapas: iniciación, elongación y terminación")
        time.sleep(5)
        cond = False
    elif numero == "3":
        print("Por aquí no! Nos hemos desviado un poco de nuestro camino")
        print("Elijamos mejor otro camino")
        numero = input()
    else:
        print("Error: El valor ingresado no es correcto. Por favor ingrese uno correcto")
        numero = input()

print("--------------------")
print("Usted ha dejado de ser una cadena de ADN y ha pasado a ser una cadena ARN")
time.sleep(2)
print("Se ha realizado la siguitene transcripción:")
print("ADN: " + adn + " => ARN: " + arn)
time.sleep(2)
print("Tenga en cuenta que la transcripción se lleva a cabo de la siguiente forma:")
print("- Las Adeninas(A) se transcriben por Uracilos(U). Estos sustituyen a las Timinas(T), ya que en el ARN no existen")
print("- Las Timinas(T) se transcriben por Adeninas(A)")
print("- Las Citosinas(C) se transcriben por Guaninas(G)")
print("- Las Guaninas(G) se transcriben por Citosinas(C)")
time.sleep(5)

print("--------------------")
print("Usted ahora es la siguiente cadena de ARN: " + arn)
time.sleep(2)
print("Ahora debemos realizar la traducción")
time.sleep(2)
print("¿Quienes nos van a ayudar a realizarla?")
time.sleep(2)

org1 = "Ribosomas"
org2 = "ARN Polimerasas"
org3 = "Mitocondias"

print("1- " + org1)
print("2- " + org2)
print("3- " + org3)
print("Elija la opción que desee y presione enter")

numero = input()

cond = True
while cond:
    if numero == "1":
        print("Muy Bien!!! La traducción del ADN es el segundo proceso de la síntesis proteica. Ocurre en todos los seres vivos y tiene lugar en el citoplasma, lugar en donde se encuentran los ribosomas, que adquieren un papel fundamental en el proceso")
        time.sleep(5)
        cond = False
    elif numero == "2":
        print("Otra vez por aquí! La transcripción ya la hicimos ;)")
        print("Elijamos mejor otro camino")
        numero = input()
    elif numero == "3":
        print("Por aquí no! Nos hemos desviado un poco de nuestro camino")
        print("Elijamos mejor otro camino")
        numero = input()
    else:
        print("Error: El valor ingresado no es correcto. Por favor ingrese uno correcto")
        numero = input()

print("--------------------")
print("Tenga en cuenta que el ARN se separa de a tres nucleotidos, denominados codones. Cada uno de ellos corresponde a un aminoacido especifico")
time.sleep(2)
print("Los aminoácidos son moléculas que se combinan para formar proteínas.")
time.sleep(2)
print("--------------------")
print("Felicitaciones!!! Ha llegado al final del camino y ha conseguido generar la proteina correctamente")
time.sleep(2)
print("Espero que el camino haya sido de su agrado. Gracias!")
