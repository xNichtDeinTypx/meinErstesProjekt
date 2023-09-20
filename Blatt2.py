#Aufgabe 1:
import math

num = input("Hier die Zahl eingeben: ");
num = float (num);
if num<0:
    print("Nicht lösbar")
else:
    print(math.sqrt(num))

#Aufgabe2:
num1 = input("Hier den Umsatz des 1. Monats angeben: ")
num2 = input("Hier den Umsatz des 2. Monats angeben: ")
num3 = input("Hier den Umsatz des 3. Monats angeben: ")

num1 = float(num1);
num2 = float(num2);
num3 = float(num3);

numGes = num1+num2+num3;



print("Umsatz 1. Monat: ",num1)
print("Umsatz 2. Monat: ",num2)
print("Umsatz 3. Monat: ",num3)
print("Umsatz gesamt: ",numGes)
if numGes>1000:
    bonus = numGes*2/100;
    print("Der Bonus beträgt: ", bonus)


#Aufgabe3:
alterMitarbeiter = input("Hier bitte Alter eingeben: ")
alterMitarbeiter = float(alterMitarbeiter);
gradBehinderung = input("Geben Sie hier den Grad der Behinderung (in %) an: ")
gradBehinderung = float(gradBehinderung)
standardUrlaub = 30;

if alterMitarbeiter<18:
    print("Anzahl der Urlaubstage: ",standardUrlaub+5 )
elif alterMitarbeiter>55:
    print("Anzahl der Urlaubstage: ", standardUrlaub + 2)
else:
    print("Anzahl der Urlaubstage: ", standardUrlaub)


if gradBehinderung>50:
    print("Anzahl der Urlaubstage: ",standardUrlaub+5)

