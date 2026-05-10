"""
Lista 3 - Introdução à Programação
Centro de Informática - UFPE
 
Este arquivo contém as soluções para os exercícios da Lista 3.
Cada questão está separada em uma função própria.
 
Questões:
    A - Setlist das Empreguetes (strings, loop infinito, break)
    B - Torre de blocos (padrão visual, multiplicação de strings)
    C - Materiais do Hugo Calderano (contadores, sabotagem em duas linhas)
    D - Batalha de doces do Arthur (loops aninhados, pedra-papel-tesoura)
    E - Finanças da família do Tino (leitura condicional de input, acumuladores)
"""
 
 
def questaoA():
    """
    Questão A - Setlist das Empreguetes
 
    Lê músicas uma a uma e monta a setlist da banda.
    Para quando a música 'Voa, Voa Brabuleta' for digitada,
    independente de maiúsculas ou minúsculas.
 
    Restrição: não é permitido usar listas.
    A setlist é construída concatenando strings manualmente com ' - '.
 
    Entrada:
        Músicas digitadas linha a linha (quantidade indefinida)
        Termina com qualquer variação de 'Voa, Voa Brabuleta'
 
    Saída:
        Saudação do radialista
        Quantidade de músicas selecionadas
        Setlist separada por ' - '
    """
 
    musicas = ""      # string que vai acumulando as músicas separadas por ' - '
    quantMusica = 0   # contador de músicas legítimas (não conta a música sabotadora)
 
    while True:
        musica = input()
 
        # .upper() converte para maiúsculo antes de comparar,
        # assim pega qualquer variação: 'voa, voa brabuleta', 'VOA, VOA BRABULETA', etc.
        if musica.upper() == "VOA, VOA BRABULETA":
            break  # música sabotadora detectada, encerra a coleta
 
        quantMusica += 1
 
        # na primeira música não colocamos ' - ' na frente
        # a partir da segunda, concatenamos com separador
        if quantMusica == 1:
            musicas = musica
        else:
            musicas = musicas + " - " + musica
 
    print("Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!")
    print(f"A quantidade de músicas selecionadas foi {quantMusica}")
    print(f"Setlist de músicas: {musicas}")
 
 
def questaoB():
    """
    Questão B - Torre de blocos
 
    Imprime uma pirâmide de '#' com N andares.
    Cada andar tem mais dois '#' que o anterior e um espaço a menos à esquerda.
 
    ATENÇÃO: o caractere de espaço usado NÃO é o espaço comum do teclado.
    É o caractere Unicode U+2800 (Braille Pattern Blank), copiado do enunciado.
    Usar espaço normal causa falha na submissão.
 
    Entrada:
        N (int) - altura da torre
 
    Saída:
        Pirâmide de N andares usando '#' e o caractere especial de espaço
    """
 
    i = int(input())  # altura da torre (também é o número de espaços da primeira linha)
    l = "⠀"           # caractere Unicode U+2800 — NÃO é um espaço normal!
    n = "#"           # string de cerquilhas, começa com 1 e cresce 2 a cada linha
 
    # a primeira linha é tratada separadamente porque o while começa decrementando i
    # se a primeira linha entrasse no loop, já sairia com um espaço a menos
    if i != 0:
        print(l * i + n)
    else:
        print("")  # caso especial: N = 0, não imprime nada
 
    # a cada iteração: perde 1 espaço à esquerda, ganha 2 cerquilhas
    while i > 1:
        i -= 1
        n += "##"
        print(l * i + n)
 
 
def questaoC():
    """
    Questão C - Materiais do Hugo Calderano
 
    Contabiliza 4 tipos de materiais (Uniforme, Isotônico, Raquete, Toalha).
    Truls Möregårdh pode tentar sabotar materiais — a sabotagem vem em DUAS linhas:
        linha 1: 'Sabotagem'
        linha 2: o material alvo
 
    A sabotagem só tem efeito se houver pelo menos 1 unidade do material.
    O programa encerra ao receber 'FIM' e exibe um relatório com 4 mensagens possíveis.
 
    Entrada:
        Materiais ou 'Sabotagem' + material, linha a linha
        Encerra com 'FIM'
 
    Saída:
        Mensagem para cada material adicionado ou sabotado
        Relatório final com contadores e mensagem de encerramento
    """
 
    # contadores individuais de cada material
    contadorUniforme = 0
    contadorIsotonico = 0
    contadorRaquete = 0
    contadorToalha = 0
    contadorTotal = 0    # soma de todos os materiais (facilita a verificação final)
 
    sabotagem = False    # flag: vira True se alguma sabotagem tiver efeito real
    materialAnterior = ""  # memória entre iterações: guarda se a linha anterior foi 'Sabotagem'
 
    while True:
        material = input()
 
        if material == "FIM":
            break  # encerra a coleta e vai para o relatório
 
        # se chegou 'Sabotagem', apenas marca e pula para a próxima iteração
        # o continue evita processar 'Sabotagem' como se fosse um material
        if material == "Sabotagem":
            materialAnterior = "Sabotagem"
            continue
 
        if materialAnterior != "Sabotagem":
            # caminho normal: adiciona o material ao contador correspondente
            if material == "Uniforme":
                contadorUniforme += 1
                contadorTotal += 1
                print(f"Tava faltando camisa! Agora temos {contadorUniforme} uniforme(s)")
            elif material == "Isotônico":
                contadorIsotonico += 1
                contadorTotal += 1
                print(f"Bora garantir a hidratação! Agora temos {contadorIsotonico} isotônico(s)")
            elif material == "Raquete":
                contadorRaquete += 1
                contadorTotal += 1
                print(f"Mais uma raquete saindo! Agora temos {contadorRaquete} raquete(s)")
            elif material == "Toalha":
                contadorToalha += 1
                contadorTotal += 1
                print(f"Mais uma toalha saindo! Agora temos {contadorToalha} toalha(s)")
        else:
            # caminho de sabotagem: decrementa só se houver pelo menos 1 unidade
            if material == "Uniforme" and contadorUniforme >= 1:
                contadorUniforme -= 1
                contadorTotal -= 1
                sabotagem = True  # sabotagem teve efeito real
                print("O sueco está roubando as camisas de Hugo!")
            elif material == "Isotônico" and contadorIsotonico >= 1:
                contadorIsotonico -= 1
                contadorTotal -= 1
                sabotagem = True
                print("O sueco está sabotando a hidratação de Hugo!")
            elif material == "Raquete" and contadorRaquete >= 1:
                contadorRaquete -= 1
                contadorTotal -= 1
                sabotagem = True
                print("O sueco está roubando as raquetes de Hugo!")
            elif material == "Toalha" and contadorToalha >= 1:
                contadorToalha -= 1
                contadorTotal -= 1
                sabotagem = True
                print("O sueco está roubando as toalhas de Hugo!")
 
            # limpa a memória: próxima entrada volta a ser tratada como material normal
            materialAnterior = ""
 
    # relatório final
    print("Bora ver o relatório final dos materiais!")
    print(f"Uniforme: {contadorUniforme} unidade(s).")
    print(f"Isotônico: {contadorIsotonico} unidade(s).")
    print(f"Raquete: {contadorRaquete} unidade(s).")
    print(f"Toalha: {contadorToalha} unidade(s).")
 
    # mensagem de encerramento: a ordem dos elif importa pois as condições se excluem
    if contadorTotal == 0 and sabotagem == True:
        print("Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!")
    elif contadorTotal == 0 and sabotagem == False:
        print("Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.")
    elif contadorUniforme < 1 or contadorToalha < 1 or contadorIsotonico < 1 or contadorRaquete < 1:
        print("Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!")
    else:
        print("Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!")
 
 
def questaoD():
    """
    Questão D - Batalha de doces do Arthur
 
    Arthur e um amigo disputam doces em rodadas de pedra-papel-tesoura com regras especiais.
    Os doces são divididos em rodadas de 10. Quem zerar a vida do adversário ganha a rodada.
 
    Regras de combate (por turno):
        - Mesma jogada: empate, nada acontece
        - Papel vs Tesoura: papel perde 3 vidas, tesoura recupera 1
        - Pedra vs Papel: pedra perde 2 vidas, papel recupera 2
        - Pedra vs Tesoura: tesoura perde 4 vidas
    A vida nunca vai abaixo de zero.
 
    Se o total de doces não for múltiplo de 10, a primeira rodada vale o resto (doces % 10).
    O jogo só acontece se Arthur for um dos jogadores.
 
    Entrada:
        doces (int) - total de doces em disputa
        jogador1 (str) - nome do primeiro jogador
        jogador2 (str) - nome do segundo jogador
        jogadas alternadas (str) - uma por linha, até a rodada terminar
 
    Saída:
        Resultado de cada turno e de cada rodada
    """
 
    doces = int(input())
    jogador1 = input()
    jogador2 = input()
 
    # o jogo só começa se Arthur estiver jogando — os doces são dele
    if jogador1 != "Arthur" and jogador2 != "Arthur":
        print("Epa!!! E cadê o dono dos doces??")
    else:
        print("A batalha vai começar!")
        rodada = 0
 
        # loop externo: cada iteração = uma rodada completa
        while doces > 0:
            rodada += 1
 
            # as vidas são reinicializadas a cada rodada, não podem carregar da anterior
            vidaJogador1 = 10
            vidaJogador2 = 10
 
            # primeira rodada especial: se doces não for múltiplo de 10,
            # essa rodada vale apenas o resto (ex: 35 doces → primeira vale 5)
            if rodada == 1 and doces % 10 != 0:
                x = doces % 10  # x = quantos doces essa rodada vale
                print(f"Pra aquecer, essa primeira vale menos, só {x} doces!")
            else:
                x = 10  # rodadas normais valem sempre 10
                print(f"Batalha número {rodada}!")
 
            # loop interno: cada iteração = um turno dentro da rodada
            # termina quando qualquer um dos jogadores chegar a zero
            while vidaJogador1 > 0 and vidaJogador2 > 0:
                jogada1 = input()
                jogada2 = input()
 
                if jogada1 == jogada2:
                    # empate: nenhuma vida muda
                    print("Eita, jogaram a mesma coisa dessa vez.")
                else:
                    # aplica os efeitos conforme a combinação de jogadas
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
 
                    # garante que a vida não fique negativa
                    # sem esse clipe, o while nunca terminaria se vida fosse -X
                    if vidaJogador1 < 0:
                        vidaJogador1 = 0
                    if vidaJogador2 < 0:
                        vidaJogador2 = 0
 
                    print(f"Esse turno terminou com {jogador1} tendo {vidaJogador1} de vida e {jogador2} tendo {vidaJogador2}!")
 
            # ao sair do loop interno, um dos dois tem vida zero
            # quem ainda tem vida ganhou a rodada
            if vidaJogador1 > 0:
                ganhadorRodada = jogador1
            else:
                ganhadorRodada = jogador2
 
            print(f"A rodada {rodada} vai para {ganhadorRodada}, que garante seus doces!")
 
            # desconta os doces desta rodada (x = 10 nas normais, resto na primeira especial)
            doces -= x
 
 
def questaoE():
    """
    Questão E - Finanças da família do Tino
 
    Amauri acompanha os gastos da família ganhadora da Mega-Sena.
    O programa lê compras e desconta do saldo até um de três encerramentos:
        1. 'Amauri' aparecer no lugar de uma compra (Amauri interrompe)
        2. O custo de uma compra ultrapassar o saldo disponível (falência)
        3. O saldo zerar exatamente após uma compra (falência)
 
    Compras com custo > 500.000 ou < 1.000 têm mensagens especiais.
    Se a compra for 'carro', o programa lê também o modelo (chevette, jeep ou bmw).
 
    ATENÇÃO: o custo só é lido se a compra NÃO for 'Amauri'.
    Inverter essa ordem causa travamento do programa.
 
    Entrada:
        dinheiroTotal (int) - saldo inicial
        compra (str) e custo (int) alternados, linha a linha
        Encerra com 'Amauri' no lugar de uma compra, falência, ou saldo zero
 
    Saída:
        Mensagem inicial com saldo
        Mensagem para cada compra (com variação conforme o custo)
        Mensagem extra se compra for 'carro'
        Mensagem de encerramento (Amauri ou falência)
        Resumo final: quantidade de compras e custo total
    """
 
    dinheiroTotal = int(input())
 
    qtdCompras = 0   # conta apenas compras que foram efetivamente realizadas
    custoTotal = 0   # soma dos custos das compras realizadas
 
    print(f"A família possui {dinheiroTotal} ainda, talvez ele fique tranquilo hoje")
 
    while True:
        compra = input()
 
        # Amauri aparece no lugar de uma compra para encerrar o programa
        # o custo NÃO é lido neste caso — Amauri não tem preço associado
        if compra == "Amauri":
            print("Sabia que vocês estão loucos, hora de encerrar essa loucura!")
            break
        else:
            custo = int(input())  # custo só é lido se a compra for válida
 
        # verifica se há saldo suficiente ANTES de contabilizar
        # a compra que quebra o banco não entra no contador
        if custo > dinheiroTotal:
            print("Enlouqueceram? Vocês estão falidos")
            break
 
        # compra aprovada: atualiza os acumuladores e o saldo
        qtdCompras += 1
        custoTotal += custo
        dinheiroTotal -= custo
 
        # mensagem de custo varia conforme o valor da compra
        if custo > 500000:
            print(f"Enlouqueceram de vez {custo} reais num(a) {compra}")
        elif custo < 1000:
            print(f'Será que se acalmaram?! {compra} por "somente" {custo} reais')
        else:
            print(f"Gastaram {custo} reais para comprar um(a) {compra}")
 
        # se a compra for um carro, lê e imprime o modelo
        # esse bloco vem DEPOIS da mensagem de custo — a ordem importa para o output
        if compra == "carro":
            modelo = input()
            if modelo == "chevette":
                print("chevette : Relembrando as origens será?")
            elif modelo == "jeep":
                print("jeep : Será que ele tá se preparando para outra aventura que não irá?")
            elif modelo == "bmw":
                print("bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁")
 
        # verifica se o saldo zerou após a compra
        # diferente da falência por custo alto: aqui a compra JÁ foi contabilizada
        if dinheiroTotal == 0:
            print("Enlouqueceram? Vocês estão falidos")
            break
 
    # resumo final: sempre imprime, independente de como o loop terminou
    print(f"{qtdCompras} - {custoTotal} reais")