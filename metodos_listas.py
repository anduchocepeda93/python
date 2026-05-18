lista = ["Andres","Cepeda",True,1.70,"Andres"]
lista2= list([-2,6,8,1.70,2])

cantidad_elementos = len(lista)
print(cantidad_elementos)

lista.append('jajajaja')

lista.insert(1,'Andres')

lista.extend([False,2002])

lista.pop(-3)

lista.remove('Andres')

#lista.clear()

#lista2.sort()

#lista2.sort(reverse=True)

lista2.reverse()

print(lista2)

