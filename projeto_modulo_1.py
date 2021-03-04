#Funções
###Função que só printa instruções do jogo
def como_jogar():
    print(
    f'\nNo jogo quem define os caminhos do personagem principal é você. \nO jogo é simples, são oferecidas possibilidades numeradas em que \nvocê poderá escolher apenas uma. Você deve digitar o número da ação \nque deseja fazer. E suas escolhas é que desenrolarão o andar da história.\n')

###Função que printa o enredo
def enredo():
    print('='*75)
    print(
    f'\nOs reptilianos finalmente se mostraram a sociedade.\n'
    f'Após muitos anos vivendo nas sombras arquitetando planos \nde domínio do planeta Terra, eles finalmente se mostraram. \n'
    f'A espécie de répteis humanoides botaram seu plano maléfico \nem prática. Eles criaram uma doença'
    f'respiratória muito grave, \na Covid-19, que vitimou muitas pessoas. Para, logo depois, \nvenderem a "cura".\n'
    f'Uma vacina, que na verdade, era o ponto final na humanidade. \nPois, a vacina, transformava humanos em jacarés! \n'
    f'Em pouco tempo milhões de jacarés povoavam as ruas do mundo todo. \nJacarés andavam livres pela 5ª Avenida em NY; Admiravam'
    f'a Jacaroa Lisa \nno Museu do Louvre e enchiam o Maracanã para ver Jacarepaguá FC \ne Jararezinho pela final do campeonato carioca.\n'
    f'\nVocê está sozinho trancado em sua casa \ntentando sobreviver em meio aos animais.'
    f'\nPois, você é a resistência. E não sucumbiu a maléfica vacina reptiliana. \n'
    f'\nVocê deve sobreviver!\n')
    print('='*75)

###Apresentação dos personagens
def apresentacao_personagens():
    print('\nEscolha um dos personagens para combater a conspiração reptiliana!')
    print(
        f'Digite: \n'
        f'1 para cloroquiner \n'
        f'2 para ivermectiner \n'
        f'3 para chazinho de gengibrer\n')

###Apresentação dos personagens
##Colocar uma apresentação dos personagens aqui

###Função para estruturar as perguntas
def pergunta(texto):
    print(texto)
    resposta = input()
    while resposta != '1' and resposta != '2' and resposta != '3':
        print(
            f'Valor inválido\n')
        print(texto)
        resposta = input()
    return resposta

###Função que define a escolha dos personagens.
def personagens():
    print()
    personagem = pergunta(
        f'\nEscolha um dos personagens para combater a conspiração reptiliana: \n'
        f'[1] Cloroquiner\n[2] Ivermectiner\n[3] Chazinho de gengibrer ')
    if personagem == '1':
        personagem = 'cloroquiner'
    elif personagem == '2':
        personagem = 'ivermectiner'
    else:
        personagem = 'chazinho de gengibrer'
    print(f'Você escolheu {personagem}\n')
    return personagem

###Função para iniciar o jogo
def inicio():
    print(f'='*75)
    print(
        f'TOC! TOC! TOC!\n'
        f'\nQuem bate na sua porta?? Seriam os jacarés tentando invadir?\n'
        f'A polícia reptiliana descobriu onde você mora e vieram prendê-lo?\n'
        f'Você olha pelo olho mágico.'
        f'É a Rainha Elizabeth, parada em sua porta!! \nA própria rainha da Inglaterra batendo em sua casa!!'
        f'Você abrirá a porta\npara a Rainha Elizabeth?\n')
    comeco = pergunta(
        f'Digite: \n'
        f'[1] Para abrir a porta para ela\n'
        f'[2] Para não abrir! Não confio em ninguém!'
    )
    return comeco

###Caminho caso não abra a porta para a Rainha
def n_abre_porta():
    n_abre_porta = pergunta(
        f'Digite: \n'
        f'[1] Para abrir a porta, ela é muito insistente! Vou ver o que ela quer.\n'
        f'[2] Para não abrir a porta, ela é muito chata! Não quero ela na minha casa!')
    return n_abre_porta

###Print da Rainha entrando na casa
def rainha_entra():
    print(
          f'\nEla entra em sua casa observando tudo cautelosamente e diz: \n'
          f'"Olá, sou a Rainha Elizabeth II! Eu costumava ser a rainha dos humanos ingleses, \nmas fomos dominados por esses reptilianos e perdi meu reino\n'
          f'Fiquei sabendo que tem um humano muito inteligente aqui nesta casa! E vim \npara recrutá-lo para a luta contra os reptilianos! Pela reconstrução do reinado dos humanos!!"\n'
          f'Mas antes de continuarmos, você poderia me dar um copo dágua?"\n')

###Caminho para servir água para a rainha ou não
def dar_agua():
    print(f'Dar água para a Rainha?')
    dar_agua = pergunta(
        f'Digite: \n'
        f'[1] Para ir a cozinha e voltar com a água para ela\n'
        f'[2] Para mandar ela ir na frente e não perder ela de vista\n'
        f'[3] Para não dar água de jeito nenhum! Não chamei ela aqui!!'
        )
    return dar_agua

###Função chamada quando perde
def perde():
    perde = True
    print(
        f'\33[91m\nVocê perdeu!\33[m\n'
        f'Ela estava te enganando o tempo todo!\n'
        f'Ela é a rainha dos reptilianos!\n'
        f'Você se descuidou e ela te transformou em jacaré!\n')
    return perde

###Função chamada quando ganha
def ganha():
    ganha = True
    print(
        f'\n\33[92mParabéns você ganhou!\33[m\n'
        f'Ela era a rainha dos reptilianos e queria te transformar em jacaré!\n'
        f'Mas, vc é muito inteligente e não deixou!\n'
        f'Você não se deixa enganar por qualquer um!\n'    
    )
    return ganha

###Função para jogar novamente
def joga_novamente():
    joga_novamente = pergunta(
            f'Gostaria de jogar novamente? \n'
            f'Digite: \n'
            f'[1] Para jogar novamente!\n'
            f'[2] Para terminar o jogo!')
    if joga_novamente == '1':
        return jogo()
    else:
        print('\nFim do jogo')

###Função do caminho ouvir a ligação
def ouvir_ligacao():
    ouvir_ligacao = pergunta(
        f'Digite: \n'
        f'[1] Para ouvir atrás da porta. É melhor previnir\n'
        f'[2] Para não ouvir. Eu não sou fofoqueiro')
    return ouvir_ligacao

###Função o que fazer ao ouvir a ligação
def que_fazer():
    que_fazer = pergunta(
        f'Digite: \n'
        f'[1] Para utilizar seu conhecimento!\n'
        f'[2] Para pular em cima dela!')
    return que_fazer

###Função do caminho para mostrar os vídeo do Olavo de Carvalho
def solta_olavo():
    solta_olavo = pergunta(
        f'Digite: \n'
        f'[1] Para soltar ela. É apenas uma velinha!\n'
        f'[2] Para levar ela ao porão e convertê-la. Mostrar vídeos do Olavo de Carvalho para ela')
    return solta_olavo

###Função para continuar a mostrar os vídeos do Olavo de Carvalho
def continua():
    continua = pergunta(
        f'Digite: \n'
        f'[1] Para não parar, ela deve ver a verdade!!\n'
        f'[2] Para parar e soltar ela')
    return continua

#O jogo
###Função que roda o jogo em si
def jogo():
    como_jogar()
    enredo()
    #apresentacao_personagens()
    personagem = personagens()
    comeco = inicio()
    if comeco == '1':
        rainha_entra()
    else:
        print(
        f'\nEla está batendo loucamente na porta, não vai abrir mesmo?'
        )
        nao_abre = n_abre_porta()
        if nao_abre == '1':
            rainha_entra()
        else:
            print(f'\nEla é muito insistente e entrou pela janela mesmo!!\n')
            rainha_entra()
    agua = dar_agua()
    if agua == '1':
        perde()
        joga_novamente()
    elif agua == '2':
        print(
            f'Vocês chegaram a cozinha\n'
            f'Ela pegou a própria água!\n'
            f'Mas, agora, pediu para ir para outro cômodo para fazer uma ligação\n'
            f'Ir para atrás da porta e ouvir a ligação?\n')
        ligacao = ouvir_ligacao()
        if ligacao == '1':
            print(
                f'\nEla está pedindo reforços!\n'
                f'Ela é uma deles e está chamando reforços para te prender!\n'
                f'O que você vai fazer?\n')
            fazer = que_fazer()
            if fazer == '1':
                if personagem == 'cloroquiner':
                    print('\nCloroquina não é eficaz contra o Corona Vírus, muito menos contra reptilianos\n')
                    perde()
                    joga_novamente()
                elif personagem == 'ivermectiner':
                    print('Ivermectina não é eficaz contra o Corona Vírus, muito menos contra reptilianos\n')
                    perde()
                    joga_novamente()
                else:
                    print('Chá de gengibre é uma delícia, mas não é eficaz contra Corona vírus muito menos contra reptilianos\n')
                    perde()
                    joga_novamente()
            else:
                print('\nVocê prendeu a rainha dos reptilianos!!')
                solta = solta_olavo()
                if solta == '1':
                    perde()
                    joga_novamente()
                else:
                    print('\nEla não aguenta mais! Está pedindo para parar')
                    continuar = continua()
                    if continuar == '1':
                        print('\nEla não resistiu a tanto conhecimento e faleceu!')
                        ganha()
                        joga_novamente()
                    else:
                        print('Ela foi embora e prometeu nunca mais voltar! Você é a resistência e nunca será dobrado!')
                        ganha()
                        joga_novamente()
        else:
            perde()
            joga_novamente()
    else:
        print('\nEla estava muito tempo sem beber água! Reptilianos não podem desidratar e ela faleceu!!')
        ganha()
        joga_novamente()

###Rodar o jogo
jogo()