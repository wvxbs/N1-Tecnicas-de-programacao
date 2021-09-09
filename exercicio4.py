#= é usado para atribuição e == é usado para compação

def Exemplo():
    atribuicao = "exemplo" #atribui "exemplo" á variável atribuição
    comparacao = "exemplo"

    if atribuicao == comparacao: #compara o valor das variáveis
        return True
    else:
        return False

def main(): 

    if Exemplo():
        print("Funcionou")
    else:
        print(":(")
main()