import random as rd

def lista_pro_user(l):
    if len(l[0]) == 0:
        print('Letras Certas: 0')
    else:
        print('Letras Certas:', end=' ')
        for i in l[0]:
            print(i,end=' ')
        print()
    if len(l[1]) == 0:
        print('Letras na posição Errada: 0')
    else:
        print('Letras na posição Errada:', end=' ')
        for w in l[1]:
            print(w,end=' ')
        print()
    if len(l[2]) == 0:
        print('Letras Erradas: 0')
    else:
        print('Letras Erradas:', end=' ')
        for g in l[2]:
            print(g,end=' ')
        print('\n')

def letras(let_user, pal_secreta):

    letras_certas_pos_certa = []
    letras_certas_pos_errada = []
    letras_erradas = []
    l = ''.join(let_user) #quando ver l, é só uma redução
    p = ''.join(pal_secreta) #quando ver p, é só uma redução

    for indice in range(len(pal_secreta)):
        if let_user[indice] in pal_secreta:
            if l[indice] == p[indice]:
                letras_certas_pos_certa.append(let_user[indice])
            else:
                letras_certas_pos_errada.append(let_user[indice])
        else:
            letras_erradas.append(let_user[indice])
    return [letras_certas_pos_certa, letras_certas_pos_errada, letras_erradas]

tentativas = 10
win = 0
lista_de_palavras = []

with open('texto.txt', 'r') as palavras:
    for linha in palavras:
        linha = linha.upper()
        palavra = linha.strip()
        lista_de_palavras.append(palavra)

gera_palavra_secreta = rd.choice(lista_de_palavras)

print('BEM VINDO AO JOGO DE ADIVINHAÇÃO DE PALAVRAS!!\nAQUI VOCÊ TERÁ QUE ADIVINHAR EM 10 TENTATIVAS A PALAVRA SECRETA QUE CONTÉM 5 LETRAS!')
print('VAMOS COMEÇAR!\n\n')

while tentativas > 0:
    try:
        ui = str(input('Insira uma palavra de 5 LETRAS:\nTentativas:{}\n> '.format(tentativas)))
        user_input = ui.upper()
        print()

        if len(user_input) != 5:
            raise ValueError("\nO--------------------------O\n Insira uma resposta válida.\nO--------------------------O\n")
        
        elif user_input == gera_palavra_secreta:
            win+=1
            print('Você Acertou a palavra!\nTentativas feitas: {}\n'.format(win))
            break

        for pos in range(len(user_input)):
            if ord(user_input[pos]) < 65 or ord(user_input[pos]) > 90:
                raise ValueError("\nO--------------------------O\n Insira uma resposta válida.\nO--------------------------O\n")
            
        todas_letras = letras(user_input, gera_palavra_secreta)
        lista_pro_user(todas_letras)

        win+=1
        tentativas-=1
        if tentativas == 0:
            print('Você perdeu :(\nA palavra certa era {}.\nTente novamente.'.format(gera_palavra_secreta))
    except ValueError as erro:
        print(erro)
