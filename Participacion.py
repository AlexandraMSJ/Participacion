from collections import Counter

#Entrada del archivo
archivo = open('Gullivers_Travels.txt',encoding='utf-8')
mensaje = archivo.read()
#Contar los caracteres
def contar_carac(mensaje):
    contador = 0
    for linea in mensaje:
        for caracter in linea:
            contador += 1
    return contador
#Ordenar caracteres
def ordenar_caracteres(mensaje):
    carac_rep = Counter(mensaje)
    caracteres_ordenados = sorted(carac_rep.items(), key=lambda x: x[1], reverse=True)

    return caracteres_ordenados
carac_ord = ordenar_caracteres(mensaje)
conta = contar_carac(mensaje)
#Añadir a un archivo el resultado
with open('resultado.txt', 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.write(f"El numero de caracteres en el texto es: {conta}\n\n")
for caracter, frecuencia in carac_ord:
    archivo_salida.write(f"Caracter: {caracter}, Frecuencia: {frecuencia}\n")
