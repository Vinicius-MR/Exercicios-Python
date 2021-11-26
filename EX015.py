dias = int(input('Quantos dias ficou com o carro? '))
Km = float(input('Quantos Km rodados? '))
total = (dias*60)+(Km*0.15)
print(f'O total a pagar será de R${total:.2f}')
