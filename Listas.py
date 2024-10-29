# frutas= ["maça", "banana", "cereja"]....
#           (0)        (1)     (2).......     
# frutas.append("melaõ") append - comando para adicionar na lista
# frutas.append("Abacaxi")
# frutas.append("morango")
# frutas.pop() pop - comando para excluir item da lista
# frutas.sort() sort - comando para ordenar em ordem alfabetica
# frutas.reverse() reverse - comando para reverter ordem alfabetica
# print(len(frutas)) len- comando para exibir em numero quantos itens tem na lista 


frutas= ["maça", "banana", "cereja"]
frutas.append("Morango")
frutas.append("melão")
frutas.append("maça")
frutas.pop(0)
frutas.sort()
frutas.reverse()
for i in range(len(frutas)) :
    if(frutas[i] == "banana"):
        frutas.pop(i)
        break
print(frutas)       
        
        

    


# frutas.append(input("Digite uma fruta"))
# print(len(frutas))

