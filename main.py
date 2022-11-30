import os
import random

print ("██╗     ██╗   ██╗ ██████╗ █████╗ ███████╗    ██████╗  █████╗ ████████╗ █████╗     ███████╗██╗  ██╗███████╗ ██████╗██╗   ██╗████████╗ ██████╗ ██████╗ ")
print ("██║     ██║   ██║██╔════╝██╔══██╗██╔════╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗    ██╔════╝╚██╗██╔╝██╔════╝██╔════╝██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗")
print ("██║     ██║   ██║██║     ███████║███████╗    ██║  ██║███████║   ██║   ███████║    █████╗   ╚███╔╝ █████╗  ██║     ██║   ██║   ██║   ██║   ██║██████╔╝")
print ("██║     ██║   ██║██║     ██╔══██║╚════██║    ██║  ██║██╔══██║   ██║   ██╔══██║    ██╔══╝   ██╔██╗ ██╔══╝  ██║     ██║   ██║   ██║   ██║   ██║██╔══██╗")
print ("███████╗╚██████╔╝╚██████╗██║  ██║███████║    ██████╔╝██║  ██║   ██║   ██║  ██║    ███████╗██╔╝ ██╗███████╗╚██████╗╚██████╔╝   ██║   ╚██████╔╝██║  ██║")
print ("╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
print()
print (" █████╗ ███╗   ██╗██████╗      ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ ")
print ("██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗")
print ("███████║██╔██╗ ██║██║  ██║    ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝")
print ("██╔══██║██║╚██╗██║██║  ██║    ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗")
print ("██║  ██║██║ ╚████║██████╔╝    ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║")
print ("╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝      ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")

print()
print()
print()
print ("Sehr geehrter", os.getlogin(), "dies ist ein Dataexecuter. Bitte pass auf während Ihre Daten verarbeitet werden!")

Zahl1 = int(0)
Zahl2 = 0
RechenopreatorFloat = "+"
StringConvert = "None"
StringConvertOperator = "uppercase"
StringFind = "Hallo"
IntZahl1 = 0
IntZahl2 = 0
RechenopreatorInt = "+"
ConvertType = "float"
ConvertString = "String"
ConvertFloat = 0.0
ConvertNumber = 0

def Abfrage():
    ExecuterAbfrage = str(input("Wählen Sie eine der möglichen Verarbeitungsmöglichkeiten. Möglich sind: float, String, Number, random, convert\n"))
    AbfrageBestanden = 0
    global Zahl1
    global Zahl2
    global RechenopreatorFloat
    global RechenopreatorInt
    global StringConvert
    global StringConvertOperator
    global StringFind
    global IntZahl1
    global IntZahl2
    global ConvertType
    global ConvertString
    global ConvertFloat
    global ConvertNumber 
    
    while AbfrageBestanden == 0:
        if ExecuterAbfrage.lower().startswith("f"):
            FloatExecuter = str(input("Wollen Sie eine Kommazahl verarbeiten? [Ja / Nein]\n"))
            if FloatExecuter.lower().startswith("j"):
                print ("Zulässige Zeichen sind:\n +, -, *, /\n")
                RechenopreatorFloat = str(input("Wählen Sie einen Rechenopreator.\n"))
                Zahl1 = float(input("Wählen Sie ihre erste Zahl.\n"))
                Zahl2 = float(input("Wählen Sie ihre zweite Zahl.\n"))
                print("Ihre Verarbeitung beginnt nun!")
                AbfrageBestanden = AbfrageBestanden + 1
                RunFloatExecuter()
            elif FloatExecuter.lower().startswith("n"):
                print(os.getlogin(), ", das Programm wird gestoppt!")
                exit()
        elif ExecuterAbfrage.lower().startswith("f"):
            NumberExecuter = str(input("Wollen Sie einen Integer verarbeiten? [Ja / Nein]\n"))
            if NumberExecuter.lower().startswith("j"):
                print ("Zulässige Zeichen sind:\n +, -, *, /\n")
                RechenopreatorInt = str(input("Wählen Sie ihren Rechenoperator.\n"))
                IntZahl1 = int(input("Geben Sie ihr erste Zahl ein.\n"))
                IntZahl2 = int(input("Geben Sie ihr zweite Zahl ein.\n"))
                print("Ihre Verarbeitung beginnt nun!")
                AbfrageBestanden = AbfrageBestanden + 1
                RunIntExecutor()
            elif NumberExecuter.lower().startswith("n"):
                print(os.getlogin(), "das Programm wird nun gestoppt!")
                exit()
        elif ExecuterAbfrage.lower().startswith("s"):
            StringExecuter = str(input("Wollen Sie einen String konvertieren?  [Ja / Nein]\n"))
            if StringExecuter.lower().startswith("j"):
                StringConvert = str(input("Geben Sie ihren String ein, welchen Sie konvertieren möchten.\n"))
                StringConvertOperator = str(input("Geben Sie einen Operator zur Textverarbeitung an. Mögliche Operatoren sind:\n lowercase \n uppercase\n find\n swap\n"))
                if StringConvertOperator == "find":
                    StringFind = str(input("Nach welchem Wort sollen wir suchen?\n"))
                    print("Ihre Verarbeitung beginnt nun!")
                    RunStringExecuter()
                elif StringFind != "find":
                    print("Ihre Verarbeitung beginnt nun!")
                RunStringExecuter()
            elif StringExecuter.lower().startswith("n"):
                print(os.getlogin(), ", das Programm wird gestoppt!")
                exit()
            AbfrageBestanden = AbfrageBestanden + 1
        elif ExecuterAbfrage.lower().startswith("r"):
            RandomZahl1= int(input("Geben Sie eine Zahl ein!\n"))
            RandomZahl2 = int(input("Geben Sie eine weitere Zahl ein!\n"))
            print("Ihre Zufallszahl ist: ",random.randint(RandomZahl1, RandomZahl2))
            AbfrageBestanden = AbfrageBestanden + 1
            exit()
        elif ExecuterAbfrage.lower().startswith("c"):
            ConvertExecutor = str((input("Wollen Sie einen Wert konvertieren?  [Ja / Nein]\n")))
            if ConvertExecutor.lower().startswith("j"):
                ConvertType = str(input("Geben Sie den Typ an, welchen Sie konvertieren wollen. Möglich sind: \n float [konvertiert in einen Integer (ganze Zahl)]\n Integer [konvertiert in einen float (Kommazahl)]\n String [Überprüfung auf Zahlen (digit)\n"))
                if ConvertType.lower() == "float":
                    ConvertFloat = float(input("Geben Sie ihre Kommazahl ein.\n"))
                    print ("Ihr Datentyp wird nun konvertiert. Ihr eingegebener Wert ist:\n", ConvertFloat)
                    AbfrageBestanden = AbfrageBestanden + 1
                    RunConvert()
                elif ConvertType == "Integer" or ConvertType == "integer":
                    ConvertNumber == int(input("Geben Sie ihren Integer ein.\n"))
                    print ("Ihr Datentyp wird nun konvertiert. Ihr eingegebener Wert ist:\n", ConvertNumber)
                    AbfrageBestanden = AbfrageBestanden + 1
                    RunConvert()
                elif ConvertType.lower() == "String" or ConvertType == "string":
                    ConvertString = str(input("Geben Sie ihren String ein, welcher überprüft werden soll.\n"))
                    print ("Ihr Datentyp wird nun konvertiert. Ihr eingegebener Wert ist:\n", ConvertString)
                    AbfrageBestanden = AbfrageBestanden + 1
                    RunConvert()
            elif ConvertExecutor.lower().startswith("n"):
                print(os.getlogin(), ", das Programm wird gestoppt!")
                exit()

def RunFloatExecuter():
    global Zahl1
    global Zahl2
    global RechenopreatorFloat

    if RechenopreatorFloat == "+":
        print("Ihr Ergebnis beträgt: \n", float(Zahl1 + Zahl2))
    elif RechenopreatorFloat == "-":
        print("Ihr Ergebnis beträgt: \n", float(Zahl1 - Zahl2))
    elif RechenopreatorFloat == "*":
        print("Ihr Ergebnis beträgt: \n", float(Zahl1 * Zahl2))
    elif RechenopreatorFloat == "/":
        print("Ihr Ergebnis beträgt: \n", float(Zahl1 / Zahl2))
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
        print("Die Postion an der sich Ihr Wort befindet ist:\n" , StringConvert.find(StringFind))

def RunIntExecutor():
    global IntZahl1
    global IntZahl2
    global RechenopreatorInt
    
    if RechenopreatorInt == "+":
        print ("Ihr Ergebnis beträgt: \n", int(IntZahl1 + IntZahl2))
    elif RechenopreatorInt == "-":
        print ("Ihr Ergebnis beträgt: \n", int(IntZahl1 + IntZahl2))
    elif RechenopreatorInt == "*":
        print ("Ihr Ergebnis beträgt: \n", int(IntZahl1 * IntZahl2))
    elif RechenopreatorInt == "/":
        print ("Ihr Ergebnis beträgt: \n", int(IntZahl1 / IntZahl2))
    else:
        Abfrage()
    
def RunConvert():
    global ConvertType
    global ConvertString
    global ConvertFloat
    global ConvertNumber

    if ConvertType == "float" or ConvertType == "Float":
        ConvertFloat = int(ConvertFloat)
        ConvertFloat = print("Ihr Ergebnis beträgt: \n",ConvertFloat)
    elif ConvertType == "Integer" or ConvertType == "integer":
        ConvertNumber = float(ConvertNumber)
        ConvertNumber = print("Ihr Ergebnis beträgt: \n", ConvertNumber)
    elif ConvertType == "String" or ConvertType == "string":
        if ConvertString.isdigit() == True:
            print(str("Ihr String enthält zahlen!"))
        elif ConvertType.isdigit() == False:
            print ("Ihr String enthält keine Zahlen")

Abfrage()