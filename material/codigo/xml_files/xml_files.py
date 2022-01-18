import xml.etree.ElementTree as ET

miarbol=ET.parse('./xml_file.xml')

miraiz=miarbol.getroot()

print(miraiz.tag)

#Subconjunto
print(miraiz[0].tag)
print(miraiz[1].tag)

#Se recorre la primera etiqueta animal
for i in miraiz[0]:
	#tag retorna nombre de la etiqueta
	#text el contenido de dicha etiqueta
	print(i.tag+': '+i.text)

for i in miraiz.findall('animal'):
	#En todas las etiquetas de animal
	nombre=i.find('nombre').text
	edad=i.find('edad').text
	#Extraer valor de nombre y edad
	print(nombre,edad)

#Recorrer mi raiz hasta encontrar la etiqueta nombre
for i in miraiz.iter('nombre'):
	#Si existe un nombre de Michi cambiarlo por el valor de 'cambio'
	if i.text=='Michi':
		cambio='Yeison'
		i.text=str(cambio)

#Crea un archivo nuevo
miarbol.write('nuevo.xml')
