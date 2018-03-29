def forma_tabla(m): #funcion que crea un arreglo vacio de tamano m
	arreglo=[None]*m
	return arreglo

def hash(llave,m):
	suma=0
	for i in range(len(llave)):
		suma=suma+ord(llave[i])
	return suma%m

def agregar(llave,valor,tabla):
    llave_hash=hash(llave,len(llave))
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
        if llaveh==len(tabla):
            print("Tabla llena")
            break
        else:
            if tabla[llaveh] is None:
                tabla[llaveh]=list(ParllaveValor)
                return True

def buscar(llave,tabla):
    llave_hash=hash(llave,len(llave))
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

vec_inf=['987632','453462','453452','564753','568679','345476',
'879737','456479','436564','123346','645645','296372']

m=len(vec_inf)
tabla_H=forma_tabla(m)
for i in range(len(vec_inf)):
    agregar(vec_inf[i],i,tabla_H)

print("\n",tabla_H)

Resultado=buscar("296372",tabla_H)
print("\nResultado: ",Resultado)