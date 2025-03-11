import random

Kort = ['E','2','3','4','5','6','7','8','9','10','J','D','K',
'E','2','3','4','5','6','7','8','9','10','J','D','K',
'E','2','3','4','5','6','7','8','9','10','J','D','K',
'E','2','3','4','5','6','7','8','9','10','J','D','K']

spelare1 = []
spelare2 = []
spelare3 = []
 
spelare1_poäng = 0
spelare2_poäng = 0 
spelare3_poäng = 0



def dela_ut_kort():
    random.shuffle(Kort)
    for _ in range(4):
        spelare1.append(Kort.pop())
        spelare2.append(Kort.pop())
        spelare3.append(Kort.pop())

def kolla_fyra_av_samma(spelare):
    poäng = 0
    for kort in set(spelare):  
        if spelare.count(kort) == 4:
            poäng += 1 
            for _ in range(4): 
                spelare.remove(kort)

def fråga_om_kort(frågande_spelare, tillfrågad_spelare, kort_frågat):
    if kort_frågat in tillfrågad_spelare:
        print(f"{frågande_spelare} får kortet {kort_frågat} från {tillfrågad_spelare}.")
        tillfrågad_spelare.remove(kort_frågat)
        frågande_spelare.append(kort_frågat)
        return True
    else:
        print(f"{kort_frågat} finns inte i {tillfrågad_spelare}, finns i sjön.")
        if Kort:  
            nytt_kort = Kort.pop()
            print(f"{frågande_spelare} drar ett kort från högen: {nytt_kort}.")
            frågande_spelare.append(nytt_kort)
        return False
    
def välj_ai_kort(spelare):
    kort_frekvens = {}
    
    for kort in spelare:
        if kort not in kort_frekvens:
            kort_frekvens[kort] = 1
        else:
            kort_frekvens[kort] += 1
    
    mest_frekventa_kort = max(kort_frekvens, key=kort_frekvens.get)

    if list(kort_frekvens.values()).count(kort_frekvens[mest_frekventa_kort]) > 1:
        mest_frekventa_kort = random.choice([kort for kort, frek in kort_frekvens.items() if frek == kort_frekvens[mest_frekventa_kort]])

    return mest_frekventa_kort

def kolla_fyra_av_samma(spelare):
    poäng = 0
    for kort in set(spelare):  
        if spelare.count(kort) == 4:
            poäng += 1 
            for _ in range(4): 
                spelare.remove(kort)
    return poäng

def räkna_poäng():
    global spelare1_poäng, spelare2_poäng, spelare3_poäng
    spelare1_poäng += kolla_fyra_av_samma(spelare1)
    spelare2_poäng += kolla_fyra_av_samma(spelare2)
    spelare3_poäng += kolla_fyra_av_samma(spelare3)

def spela_med_användare():
    global spelare1_poäng, spelare2_poäng, spelare3_poäng
    dela_ut_kort()  
    spelare = ['spelare1', 'spelare2', 'spelare3']
    
    while spelare1_poäng + spelare2_poäng + spelare3_poäng < 13:
        for spelare_namn in spelare:
            print(f"\n{spelare_namn}'s tur!")
            
            if spelare_namn == 'spelare1':  
                print(f"Din hand: {spelare1}")
                kort_frågat = input("Välj ett kort att fråga om: ")

                
                if kort_frågat in spelare1:
                    tillfrågad_spelare = random.choice([spelare2, spelare3])
                    fråga_om_kort(spelare1, tillfrågad_spelare, kort_frågat)
                else:
                    print(f"Du har inte kortet {kort_frågat} i din hand.")
            
            elif spelare_namn == 'spelare2': 
                frågande_spelare, tillfrågad_spelare = spelare2, random.choice([spelare1, spelare3])
                kort_frågat = välj_ai_kort(frågande_spelare)
                print(f"(spelare2) frågar om kortet: {kort_frågat}.")
                fråga_om_kort(frågande_spelare, tillfrågad_spelare, kort_frågat)
            
            else:  
                frågande_spelare, tillfrågad_spelare = spelare3, random.choice([spelare1, spelare2])
                kort_frågat = välj_ai_kort(frågande_spelare)
                print(f"(spelare3) frågar om kortet: {kort_frågat}.")
                fråga_om_kort(frågande_spelare, tillfrågad_spelare, kort_frågat)
            
            räkna_poäng()  
            print(f"Poäng - Spelare 1: {spelare1_poäng}, Spelare 2: {spelare2_poäng}, Spelare 3: {spelare3_poäng}")

        if spelare1_poäng + spelare2_poäng + spelare3_poäng >= 13:
            break 

    
    if spelare1_poäng > spelare2_poäng and spelare1_poäng > spelare3_poäng:
        print("\nDu vann")
    elif spelare2_poäng > spelare1_poäng and spelare2_poäng > spelare3_poäng:
        print("\nSpelare 2 vann")
    elif spelare3_poäng > spelare1_poäng and spelare3_poäng > spelare2_poäng:
        print("\nSpelare 3 vann")
    else:
        print("\nDet blev oavgjort")

spela_med_användare()

