import random

def spel_runda():
    alt = ["sten","sax","påse"]
    motståndare_val = random.choice(alt)

    ditt_val = input("Välj: sten, sax eller påse: ")

    print(f"ditt val: {ditt_val}")
    print(f"motståndare: {motståndare_val}")

    if ditt_val == motståndare_val:
        print ("lika")
        return 0
    elif(ditt_val== "sten" and motståndare_val == "sax" or 
         ditt_val == "sax" and motståndare_val == "påse" or 
         ditt_val == "påse" and motståndare_val == "sten"):
        print("poäng till dig")
        return 1
    elif(ditt_val== "sten" and motståndare_val == "påse" or 
         ditt_val== "sax" and motståndare_val == "sten" or 
         ditt_val== "påse" and motståndare_val == "sax"):
        print("poäng till motståndare")
        return -1
    else:
        print("funker inte försök igen")
        return None

def main():
    dina_poäng = 0
    motståndares_poäng = 0

    while dina_poäng < 3 and motståndares_poäng < 3:
        resultat = spel_runda()
        if resultat == 1:
            dina_poäng += 1
        elif resultat == -1:
            motståndares_poäng += 1

    if dina_poäng == 3:
        print("du vann")
    elif motståndares_poäng == 3:
        print("Motståndaren vann")


if __name__ == "__main__":
    main()