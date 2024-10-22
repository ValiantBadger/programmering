import datetime

def berakna_kostnad():

    
    
    startdatum = input("Ange startdatum (YYYY-MM-DD): ")
    slutdatum = input("Ange slutdatum (YYYY-MM-DD): ")

    matar_start = int(input("mätarinställning vid startdatum: "))
    matar_slut = int(input("mätarinställning vid slutdatum: "))
    
    kostnad_per_kwh = int(input("kostnad öre/kWh: "))
    
    avgift = int(input("daglig avgift i öre: "))
    
    
    startdatum = datetime.datetime.strptime(startdatum, "%Y-%m-%d")
    slutdatum = datetime.datetime.strptime(slutdatum, "%Y-%m-%d")
    
  
    dagar_diff = (slutdatum - startdatum).days
    
    
    mät_diff = matar_slut - matar_start
    
    
    moms = 1.25  
    total_kost = ((dagar_diff * avgift) + (mät_diff * kostnad_per_kwh)) * moms
    
   
    print(total_kost)


berakna_kostnad()