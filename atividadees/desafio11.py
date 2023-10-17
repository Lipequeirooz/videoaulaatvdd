#largura e altura de uma parede , calcule a area e a quantidade de tinta para pintar cada litro de tinta
#pinta 2m²
larg = float(input('digite a largura em metros da sua parede'))
alt = float(input('digite a altura em metros da sua parede'))
area = larg * alt
print(f' a altura da sua parede {alt} e a largura {larg} que da {area}m²')
tinta = area / 2
print (f' serão necessários {tinta} litros de tinta')