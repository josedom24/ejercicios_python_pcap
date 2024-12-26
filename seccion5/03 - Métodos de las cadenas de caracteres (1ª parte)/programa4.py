texto = """Una variante del lorem ipsum ordinario
se utiliza en la composición tipográfica desde los años sesenta 
o antes, cuando se popularizó por los anuncios 
de las hojas de transferencia Letraset. Se introdujo en 
en la era de la información a mediados de los ochenta por Aldus Corporation, 
que lo empleó en plantillas gráficas y de tratamiento de textos
para su programa de autoedición PageMaker (de Wikipedia)"""

encontrado = texto.find('de')
while encontrado != -1:
    print(encontrado)
    encontrado = texto.find('de', encontrado + 1)