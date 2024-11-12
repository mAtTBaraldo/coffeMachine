import time
import os
somma2="*"
barra2="*"
k=15
ml=[30,120,120,20,30,45,30]
somma="*"
barra="*****"
acqua=500
#controllo riscaldamento
print("Aspetta che la macchinetta si riscaldi")
for i in range (1,30):
    somma2=somma2+barra2
    os.system('cls')
    print(30-i,"secondi rimanenti")
    print(somma2)
    time.sleep(1)
    os.system('cls')
print("la macchinetta è pronta")
#selezione bevande
n=10
for i in range (0,n+1):
    print ("Ciao! che cosa vuoi bere? ", u"\U0001F964")
    bevande=["1-caffe","2-the","3-cioccolata","4-espresso","5-decaffeinato","6-macchiato","7-premium"]
    for m in bevande:
        print (m)
    scelta=int(input("scegli la bevanda: "))
    while (scelta>7) or (scelta<1):
        scelta=int(input("ri-scegli la bevanda: "))
#CONTROLLO TAZZINA
    tazzina=input("hai inserito la tazzina? scrivi si per procedere: ")
    while tazzina != "si":
        print("verificare di aver inserito la tazzina")
        tazzina=input("hai inserito la tazzina? scrivi si per procedere: ")
#controllo scelta e fa la bevanda
    if scelta==1:
        t=ml[0]/k
        acqua=acqua-ml[0]
        while acqua<ml[0]:
            acqua2=int(input("inserisci acqua: "))
            acqua=acqua+acqua2
        while (acqua>500):
            print("la macchinetta ha sbordato")
            print("togliere acqua")
            acqua=acqua-acqua2
            print (t,"s")
        while t != 0:
            somma=somma+barra
            os.system('cls')
            print (somma)
            time.sleep(1)
            t=t-1
        print("la bevanda risulta essere pronta", u"\U0001F964")
        os.system('cls')
#da fare con elif altrimenti riscrive tutto
    if scelta==2:
        t=ml[1]/k
        acqua=acqua-ml[1]
        while acqua<ml[1]:
            acqua2=int(input("inserisci acqua: "))
            acqua=acqua+acqua2
            while (acqua>500):
                print("la macchinetta ha sbordato")
                print("togliere acqua")
                acqua2=int(input("togli l'acqua"))
                acqua=acqua-acqua2
            print (t,"s")
        while t != 0:
            somma=somma+barra
            os.system('cls')
            print (somma)
            time.sleep(1)
            t=t-1
        print("la bevanda risulta essere pronta",u"\U0001F964")
        os.system('cls')
    if scelta==3:
        t=ml[2]/k
        acqua=acqua-ml[2]
        while acqua<ml[2]:
            acqua2=int(input("inserisci acqua: "))
            acqua=acqua+acqua2
            while (acqua>500):
                print("la macchinetta ha sbordato")
                print("togliere acqua")
                acqua2=int(input("togli l'acqua"))
                acqua=acqua-acqua2
            print (t,"s")
        while t != 0:
            somma=somma+barra
            os.system('cls')
            print (somma)
            time.sleep(1)
            t=t-1
        print("la bevanda risulta essere pronta", u"\U0001F964")
        os.system('cls')
    if scelta==4:
        t=ml[3]/k
        acqua=acqua-ml[3]
        while acqua<ml[3]:
            acqua2=int(input("inserisci acqua: "))
            acqua=acqua+acqua2
            while (acqua>500):
                print("la macchinetta ha sbordato")
                print("togliere acqua")
                acqua2=int(input("togli l'acqua"))
                acqua=acqua-acqua2
            print (t,"s")
        while t != 0:
            somma=somma+barra
            os.system('cls')
            print (somma)
            time.sleep(1)
            t=t-1
        print("la bevanda risulta essere pronta", u"\U0001F964")
        os.system('cls')
    if scelta==5:
        t=ml[4]/k
        acqua=acqua-ml[4]
        while acqua<ml[4]:
            acqua2=int(input("inserisci acqua: "))
            acqua=acqua+acqua2
            while (acqua>500):
                print("la macchinetta ha sbordato")
                print("togliere acqua")
                acqua2=int(input("togli l'acqua"))
                acqua=acqua-acqua2
            print (t,"s")
        while t != 0:
            somma=somma+barra
            os.system('cls')
            print (somma)
            time.sleep(1)
            t=t-1
        print("la bevanda risulta essere pronta",u"\U0001F964")
        os.system('cls')
    if scelta==6:
        t=ml[5]/k
        print (t,"s")
        acqua=acqua-ml[5]
        while acqua<ml[5]:
            acqua2=int(input("inserisci acqua: "))
            acqua=acqua+acqua2
            while (acqua>500):
                print("la macchinetta ha sbordato")
                print("togliere acqua")
                acqua2=int(input("togli l'acqua"))
                acqua=acqua-acqua2
        while t != 0:
            somma=somma+barra
            os.system('cls')
            print (somma)
            time.sleep(1)
            t=t-1
        print("la bevanda risulta essere pronta",u"\U0001F964")
        os.system('cls')
    if scelta==7:
        t=ml[6]/k
        print (t,"s")
        acqua=acqua-ml[6]
        while acqua<ml[6]:
            acqua2=int(input("inserisci acqua: "))
            acqua=acqua+acqua2
            while (acqua>500):
                print("la macchinetta ha sbordato")
                print("togliere acqua")
                acqua2=int(input("togli l'acqua"))
                acqua=acqua-acqua2
        while t != 0:
            somma=somma+barra
            os.system('cls')
            print (somma)
            time.sleep(1)
            t=t-1
        print("la bevanda risulta essere pronta",u"\U0001F964")
        os.system('cls')
    if n>10:
        print("la macchinetta è piena, svuotarla")
        print("vuoi svuotare la macchinetta")
        n=0
        print("macchinetta vuota")