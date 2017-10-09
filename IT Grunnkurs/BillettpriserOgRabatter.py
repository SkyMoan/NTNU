dagerTilReise = int(input("Hvor mange dager er det til du skal reise?"))

def prisCalc (x):
    if x >= 14:
        pris = 199
    else:
        pris = 440

    return pris


result = prisCalc(dagerTilReise)

if result == 199:
    print("Denne billetten til minipris kan ikke refunderes")
    svar = input("Ønsker du fortsatt denne biletten? (J/N)")


    if svar == "J":
        print("Prisen for reisen din: "+ str(result) + ",-")


    else:
        print("Da tillbyr vi fullpris: 440,-")


else:
    print("Prisen for reisen din er 440,-")