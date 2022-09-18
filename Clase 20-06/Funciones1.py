#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Taller 3
#Primer enunciado

def modificar_pos_impares(lista):
    for i in range(1,len(lista),2):
        lista[i] = lista[i] - lista[i-1]
    return lista

numerolista = [1,8,6,4,5,7,3,2]

#print(modificar_pos_impares(numerolista))


# In[7]:


#Segundo enunciado

def modificar_multiplo(lista):
    for i in range(1,len(lista)):
        if lista[i] % 7 == 0:
            lista[i] = lista[i] + lista[len(lista)-1]
    return lista

nuevalista = [1,14,6,49,5,7,3,2]

#print(modificar_multiplo(nuevalista))


# In[8]:


#Tercer enunciado

def crear_lista():
    continuar = True
    lista = []
    while(continuar):
        num = int(input("Ingrese un numero < 500 (Para salir ingrese -1): "))
        if(num < 0):
            continuar = False
        elif num < 500:
            lista.append(num)
        else:
            print("Error el numero debe ser < 500 !!!")
    return lista

#print(crear_lista())


# In[ ]:


#Cuarto enunciado

