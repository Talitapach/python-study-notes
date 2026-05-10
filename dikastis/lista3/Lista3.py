def questaoA():
    musicas = ""
    quantMusica = 0

    while (True):
        musica = input()
        if(musica.upper() == "VOA, VOA BRABULETA"):
            break

        quantMusica += 1

        if(quantMusica == 1):
            musicas = musica
        else:
            musicas = musicas + " - " + musica
                
                
    print("Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!") 
    print(f"A quantidade de músicas selecionadas foi {quantMusica}")  
    print(f"Setlist de músicas: {musicas}")


def questaoB():
    i = int(input())
    l = "⠀"
    n = "#"
    if(i != 0):
        print(l*i + n)
    else:
        print("")
    while(i > 1):
        i-=1
        n += "##"
        print(l*i + n)


def questaoC():
    contadorUniforme = 0
    contadorIsotonico = 0
    contadorRaquete = 0
    contadorToalha = 0
    contadorTotal = 0
    sabotagem = False
    materialAnterior = ""

    while(True):
        material = input()

        if(material == "FIM"):
            break

        if material == "Sabotagem":
            materialAnterior = "Sabotagem"
            continue

        if(materialAnterior != "Sabotagem"):
            if(material == "Uniforme"):
                contadorUniforme += 1
                contadorTotal += 1
                print(f"Tava faltando camisa! Agora temos {contadorUniforme} uniforme(s)")
            elif(material == "Isotônico"):
                contadorIsotonico += 1
                contadorTotal += 1
                print(f"Bora garantir a hidratação! Agora temos {contadorIsotonico} isotônico(s)")
            elif(material == "Raquete"):
                contadorRaquete += 1
                contadorTotal += 1
                print(f"Mais uma raquete saindo! Agora temos {contadorRaquete} raquete(s)")
            elif(material == "Toalha"):
                contadorToalha += 1
                contadorTotal += 1
                print(f"Mais uma toalha saindo! Agora temos {contadorToalha} toalha(s)")
        else:
            if(material == "Uniforme" and contadorUniforme >= 1):
                contadorUniforme -= 1
                contadorTotal -=1
                sabotagem = True
                print("O sueco está roubando as camisas de Hugo!")
            elif(material == "Isotônico" and contadorIsotonico >= 1):
                contadorIsotonico -= 1
                contadorTotal -= 1
                sabotagem = True
                print("O sueco está sabotando a hidratação de Hugo!")
            elif(material == "Raquete" and contadorRaquete >= 1):
                contadorRaquete -= 1
                contadorTotal -= 1
                sabotagem = True
                print("O sueco está roubando as raquetes de Hugo!")
            elif(material == "Toalha" and contadorToalha >= 1):
                contadorToalha -= 1
                contadorTotal -= 1
                sabotagem = True
                print("O sueco está roubando as toalhas de Hugo!")
            materialAnterior = ""

    print("Bora ver o relatório final dos materiais!")
    print(f"Uniforme: {contadorUniforme} unidade(s).")
    print(f"Isotônico: {contadorIsotonico} unidade(s).")
    print(f"Raquete: {contadorRaquete} unidade(s).")
    print(f"Toalha: {contadorToalha} unidade(s).")

    if(contadorTotal == 0 and sabotagem == True):
        print("Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!")
    elif(contadorTotal == 0 and sabotagem == False):
        print("Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.")
    elif(contadorUniforme < 1 or contadorToalha < 1 or contadorIsotonico < 1 or contadorRaquete < 1):
        print("Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!")
    else:
        print("Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!")


def questaoD():
    doces = int(input())
    jogador1 = input()
    jogador2 = input()

    if jogador1 != "Arthur" and jogador2 != "Arthur":
        print("Epa!!! E cadê o dono dos doces??")
    else:
        print("A batalha vai começar!")
        rodada = 0
        
        while doces > 0:
            rodada += 1
            
            vidaJogador1 = 10
            vidaJogador2 = 10
            
            if rodada == 1 and doces % 10 != 0:
                x = doces % 10
                print(f"Pra aquecer, essa primeira vale menos, só {x} doces!")
            else:
                x = 10
                print(f"Batalha número {rodada}!")

            while vidaJogador1 > 0 and vidaJogador2 > 0:
                jogada1 = input()
                jogada2 = input()

                if jogada1 == jogada2:
                    print("Eita, jogaram a mesma coisa dessa vez.")
                else:
                    if jogada1 == "papel" and jogada2 == "tesoura":
                        vidaJogador1 -= 3
                        vidaJogador2 += 1
                    elif jogada1 == "tesoura" and jogada2 == "papel":
                        vidaJogador2 -= 3
                        vidaJogador1 += 1
                    elif jogada1 == "pedra" and jogada2 == "papel":
                        vidaJogador1 -= 2
                        vidaJogador2 += 2
                    elif jogada1 == "papel" and jogada2 == "pedra":
                        vidaJogador2 -= 2
                        vidaJogador1 += 2
                    elif jogada1 == "pedra" and jogada2 == "tesoura":
                        vidaJogador2 -= 4
                    elif jogada1 == "tesoura" and jogada2 == "pedra":
                        vidaJogador1 -= 4

                    if vidaJogador1 < 0: 
                        vidaJogador1 = 0
                    if vidaJogador2 < 0: 
                        vidaJogador2 = 0

                    print(f"Esse turno terminou com {jogador1} tendo {vidaJogador1} de vida e {jogador2} tendo {vidaJogador2}!")

            if vidaJogador1 > 0:
                ganhadorRodada = jogador1
            else:
                ganhadorRodada = jogador2
                
            print(f"A rodada {rodada} vai para {ganhadorRodada}, que garante seus doces!")
            doces -= x


def questaoE():
    dinheiroTotal = int(input())

    qtdCompras = 0
    custoTotal = 0

    print(f"A família possui {dinheiroTotal} ainda, talvez ele fique tranquilo hoje")

    while(True):
        compra = input()

        if(compra == "Amauri"):
            print("Sabia que vocês estão loucos, hora de encerrar essa loucura!")
            break
        else:
            custo = int(input())
        
            
        if(custo > dinheiroTotal):
            print("Enlouqueceram? Vocês estão falidos")
            break
        
        qtdCompras += 1
        custoTotal += custo
        dinheiroTotal -= custo
        
        if(custo > 500000):
            print(f"Enlouqueceram de vez {custo} reais num(a) {compra}")
        elif(custo < 1000):
            print(f'Será que se acalmaram?! {compra} por "somente" {custo} reais')
        else:
            print(f"Gastaram {custo} reais para comprar um(a) {compra}")
            
        if(compra == "carro"):
            modelo = input()
            if(modelo == "chevette"):
                print("chevette : Relembrando as origens será?")
            elif(modelo == "jeep"):
                print("jeep : Será que ele tá se preparando para outra aventura que não irá?")
            elif(modelo == "bmw"):
                print("bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁")
                
        if(dinheiroTotal == 0):
            print("Enlouqueceram? Vocês estão falidos")
            break
                    
    print(f"{qtdCompras} - {custoTotal} reais")
    