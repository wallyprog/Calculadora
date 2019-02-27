operacao = float(input("Qual operacao voce quer fazer ?\n(1) Soma\n(2) Subtracao\n(3) Multiplicacao\n(4) Divisao\n"))

if (operacao==1):
    numeroUm=float(input("Digite um numero\n"))
    numeroDois=float(input("Certo, agora digite outro numero\n"))
    resultado = numeroUm+numeroDois
    print("O resultado de sua operacao e ",resultado)

elif (operacao==2):
    numeroUm=float(input("Digite um numero\n"))
    numeroDois=float(input("Certo, agora digite outro numero\n"))
    resultado = numeroUm-numeroDois
    print("O resultado de sua operacao e ",resultado)
elif (operacao==3):
    numeroUm=float(input("Digite um numero\n"))
    numeroDois=float(input("Certo, agora digite outro numero\n"))
    resultado = numeroUm*numeroDois
    print("O resultado de sua operacao e ",resultado)
elif (operacao==4):
    numeroUm=float(input("Digite um numero\n"))
    numeroDois=float(input("Certo, agora digite outro numero\n"))
    resultado = numeroUm/numeroDois
    print("O resultado de sua operacao e ",resultado)
print ("\n FINAL DO PROGRAMA !")
