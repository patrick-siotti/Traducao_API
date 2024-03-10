from modelo import tradutor_terminal as modelo

# jogo escolhido pro teste: Crusader Kings 2
# arquivo de tradução escolhido: CombatUpdate.csv
# arquivo primario de execução

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