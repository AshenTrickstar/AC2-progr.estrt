#Exercício 4

ano = int(input("Informe o ano: "))

anocerto = (ano % 4 == 0 and ano %  100 != 0 or ano % 400 == 0)

resposta = "O ano informado é bissexto" if  anocerto else " O ano informado não é bissexto"

print(resposta)