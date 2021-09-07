from tools.ReceiveUserInput import ReceiveUserInput
from tools.ShowResult import ShowResult

def CalculateSquareArea(Side):
    Area = Side ** 2
    
    return Area

def main():
    Side = ReceiveUserInput("Informe o valor do lado do quadrado")
    Area = CalculateSquareArea(Side)

    ShowResult(f"A área do quadrado de lado {Side} é", Area)

main()