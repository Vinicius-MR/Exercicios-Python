salario = float(input('Qual é o salário do Funcionário? R$'))
porcentagem = int(input('Qual será a porcentagem do aumento? '))
aumento = salario + (salario*porcentagem/100)
print(f'Um funcionário que ganhava R${salario:.2f}, com {porcentagem}% de aumento, passa a receber R${aumento:.2f}')
