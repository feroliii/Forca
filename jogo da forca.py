import random

palavras = ['blitz','lux','yasuo','zed','gnar','caitlyn']
certa = random.choice(palavras)
amostra = ['-'] * len(certa)
tent = 8

print('----------------------------')
print('Bem-vindo ao Jogo da Forca') 
print('----------------------------')

for i in range(9):
     letra = input('Digite uma letra: ').lower()
     if letra in certa:
        indice = certa.index(letra)
        amostra[indice] = letra 
        print(f'Tentativas = {tent}')
        print(f"Palavra: {amostra}")
        print()
     if '-' not in amostra:
        print('PARABENS, VOCE GANHOU')
        break
     if letra not in certa:
        print(f'Tentativas = {tent}')
        print(f"Palavra: {amostra}")
        print("Você errou")
        print()
     tent -= 1
     if tent == 0:
         print(f'Perdeu irmão :(')
         break

