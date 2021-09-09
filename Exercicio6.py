from tools.ReceiveNumericUserInput import ReceiveNumericUserInput
from tools.ReceiveUserInput import ReceiveUserInput
from tools.ShowResult import ShowResult

def CalcularCircunferencia(Raio, Pi):
    Resultado = 2 * Pi * Raio

    return Resultado 

def CalcularArea(Raio, Pi):
    Resultado = Pi* Raio * Raio

    return Resultado 

def circunferencia_ou_area(Raio, Operacao = "c"):
    Pi = 3.14

    if Operacao == "c":
        return CalcularCircunferencia(Raio, Pi)
    else:
        return CalcularArea(Raio, Pi)

def main():
    while(True):

        Raio = ReceiveNumericUserInput("Insira o valor do raio")
        DesejaCalcularArea = ReceiveUserInput("Deseja calcular a área?")

        if DesejaCalcularArea.lower() == "sim":
            ShowResult("A área é",circunferencia_ou_area(Raio, DesejaCalcularArea))
            
        elif DesejaCalcularArea.lower() == "nao" or DesejaCalcularArea.lower() == "não":
            ShowResult("A circunferência é", circunferencia_ou_area(Raio))

        else:
            ShowResult("Resposta inválida", DesejaCalcularArea)


main()