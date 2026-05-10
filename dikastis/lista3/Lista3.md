# Lista 3 - Exercícios em Python

Este arquivo contém minhas soluções e explicações para os exercícios da Lista 3.


## Organização

Todas as questões foram separadas em métodos/funções dentro do arquivo `Lista3.py`:

```python
def questaoA():
def questaoB():
def questaoC():
def questaoD():
def questaoE():
```

Cada função representa uma questão da lista.


# Questão A
 
### O que a questão pede
 
A gente vai montar a setlist das Empreguetes! O programa lê músicas uma por uma, sem saber de antemão quantas vai receber. Quando aparecer a música "Voa, Voa Brabuleta" (não importa se está em maiúscula, minúscula ou misturado), o programa para e exibe tudo que foi coletado até ali.
 
O desafio extra: **não pode usar listas** pra guardar as músicas.
 
---
 
### A sacada principal: guardar tudo numa string
 
Normalmente nossa primeira ideia seria jogar tudo em uma lista e depois juntar com `join`. Mas a questão proíbe isso. Então a solução é ir **construindo a string aos poucos**, adicionando ` - ` entre cada música manualmente.
 
O truque está aqui:
 
```python
if quantMusica == 1:
    musicas = musica
else:
    musicas = musicas + " - " + musica
```
 
Por que esse `if`? Porque na primeira música a gente não quer o ` - ` na frente. Se simplesmente fizesse sempre `musicas + " - " + musica`, o resultado começaria assim: ` - Vida de Empreguete - ...`, o que estaria errado.
 
---
 
### Por que `.upper()`?
 
A questão avisa que a música sabotadora pode vir escrita de qualquer jeito: `voa, voa brabuleta`, `VOA, VOA BRABULETA`, `Voa, Voa BRABULETA`... Para não precisar checar cada variação, convertemos o que o usuário digitou para maiúsculo antes de comparar:
 
```python
if musica.upper() == "VOA, VOA BRABULETA":
    break
```
 
Assim, não importa como chegou — a comparação sempre funciona.

 
---
 
### Detalhe de output
 
A quantidade exibida **não inclui** a música sabotadora — afinal, ela foi barrada antes de entrar na setlist. O contador só sobe quando uma música legítima entra.
 
---

# Questão B
 
### O que a questão pede
 
Dado um número `N`, imprimir uma torre de blocos em formato de pirâmide. Cada andar da torre tem mais `##` do que o de cima, e os espaços à esquerda vão diminuindo conforme a gente desce — criando o efeito de centralização.
 
Para `N = 3`, a saída fica assim:
 
```
⠀⠀⠀#
⠀⠀###
⠀#####
```
 
---

### Como a torre é construída
 
A lógica toda gira em torno de duas variáveis que mudam a cada linha:
 
- `i` → quantidade de espaços à esquerda (começa em `N`, vai diminuindo)
- `n` → a string de `#` (começa com `"#"`, vai crescendo `+= "##"` a cada linha)
Veja como fica para `N = 4`:
 
| Linha | `i` (espaços) | `n` (cerquilhas) | Resultado       |
|-------|--------------|-----------------|-----------------|
| 1ª    | 4            | `#`             | `⠀⠀⠀⠀#`        |
| 2ª    | 3            | `###`           | `⠀⠀⠀###`       |
| 3ª    | 2            | `#####`         | `⠀⠀#####`      |
| 4ª    | 1            | `#######`       | `⠀#######`     |
 
Repare que a cada linha: `i` perde 1, e `n` ganha 2 cerquilhas. Isso é o que cria o efeito de pirâmide.
 
---
 
### Por que a primeira linha fica fora do `while`?
 
```python
if(i != 0):
    print(l*i + n)   # imprime a primeira linha
while(i > 1):
    i -= 1
    n += "##"
    print(l*i + n)   # imprime as demais
```
 
Porque o `while` começa decrementando `i` antes de imprimir. Se a primeira linha entrasse no loop, ela já sairia com `i-1` espaços — uma a menos do que deveria. Então a primeira linha é tratada separadamente, e o loop cuida do resto.
 
O `if(i != 0)` protege o caso em que `N = 0` é passado como entrada — nesse caso nada é impresso.
 
---
### Detalhe importante

Essa questão possui um problema de formatação muito específico.

A variável:

```python
l = "⠀"
```

NÃO contém um espaço normal.

Ela contém um caractere Unicode especial copiado diretamente do enunciado da questão.

Se você substituir por um espaço comum como:

```python
l = " "
```

a submissão pode falhar por diferença de formatação.

Portanto, o correto é:
- copiar exatamente o caractere do enunciado
- evitar digitar um espaço comum manualmente
 
---
 
### Resumo rápido
 
- A torre tem `N` andares
- Andar `k` (de cima pra baixo) tem `(N - k)` espaços e `(2k - 1)` cerquilhas
- O espaço **não é espaço** — é o caractere Braille U+2800, copie do enunciado
---

# Questão C
 
### O que a questão pede
 
Ajudar Hugo Calderano a organizar os materiais antes do campeonato. O programa lê entradas uma a uma — cada entrada é um material (`Uniforme`, `Isotônico`, `Raquete`, `Toalha`) ou a palavra `Sabotagem` seguida do material a ser sabotado. Quando chegar `FIM`, o programa para e exibe um relatório.
 
A sabotagem tem uma pegadinha: ela **vem em duas linhas**. Primeiro chega `"Sabotagem"`, e só na linha seguinte o material alvo. O programa precisa "lembrar" que a entrada anterior foi uma sabotagem para tratar a próxima linha de forma diferente.
 
---

### A sacada principal: a sabotagem vem em duas linhas
 
Esse é o ponto mais delicado da questão. A entrada não é uma linha só — são duas:
 
```
Sabotagem        ← linha 1: sinal de que vem sabotagem
Uniforme         ← linha 2: qual material será sabotado
```
 
A solução é usar uma variável chamada `materialAnterior` como **memória entre iterações**. Ela guarda o que veio na linha anterior:
 
```python
if material == "Sabotagem":
    materialAnterior = "Sabotagem"
    continue          # pula o resto e vai ler a próxima linha
 
if materialAnterior != "Sabotagem":
    # trata como adição normal
else:
    # trata como sabotagem
    materialAnterior = ""   # reseta a memória
```
 
O `continue` é essencial aqui — sem ele, o programa tentaria processar `"Sabotagem"` como se fosse um material, o que não faz sentido.
 
---
 
### A flag `sabotagem`
 
A variável `sabotagem` começa como `False` e vira `True` assim que qualquer sabotagem tem **efeito real** (ou seja, quando havia pelo menos 1 unidade do material). Ela é usada só no final, para decidir qual mensagem de encerramento imprimir.
 
Repare que ela **não vira True** se a sabotagem não surtiu efeito (quando o contador já está em zero). Isso é intencional — a questão diz que a sabotagem só conta se houver pelo menos uma unidade.
 
---
 
### A condição de sabotagem com efeito
 
```python
elif(material == "Uniforme" and contadorUniforme >= 1):
    contadorUniforme -= 1
    sabotagem = True
    ...
```
 
O `and contadorUniforme >= 1` é a proteção: se o sueco tentar sabotar mas não tiver nenhum uniforme, nada acontece — sem mensagem, sem decremento, sem marcar sabotagem.
 
---
 
### As quatro mensagens finais
 
No encerramento, a lógica das mensagens segue esta ordem de prioridade:
 
| Condição | Mensagem |
|---|---|
| `contadorTotal == 0` e houve sabotagem | Truls conseguiu sabotar tudo |
| `contadorTotal == 0` e não houve sabotagem | Vai faltar material |
| Algum material com zero unidades | Tá faltando alguma coisa |
| Todos com pelo menos 1 | Tudo pronto! |
 
A ordem importa porque as condições são exclusivas — usar `if / elif / elif / else` garante que só uma mensagem será impressa.
 
---
 
### Resumo rápido
 
- Sabotagem **vem em duas linhas** — use uma variável para lembrar o contexto
- `continue` serve para pular para a próxima iteração sem executar o resto do loop
- A sabotagem só tem efeito se o contador do material for `>= 1`
- A flag `sabotagem` só vira `True` quando a sabotagem realmente aconteceu
- A ordem dos `if / elif` no relatório final é importante — as condições se excluem mutuamente
---

# Questão D
 
### O que a questão pede
 
Arthur e um amigo disputam doces num jogo de pedra-papel-tesoura com regras especiais. Os doces são divididos em **rodadas de 10** — quem zerar a vida do adversário primeiro ganha aquela rodada e fica com os doces dela. O jogo só rola se Arthur estiver jogando, afinal os doces são dele.
 
---
 
### A estrutura de dois loops aninhados
 
Essa é a parte mais importante de entender antes de qualquer coisa. O programa tem **dois níveis de repetição**:
 
```
while doces > 0:          ← loop externo: uma iteração = uma rodada
    ...
    while vida1 > 0 and vida2 > 0:    ← loop interno: uma iteração = um turno
        ...
```
 
O loop externo controla as rodadas. O interno controla os turnos dentro de cada rodada. Quando alguém zera a vida, o loop interno para — aí o externo verifica se ainda há doces e, se sim, abre uma nova rodada.
 
---
 
### A primeira rodada especial
 
Se o total de doces **não for múltiplo de 10**, a primeira rodada vale menos — exatamente o resto da divisão por 10:
 
```python
if rodada == 1 and doces % 10 != 0:
    x = doces % 10
    print(f"Pra aquecer, essa primeira vale menos, só {x} doces!")
else:
    x = 10
    print(f"Batalha número {rodada}!")
```
 
O `%` aqui é o operador módulo — ele retorna o **resto** da divisão. Por exemplo: `35 % 10 = 5`. Então se houver 35 doces, a primeira rodada vale 5, e depois vêm três rodadas de 10.
 
Repare que `x` é quem controla quantos doces são descontados ao final da rodada: `doces -= x`. Nas rodadas normais `x = 10`, na primeira especial `x` é o resto.
 
---
 
### As regras de combate
 
Cada turno lê duas jogadas e aplica os efeitos:
 
| Jogada 1 | Jogada 2 | Efeito |
|---|---|---|
| igual | igual | empate, nada acontece |
| papel | tesoura | papel perde 3, tesoura recupera 1 |
| tesoura | papel | papel perde 3, tesoura recupera 1 |
| pedra | papel | pedra perde 2, papel recupera 2 |
| papel | pedra | pedra perde 2, papel recupera 2 |
| pedra | tesoura | tesoura perde 4 |
| tesoura | pedra | tesoura perde 4 |
 
Um detalhe que a questão avisa explicitamente: **a vida não pode ficar negativa**. Por isso existe esse trecho depois de cada cálculo:
 
```python
if vidaJogador1 < 0:
    vidaJogador1 = 0
if vidaJogador2 < 0:
    vidaJogador2 = 0
```
 
Sem isso, se alguém tivesse 2 de vida e levasse 4 de dano, ficaria com -2 — e o loop interno nunca terminaria, pois a condição é `> 0`, não `>= 0`.
 
---
 
### Reinicialização das vidas a cada rodada
 
Repare que `vidaJogador1 = 10` e `vidaJogador2 = 10` estão **dentro** do loop externo:
 
```python
while doces > 0:
    rodada += 1
    vidaJogador1 = 10   # ← reseta a cada nova rodada
    vidaJogador2 = 10   # ← reseta a cada nova rodada
    ...
```
 
Se estivessem fora, as vidas continuariam do ponto onde pararam na rodada anterior — o que seria errado. Cada rodada começa do zero.
 
---
 
### Quem ganhou a rodada?
 
Ao sair do loop interno, um dos dois tem vida zero. A lógica é simples:
 
```python
if vidaJogador1 > 0:
    ganhadorRodada = jogador1
else:
    ganhadorRodada = jogador2
```
 
Não precisa checar os dois — se o primeiro ainda tem vida, ele ganhou. Caso contrário, o segundo ganhou. (A questão não prevê empate exato — ambos não chegam a zero no mesmo turno, pois o loop para quando o primeiro chega.)
 
---
 
### Resumo rápido
 
- Dois `while` aninhados: externo = rodadas, interno = turnos
- `doces % 10` determina se a primeira rodada é especial e quanto ela vale
- Vida não pode ficar negativa — sempre clipa em 0 após o dano
- Vidas são reinicializadas **dentro** do loop externo, não fora
- O programa nem começa se Arthur não for um dos jogadores
---


# Questão E
 
### O que a questão pede
 
Amauri é um contador que acompanha os gastos da família do Tino, ganhadores da Mega-Sena que estão indo à falência. O programa lê compras uma a uma e vai descontando do saldo. Ele para em três situações: Amauri aparece e encerra tudo, a família tenta comprar algo sem ter dinheiro, ou o saldo zera.
 
---
 
### A ordem das verificações importa
 
Esse é o ponto mais delicado do código. Olha a sequência dentro do loop:
 
```python
compra = input()
 
if compra == "Amauri":          # 1º: verifica se é o Amauri
    print("...")
    break
else:
    custo = int(input())        # só lê o custo se não for Amauri
 
if custo > dinheiroTotal:       # 2º: verifica se tem dinheiro
    print("Enlouqueceram? Vocês estão falidos")
    break
 
# só chega aqui se a compra foi válida e tem dinheiro
qtdCompras += 1
custoTotal += custo
dinheiroTotal -= custo
```
 
O `custo` só é lido **depois** de confirmar que não é `"Amauri"`. Isso é intencional — o enunciado diz que Amauri nunca tem custo associado. Se você lesse o custo antes de checar quem é, o programa travaria esperando um input que nunca vai chegar.
 
A checagem de falência (`custo > dinheiroTotal`) vem logo depois, **antes** de contabilizar a compra. A compra que quebra o banco não entra no contador.
 
---
 
### O `break` no meio da falência vs. no fim
 
Existem dois momentos em que o programa imprime `"Enlouqueceram? Vocês estão falidos"`:
 
```python
# caso 1: tentou comprar sem ter dinheiro
if custo > dinheiroTotal:
    print("Enlouqueceram? Vocês estão falidos")
    break
 
# caso 2: ficou com saldo zero depois da compra
if dinheiroTotal == 0:
    print("Enlouqueceram? Vocês estão falidos")
    break
```
 
No **caso 1**, o break vem antes de contabilizar — a compra não aconteceu de verdade.
 
No **caso 2**, o break vem depois — a compra foi feita, o dinheiro acabou, e só aí encerra. Por isso, nesse caso a compra já está contada no total.
 
---
 
### Leitura aninhada: o modelo do carro
 
Se a compra for `"carro"`, o programa lê mais uma entrada — o modelo:
 
```python
if compra == "carro":
    modelo = input()
    if modelo == "chevette":
        print("chevette : Relembrando as origens será?")
    elif modelo == "jeep":
        print("jeep : Será que ele tá se preparando para outra aventura que não irá?")
    elif modelo == "bmw":
        print("bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁")
```
 
Esse bloco fica depois da mensagem de custo, não antes. Ou seja, a ordem de saída é:
 
1. mensagem de custo (`"Gastaram X reais..."`)
2. mensagem do modelo (se for carro)
Se você invertesse, o output ficaria na ordem errada e a submissão falharia.
 
---
 
### As três mensagens de custo
 
Após confirmar que a compra é válida e o dinheiro existe, o programa decide qual mensagem de custo imprimir com base no valor:
 
| Condição | Mensagem |
|---|---|
| `custo > 500000` | Enlouqueceram de vez... |
| `custo < 1000` | Será que se acalmaram?! |
| qualquer outro valor | Gastaram X reais... |
 
Repare que não há `elif` entre as duas primeiras — as condições são mutuamente exclusivas por definição (um número não pode ser maior que 500.000 e menor que 1.000 ao mesmo tempo), então `if / elif / else` funciona perfeitamente.
 
---
 
### O resumo final sempre imprime
 
```python
print(f"{qtdCompras} - {custoTotal} reais")
```
 
Esse `print` está **fora** do loop, então ele sempre executa — independente de como o loop terminou (Amauri, falência por custo alto, ou saldo zerado). Isso é importante: mesmo que o programa encerre abruptamente por `break`, o relatório final sempre aparece.
 
---
 
### Resumo rápido
 
- O custo só é lido se a compra **não** for `"Amauri"` — nunca inverta essa ordem
- A compra que estoura o saldo **não** entra no contador (`break` antes do `+=`)
- A compra que zera o saldo **entra** no contador (`break` depois do `+=`)
- O modelo do carro é lido **depois** da mensagem de custo, não antes
- O `print` final está fora do loop e sempre executa
---


# Erros Comuns

Alguns erros comuns ao resolver essas questões:

- esquecer de atualizar contadores
- criar loops infinitos por falta de `break`
- formatar a saída incorretamente
- usar espaços normais ao invés de caracteres Unicode especiais
- esquecer de validar valores negativos
- ler inputs na ordem errada
- misturar strings com inteiros

---