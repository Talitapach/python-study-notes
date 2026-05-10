# Lista 3 - Exercícios em Python

Este arquivo contém minhas soluções e explicações para os exercícios da Lista 3.

---

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

---

## Questão B

### Conceitos utilizados
- loops
- multiplicação de strings
- impressão de padrões

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

### Lógica

A questão imprime um padrão em forma de pirâmide utilizando:
- `#`
- identação decrescente
- aumento da quantidade de símbolos

---

## Erros Comuns

Alguns erros comuns ao resolver essas questões:

- esquecer de atualizar contadores
- criar loops infinitos por falta de `break`
- formatar a saída incorretamente
- usar espaços normais ao invés de caracteres Unicode especiais
- esquecer de validar valores negativos
- ler inputs na ordem errada
- misturar strings com inteiros

---