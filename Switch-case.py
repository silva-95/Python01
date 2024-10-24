# valve=3
# match Value:

#     case 1:
#         result="one"

#     case 2:
#         result="two"

#     case 3:
#         result="three"

#     case _:
#         result="default"

#         print(result)

Total=0 
escolha=0
while(escolha!=5):      
    print("Cardapio")
    print("1- calabresa com cebola - R$59.90\n2- camarão com catupiry - R$87.80\n3- frango com requeijão - R$65.50\n4- banana com chocolate - R$59.90")
    print("5- Finalizar pedido")
    escolha=int(input("Digite a opção escolhida (apenas números):"))

    match escolha:
        case 1:
            print("calabresa com cebola - R$59.90")
            Total+=59.90

        case 2:
            print("camarão com catupiry - R$87.80")
            Total+=87.80

        case 3:
            print("frango com requeijão - R$65.50")
            Total+=65.50

        case 4:
            print(" banana com chocolate - R$59.90")    
            Total+=59.90
        case 5:
            print(f"Total do pedido: R${Total}")

        case _:
            print("Escolha uma opção válida") 

