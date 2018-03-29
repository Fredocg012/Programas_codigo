def buscar(llave,tabla):
    llave_hash=1
    if tabla[llave_hash] is not None:
        for par in tabla[llave_hash]:
            if par==llave:
                return (tabla[llave_hash][1])
            else:
                for j in range(len(tabla)):
                    llaveh=(llave_hash+j)%13
                    if llaveh==len(tabla):
                        break
                    for par1 in tabla[llaveh]:
                        if par1==llave:
                            return (tabla[llaveh][1])
    return None

tabla=[None,["JESUS9",5],None,None,None,None,None,None,
None,None,None,None,None]
print("Resultado: ",buscar("JESUS9",tabla))