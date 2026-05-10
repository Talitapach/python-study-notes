def questaoA():
    print("Olá, eu sou o BMO! Prazer em te conhecer, estranho!")
    print("Qual é o seu nome?")
    nome = input()
    if (nome == "Finn" or nome == "Jake"):
        print("Caramba, que coincidência! Você tem o mesmo nome de um amigo meu!")
        
    print("Gostei do seu nome!")

    print("Quantos anos você tem?")
    idade = int(input())

    if (idade == 12):
        print("Nossa, você tem a mesma idade do meu amigo Finn")

    print("Entendi!")

    print("Ei, qual princesa desse mundo é a mais bonita pra você?")
    princesa = input()
    if (princesa == "Princesa de Fogo" or princesa == "Princesa Jujuba"):
        print("Meu amigo Finn vai ficar com ciúmes de você!")
        
    print("Finalmente chegamos!")
    print(f"Foi um prazer te conhecer, {nome}! Boa sorte para encontrar a {princesa} :)")



def questaoB():
    alien = input()

    print("Ben: Tá na hora de virar herói!")

    if(alien == "Chama" or alien == "XLR8" or alien == "Diamante" or alien == "Besta" or alien == "Ultra-T"):
        print(f"Ben: Bora lá, {alien}!")
        print("Gwen: Boa, Ben, agora vamos, temos que encontrar Azmuth.")
    else:
        print(f"Ben: Droga, Não consigo me transformar no {alien}.")
        print("Gwen: Ben Tennyson! Pare com a Bobeira.")
        
    if(alien == "Insectoide"):
        print("Gwen: Ben, de todos os seus bichos, você tentou escolher esse?")
    elif(alien == "Fantasmático"):
        print("Ben: Zs'skayr... Ainda bem que o relógio não funcionou.")
    elif(alien == "XLR8"):
        print("Ben: Vamos encontrar ele bem rápido com o XLR8!")
    elif(alien == "Chama"):
        print("Ben: Eu tô pegando fogo!")



def questaoC():
    velocidadeIJ = int(input())
    velocidadeLR = int(input())
    dificuldadeInimigos = int(input())

    pontuacao = (velocidadeIJ * velocidadeLR) // dificuldadeInimigos

    if(pontuacao <= 65000):
        print("BRUTAL! Ninguém jamais conseguiu alcançar as pontuações fantásticas do Jorel.")
    elif(pontuacao > 65000 and pontuacao <= 99000):
        print("INCRÍVEL! A dupla conseguiu alcançar o top 10 nas pontuações do jogo.")
    elif(pontuacao > 99000 and pontuacao <= 153000):
        print("SENSACIONAL!! Os jogadores conseguiram alcançar o pódio do jogo ao lado das outras pontuações do Jorel.")
    elif(pontuacao > 153000):
        print("IMPOSSÍVEL!!! A DUPLA IMPLACÁVEL FOI CAPAZ DE QUEBRAR O RECORDE INALCANÇÁVEL DO JOREL!")



def questaoD():
    nomeCompetidor1 = input()
    pasteisCompetidor1 = int(input())
    nomeCompetidor2 = input()
    pasteisCompetidor2 = int(input())
    nomeCompetidor3 = input()
    pasteisCompetidor3 = int(input())

    nomeCampeao = None
    pasteisCampeao = None

    if(nomeCompetidor1 != "Lineu" and nomeCompetidor2 != "Lineu" and nomeCompetidor3 != "Lineu"):
        if(pasteisCompetidor1 > pasteisCompetidor2 and pasteisCompetidor1 > pasteisCompetidor3):
            nomeCampeao = nomeCompetidor1
            pasteisCampeao = pasteisCompetidor1
        elif(pasteisCompetidor2 > pasteisCompetidor1 and pasteisCompetidor2 > pasteisCompetidor3):
            nomeCampeao = nomeCompetidor2
            pasteisCampeao = pasteisCompetidor2
        else:
            nomeCampeao = nomeCompetidor3
            pasteisCampeao = pasteisCompetidor3
                
        print(f"A(O) campeã(o) é {nomeCampeao}, com {pasteisCampeao} pastéis consumidos!")
            
        if((nomeCompetidor1 == "Floriano" or nomeCompetidor2 == "Floriano" or nomeCompetidor3 == "Floriano") and nomeCampeao != "Floriano"):
            print(f"Anos comendo pastel e perdeu justo para {nomeCampeao}, lastimável, Sr. Flor!")
        
        if(nomeCampeao == "Agostinho" and pasteisCampeao > 100):
            print("Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!")
        elif(nomeCampeao == "Agostinho" and pasteisCampeao > 50 and pasteisCampeao < 100):
            print("Agostinho madrugou no taxi e veio cheio de fome para a competição!")
    else:
        print("Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!")
    


def questaoE():
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    quantidadeAula = int(input())
    quantidadeFaltas = int(input())

    assistidas = quantidadeAula - quantidadeFaltas

    media = (nota1 + nota2 + nota3) / 3
    presenca = (assistidas/quantidadeAula) * 100

    print(f"Chris, você conseguiu média {media:.2f} e {presenca:.2f}% de presença.")

    if(media >= 8 and presenca >= 75):
        print("Chris está APROVADO por nota e por presença! \U0001F389")
        print("Pisante maneiro, Chris! Agora é só torcer pros outros não vacilarem.")
    elif((media >= 7 and media < 8) and presenca >= 75):
        print("Chris está APROVADO! \u2705")
        print("Sacomé, né? Passou raspando, mas a pizza ainda ficou longe.")
    elif(media >= 7 and presenca < 75):
        print("Chris ESTÁ REPROVADO por FALTA. \u274c")
        print("Trágico! Não adianta só saber, tem que aparecer.")
    elif(media < 7 and presenca >= 75):
        print("Chris ESTÁ REPROVADO por NOTA. \u274c")
        print("Chris, já pro seu quarto ou eu vou te bater até você virar o avesso!")
    else:
        print("Chris ESTÁ REPROVADO por NOTA e por FALTA. \u274c")
        print("Chris, você perdeu o juízo? Eu trouxe você para esse mundo e posso muito bem tirar você dele.")