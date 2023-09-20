#Aufgabe 1a: Der Text "Hallo Welt" soll asugegeben werden.
print("Hello World")

#Aufgabe 1b: Der Anwender gibt eine Zahl ein und das Programm gibt diese Zahl wieder aus
num = input("Hier die Zahl eingeben: ")
print(num)

#Aufgabe 1b: Der Anwender gibt einen Satz ein und das Programm gibt diesen Satz wieder aus
sentence = input("Hier den Satz eingeben: ")
print(sentence)

#Aufgabe 1c,d: Der Anwender gibt zwei Zahlen ein und das Programm gibt die Summe aus
num1 = input("Hier bitte die erste Zahl eingeben: ")
num2 = input("Hier bitte die zweite Zahl eingeben: ")
sum = int (num1)+ int (num2)
print ("Die Summe ist: ", sum)

#Aufgabe 2b: Mithilfe vom Satz des Pythagoras die Hypotenuse berechnen
import math

katOne = input("katheter 1: ")
katTwo = input("katheter 2: ")

katOne = float(katOne)
katTwo = float(katTwo)

hypotenuse = (katOne ** 2) + (katTwo ** 2)
print(math.sqrt(hypotenuse))
#Aufgabe 3b: Der Anwender gibt zwei Zahlen ein und das Programm gibt die größere Zahl an
num1 = input("Hier bitte die erste Zahl eingeben: ")
num2 = input("Hier bitte die zweite Zahl eingeben: ")

if (num1>num2):
    print("Die größere Zahl ist: ",num1)
else:
    print("Die größere Zahl ist: ",num2)