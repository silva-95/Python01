# construa uma pagina/programa que o usuario digite um numero e a aplicação conte ate cem em numeros pares

numero=int(input("DIgite um numero: "))
for numero in range(numero,101):
    if(numero%2==0):
        print(numero)


# numero=int(input("Digite um numero: "))
# while(numero<=100):
#     if(numero%2==0):
#         print(numero)
#         numero+=1


