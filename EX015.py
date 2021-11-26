#O carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias alugados? '))
Km = float(input('Quantos Km rodados? '))
total = (Km*0.15)+(dias*60)
print(f'O total a pagar é de R${total:.2f}')
