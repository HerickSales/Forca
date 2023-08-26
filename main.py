import funcoes 

print('*'*30)
print('Bem-Vindo! ')
print('Vamos jogar forca!')
print("*"*30)

palavra_chave=funcoes.palavra_aleatoria()
erro=0
letras_certas=['_' for i in range(len(palavra_chave))]
chutes=[]

ganhou=False
perdeu=False

tot_letras=len(palavra_chave)
tracejado=['_'*tot_letras]

while True:

    print(funcoes.quantidade_erro(erro))
    print(letras_certas)
    if erro==6:
        print('voce perdeu... tente novamente!')
        perdeu=True
        break

    if '_' not in letras_certas:
        ganhou=True
        break
    
    if len(chutes)>0:
        print('voce ja disse as letras {}'.format(chutes).upper())


    chute=input('faça seu chute:')
    if chute in chutes:
        chute=input('voce ja disse essa letra, diga uma letra diferente:')
    
    chutes.append(chute)

    if funcoes.verificacao(chute,palavra_chave) is False:    
        erro+=1
    else:
        funcoes.letras(chute,palavra_chave,letras_certas)
    
if ganhou==True:
    print('parabens, voce ganhou!!')

if perdeu==True:
    print('infelizmente voce perdeu...')
    print('a palavra era {}'.format(palavra_chave))






