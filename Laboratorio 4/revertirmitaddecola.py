'''
Escribir una función que tome una cola y revierta la mitad de sus elementos utilizando solo una pila
adicional.
La cola debe mantener la misma secuencia de elementos, pero la mitad debe estar en orden inverso.
'''
from collections import deque

def revertir_mitad_cola(cola):
    pila = []

    longitud = len(cola)
    mitad = longitud // 2
    
    # Transferir la mitad de la cola a la pila
    for _ in range(mitad):
        pila.append(cola.popleft())
    
    # Transferir la mitad de la pila a la cola en orden inverso
    for _ in range(mitad):
        pila.append(cola.pop())

    
    if longitud % 2 != 0:
        cola.append(pila.pop())

    while pila:
        cola.appendleft(pila.pop())

    return cola


en_cola = deque([2,4,6,8,10,12,14])
print("Cola original:", en_cola)
en_cola = revertir_mitad_cola(en_cola)
print("Cola con la mitad revertida:", en_cola)