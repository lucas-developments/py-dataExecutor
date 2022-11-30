import os
import random

print ("Sehr geehrter", os.getlogin(), "dies ist ein Dataexecuter. Bitte pass auf während deine Daten verarbeitet werden!")

Zahl1 = int(0)
Zahl2 = 0
RechenopreatorFloat = "+"
StringConvert = "None"
StringConvertOperator = "uppercase"
StringFind = "Hallo"

def Abfrage():
    ExecuterAbfrage = str(input("Wählen Sie eine der möglichen Verarbeitungsmöglichkeiten. Möglich sind: float, String, Number, random\n"))
    AbfrageBestanden = 0
    global Zahl1
    global Zahl2
    global RechenopreatorFloat
    global StringConvert
    global StringConvertOperator
    global StringFind

    while AbfrageBestanden == 0:
        if ExecuterAbfrage == "float":
            FloatExecuter = str(input("Wollen Sie eine Kommazahl verarbeiten? [Ja / Nein]\n"))
            if FloatExecuter.lower().startswith("j"):
                print ("Zulässige Zeichen sind:\n +, -, *, /\n")
                RechenopreatorFloat = str(input("Wählen Sie einen Rechenopreator.\n"))
                Zahl1 = int(input("Wählen Sie ihre erste Zahl.\n"))
                Zahl2 = int(input("Wählen Sie ihre zweite Zahl.\n"))
                AbfrageBestanden = AbfrageBestanden + 1
                RunFloatExecuter()
            elif FloatExecuter.lower().startswith("n"):
                print(os.getlogin(), ", das Programm wird gestoppt!")
                exit()
        elif ExecuterAbfrage == "Number":
            NumberExecuter = int(input("Falls Sie eine Zahl verarbeiten möchten, nutzen Sie bitte diese Option!\n"))
            AbfrageBestanden = AbfrageBestanden + 1
        elif ExecuterAbfrage == "String":
            StringExecuter = str(input("Wollen Sie einen String konvertieren?  [Ja / Nein]\n"))
            if StringExecuter.lower().startswith("ja"):
                StringConvert = str(input("Geben Sie ihren String ein, welchen Sie konvertieren möchten.\n"))
                StringConvertOperator = str(input("Geben Sie einen Operator zur Textverarbeitung an. Mögliche Operatoren sind:\n lowercase \n uppercase\n find\n swap\n"))
                if StringConvertOperator == "find":
                    StringFind = str(input("Nach welchem Wort sollen wir suchen?\n"))
                    print("Ihre Verarbeitung beginnt nun!")
                    RunStringExecuter()
                else:
                    print("Ihre Verarbeitung beginnt nun!")
                RunStringExecuter()
            elif StringExecuter.lower().startswith("n"):
                print(os.getlogin(), ", das Programm wird gestoppt!")
                exit()
            AbfrageBestanden = AbfrageBestanden + 1
        elif ExecuterAbfrage == "random":
            RandomZahl1= int(input("Geben Sie eine Zahl ein!\n"))
            RandomZahl2 = int(input("Geben Sie eine weitere Zahl ein!\n"))
            print(random.randint(RandomZahl1, RandomZahl2))
            AbfrageBestanden = AbfrageBestanden + 1

def RunFloatExecuter():
    global Zahl1
    global Zahl2
    global RechenopreatorFloat

    if RechenopreatorFloat == "+":
        print(float(Zahl1 + Zahl2))
    elif RechenopreatorFloat == "-":
        print(float(Zahl1 - Zahl2))
    elif RechenopreatorFloat == "*":
        print(float(Zahl1 * Zahl2))
    elif RechenopreatorFloat == "/":
        print(float(Zahl1 / Zahl2))
    else:
        Abfrage()

def RunStringExecuter():
    global StringConvert
    global StringConvertOperator
    global StringFind

    if StringConvertOperator == "lowercase":
        print (StringConvert.lower())
    elif StringConvertOperator == "uppercase":
        print(StringConvert.upper())
    elif StringConvertOperator == "swap":
        print(StringConvert.swapcase())
    elif StringConvertOperator == "find":
        print("Die Postion an der sich dein Wort befindet ist:" , StringConvert.find(StringFind))

Abfrage()