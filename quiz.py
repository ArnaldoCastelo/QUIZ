print("=== QUIZ INTERATIVO ===")
print("Responda às perguntas abaixo!")

pontuacao = 0

pergunta = input("1. Qual é a capital do Brasil? ")

if pergunta.lower() == "brasília":
    print("Resposta correta!")
    pontuacao += 1
else:
    print("Resposta incorreta!")

pergunta = input("2. Quanto é 5 + 5? ")

if pergunta == "10":
    print("Resposta correta!")
    pontuacao += 1
else:
    print("Resposta incorreta!")

pergunta = input("3. Qual planeta é conhecido como planeta vermelho? ")

if pergunta.lower() == "marte":
    print("Resposta correta!")
    pontuacao += 1
else:
    print("Resposta incorreta!")

print()
print("=== RESULTADO ===")
print("Sua pontuação foi:", pontuacao, "de 3")