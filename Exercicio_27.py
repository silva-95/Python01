#construa uma pagina/programa onde o usuario digitara uma numero,onde a pagina contara ate zero e depois ate o numero que o usuario digitou


n=int(input("Digite um numero."))
for i in range(n,-1,-1):
    print(i)
for i in range(n):
    print(i+1)


