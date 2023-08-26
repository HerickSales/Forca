
def palavra_aleatoria():
    import random
    lista_palavras=['abelha','anta','andorinha','baleia','besouro','borboleta',
                    'burro','cachorro','cavalo','cupim','elefante','esquilo',
                    'flamingo','ganso','lebre','orca','pernilongo','zebra','boi'] 
    palavra_aleatoria= random.choice(lista_palavras)

    return palavra_aleatoria


def quantidade_erro(erro):
    if erro==0:
         print(' _\n| |\n|\n|')
    if erro==1:
         print(' __\n|  |\n| ( )\n|\n')
    if erro==2:
        print(' __\n|  |\n| ( )\n|  |\n')
    if erro==3:
        print(' __\n|  |\n| ( )\n|  |\n  /')
    if erro==4:
        print(' __\n|  |\n| ( )\n|  |\n  / \ ')
    if erro==5:
        print(' __\n|  |\n| ( )/\n|  |/\n  / \ ')
    if erro==6:
        print(' __\n|  |\n| \( )/\n|  \|/\n   / \ ')
    
    return   ' '


def verificacao(chute, palavra_chave):
    if chute in palavra_chave:
        return True
    else:
        return False


def letras(chute,palavra_chave,letras_certas):
    posicao_letra=[]

    for i, n in enumerate(palavra_chave):
        if n==chute:
            posicao_letra.append(i)
    
    for i in posicao_letra:
        letras_certas[i]=chute.upper()
    
    return letras_certas
        