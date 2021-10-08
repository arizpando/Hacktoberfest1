x=int(input("opción= "))
espacios=x+2
if espacios >= 1:
    if (x%2)==0:
        for i in range(0,(espacios//2)-1):
            espacio=" "
            espacios-=2
            numEspac=(espacio*espacios)
            inicEspac=espacio*i
            print(inicEspac,"\\",numEspac,"/")
            for i in range(0,(espacios//2)-1,-1):
                espacio=" "
                espacios+=2
                numEspac=(espacio*espacios)
                inicEspac=espacio*i
                print(inicEspac,"/",numEspac,"\\")
    else:
        for i in range(0,(espacios//2)-1):
            espacio=" "
            espacios-=2
            numEspac=(espacio*espacios)
            inicEspac=espacio*i
            print(inicEspac,"\\",numEspac,"/")  
