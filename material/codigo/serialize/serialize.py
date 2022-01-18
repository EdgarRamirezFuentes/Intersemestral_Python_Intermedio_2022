import pickle 

lenguajes = ["Python", "Java", "C", "C++"] #coleccion

#Serializacion
with open('lenguajes','wb') as archivo_b:  #1
    #dump(contenido,destino) el destino puede ser una variable
    pickle.dump(lenguajes,archivo_b) #dump metodo que toma el texto y lo descompone quitando el contexto de python
    archivo_b.close()#cerrar como buenas practicas


#Deserializacion
archivo_python=open('lenguajes','rb') #2 
# 1 y 2 equivalentes
info_python=pickle.load(archivo_python)
print(info_python)