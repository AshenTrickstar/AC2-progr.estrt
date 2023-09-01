def pagamento(salario_hora, horas_trabalhadas):
    
    return salario_hora * horas_trabalhadas

salario_hora = int(input("O salário por hora é "))
horas_trabalhadas = float(input("As horas trabalhadas foram "))
print(pagamento(salario_hora, horas_trabalhadas))