# Modelo Facebook

nota de 0 a 10

como funciona?
tempo: <quão rapido ele traduz>: quanto maior, melhor
tradução: <qualidade da tradução>: quanto maior, melhor
complexidade: <dificuldade de leitura e escrita do codigo>: quanto maior, melhor

tempo: 8.5:
tradução: 7:
complexidade main: 9.5:
complexidade modelo: 7.5:

Este modelo é realmente bem bom, se caso for bem refinado ou caso consiga encontrar um modelo melhor, pode acabar sendo de bom uso.
Ele pode ser usado mesmo offline, só tem que ser usado uma vez online para o download do modelo
Conseguiria traduzir um jogo grande rapidamente

# como usar o pacote?

primeiro baixe os requerimentos usando: `pip install -r requirements.txt`

depois é só criar uma pasta e colocar o arquivo `modelo.py` dentro da pasta

só criar um arquivo `main.py` na mesma pasta, importar o modelo e começar a programar:

com o arquivo padrão do texto sendo o `CombatUpdate.csv`, a configuração escolhida por mim foi:

```python
from modelo import tradutor_terminal as modelo

modelo.retira = [['§', '§'], ['$', '$'], ['[', ']']] # fala como as variaveis começa e termina para separar
modelo.substituir = 'var' # substitua as variaveis por var
modelo.ignorar = ['ENGLISH'] # ignorar linhas que contenham essas palavras-chave
modelo.caminho = 'CombatUpdate.csv' # caminho pro arquivo
modelo.regex = ';(.*?);' # regex usada para pegar o texto entre os delimitadores
modelo.max_thread = 5 # numero maximo de traduções simultaneas

if __name__ == '__main__': # codigo em si
  modelo.retira_texto_de_arquivo() # retira o texto do arquivo especificado em modelo.caminho
  print('iniciando traduçao') # print
  modelo.traduzir_linhas_salvas() # inicia a tradução
```

# configuração

o modelo tem algumas configurações que podem ser interessantes usar:

`substituir` - é usado para substituir as variaveis nos textos por um texto secundario, para que o modelo não acabe traduzindo as variaveis. Isso é importante pois se caso a variavel não existir, pode acarrentar em bugs no jogo. Recebe uma `str`

`modelo_translate` - o modelo padrão é facebook/m2m100_418M, mas você pode mudar usando esta configuração. Caso mude o modelo, teste bem, a qualidade da tradução pode mudar dependendo do modelo. Recebe uma `str`

`de` - em qual linguagem vai estar o texto, padrão `en` (inglês). Recebe uma `str`

`para` - em qual lingua é pra traduzir. padrão `pt` (português). Recebe uma `str`

`retira` - um lista de listas com strings que contem textos com caracteres que representam o inicio e o final de uma variavel. Recebe uma `list[list[str, str], ]`

`ignorar` - uma lista com palavras que devem ser ignoradas pelo tradutor. recebe uma `list[str]`

`ignorar_sensivel` - se as letras maiusculas e minusculas devem ser ignoradas. Padrão `True`. Recebe um `bool`

`caminho` - caminho onde se encontra o arquivo para tradução. Padrão `None`. Recebe um `bool`

`reescrever` - se deve criar um arquivo igual para reescrever o texto original com a tradução. Padrão `True`. Recebe um `bool`

`regex` - se caso quiser aplicar um regex para traduzir apenas uma parte do texto. Padrão `''`. Recebe um `str`

`encoding` - codificação do arquivo, caso a codificação seja diferente. Padrão `utf-8`. Recebe um `str`

`max_thread` - quantidade maxima de traduções simultaneas. Padrão `1`, Recebe um `int`
