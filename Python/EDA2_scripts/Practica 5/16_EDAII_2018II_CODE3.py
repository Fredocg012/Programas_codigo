def agregar(llave,valor,tabla):
    llave_hash=1
    ParllaveValor=[llave,valor]
    if tabla[llave_hash] is None:
        tabla[llave_hash]=list(ParllaveValor)
        return True
    else:
        i=0
        for par in tabla[llave_hash]:
            if par==llave:
                i+=1
                continue
            if par==valor:
                i+=1
            if i==2:
                return True
    for j in range(len(tabla)):
        llaveh=(llave_hash+j)%13
        if llaveh>=len(tabla):
            print("Tabla llena",llave_hash)
            break
        else:
            if tabla[llaveh] is None:
                tabla[llaveh]=list(ParllaveValor)
                return True

tabla=[None,None,None,None,None,None,None,None,None,
None,None,None,None]
agregar("JESUS9",0,tabla)
print(tabla)