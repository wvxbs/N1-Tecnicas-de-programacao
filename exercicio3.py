def main():
    valor_euro = 6.15
    n_euros = float(input('Quantos euros você quer comprar? ')) #não é possivel multiplicar um valor int por float.
    print(f'Você precisa de {valor_euro * n_euros} reais.'), #não é possivel concatenar float com string.


main()