real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.51
euro = real / 6.38
libra = real / 7.44
iene = real / 0.049
print(f'Com R${real} você pode comprar: \nUS${dolar:.2f} dólares\n€{euro:.2f} euros\n£{libra:.2f} libra esterlina\n¥{iene:.2f} ienes')
