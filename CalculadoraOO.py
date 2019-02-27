from calculadoraClass import Calculadora

operacao = float(input("Qual operacao voce quer fazer ?\n(1) Soma\n(2) Subtracao\n(3) Multiplicacao\n(4) Divisao\n"))
c = Calculadora()
if (operacao==1):
    numeroUm=float(input("Digite um numero:\n"))
    numeroDois=float(input("Certo, agora digite outro numero\n"))
    print("O resultado de sua operacao e ",c.soma(numeroUm,numeroDois))

elif (operacao==2):
    numeroUm=float(input("Digite um numero:\n"))
    numeroDois=float(input("Certo, agora digite outro numero\n"))
    print("O resultado de sua operacao e ",c.subtrai(numeroUm,numeroDois))
elif (operacao==3):
    numeroUm=float(input("Digite um numero:\n"))
    numeroDois=float(input("Certo, agora digite outro numero\n"))
    print("O resultado de sua operacao e ",c.multiplica(numeroUm,numeroDois))
elif (operacao==4):
    numeroUm=float(input("Digite um numero:\n"))
    numeroDois=float(input("Certo, agora digite outro numero\n"))
    print("O resultado de sua operacao e ",c.divide(numeroUm,numeroDois))
print ("\n FINAL DO PROGRAMA !")