# Programa de calculo de media de notas
# Autor: Ellen Sabrina Rangel Milan Marassi

#Entrada
nome = input("Digite o nome do aluno(a): ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

#Processamento
media = (nota_1 + nota_2) / 2

#Saida
print(f"\nAluno(a): {nome}")
print(f"media: {media:.2f}")

if media >= 6 :
    print("Situaçao: Aprovado")
else:
    print("Situaçao: Reprovado")
