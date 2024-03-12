# Modelo Facebook

nota de 0 a 10

como funciona? <br>
tempo: <quão rapido ele traduz>: quanto maior, melhor <br>
tradução: <qualidade da tradução>: quanto maior, melhor <br>
complexidade: <dificuldade de leitura e escrita do codigo>: quanto maior, melhor <br>

tempo: 8.5: <br>
tradução: 7: <br>
complexidade main: 9.5: <br>
complexidade modelo: 7.5: <br>

Este modelo é realmente bem bom, se caso for bem refinado ou caso consiga encontrar um modelo melhor, pode acabar sendo de bom uso. <br>
Ele pode ser usado mesmo offline, só tem que ser usado uma vez online para o download do modelo <br>
Conseguiria traduzir um jogo grande rapidamente <br>

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

# Modelo T5-Base

O T5-Base é uma versão menor do Text-To-Text Transfer Transformer (T5), desenvolvido pelo Google AI. Ele faz parte da família Transformer, que revolucionou o campo do processamento de linguagem natural (PLN) nos últimos anos.

## Especificações Técnicas:

- **Número de Parâmetros:** Aproximadamente 220 milhões.
- **Arquitetura:** Transformer.
- **Treinamento:** Realizado em uma grande quantidade de dados textuais.
- **Pré-treinamento:** O modelo é pré-treinado em uma variedade de tarefas de PLN, incluindo tradução de texto, sumarização, questionamento e resposta, entre outras.
- **Finetuning:** Pode ser finetunado para tarefas específicas de PLN, ajustando-se aos requisitos do projeto.
- **Desempenho Geral:** O T5-Base demonstra um bom desempenho em uma ampla variedade de tarefas de PLN, especialmente em tradução de texto.

## Como o T5-Base é Utilizado no Projeto:

O modelo T5-Base é utilizado como mecanismo de tradução de texto no projeto. Ele é capaz de receber um texto de entrada em um determinado idioma e gerar uma tradução para outro idioma de saída. O T5-Base é integrado ao projeto por meio da biblioteca Transformers, permitindo que seja facilmente utilizado para tarefas de tradução de texto em Python.

## Benefícios do Uso do T5-Base:

- **Versatilidade:** O T5-Base é capaz de lidar com uma variedade de tarefas de PLN, tornando-o uma escolha versátil para o projeto.
- **Desempenho:** O modelo oferece um bom desempenho em tradução de texto, proporcionando resultados de alta qualidade.
- **Facilidade de Uso:** A integração com a biblioteca Transformers simplifica o processo de utilização do modelo no projeto.

## Como Usar o Projeto:

Para utilizar o projeto e realizar traduções de texto com o modelo T5-Base, siga as instruções abaixo:

1. **Instalação:**

Certifique-se de ter o Python e o pip instalados em seu sistema. Em seguida, instale as dependências necessárias executando o seguinte comando no terminal:

pip install -r requirements.txt


Este comando instalará todas as bibliotecas Python necessárias, incluindo a biblioteca Transformers para trabalhar com o modelo T5-Base.

2. **Execução:**

Após instalar as dependências, você pode executar o projeto para realizar traduções de texto. Você pode optar por usar o script `translate.py` ou integrar o código diretamente em seu próprio projeto Python.

   - **Usando o script `translate.py`:**

     O script `translate.py` fornece uma interface simples para traduzir texto de um idioma de entrada para um idioma de saída específico. Para usar o script, execute o seguinte comando no terminal:

     ```
     python translate.py --input_file caminho/para/arquivo_de_entrada.txt --output_file caminho/para/arquivo_de_saida.txt --source_language código_do_idioma_de_entrada --target_language código_do_idioma_de_saída
     ```

     Substitua `caminho/para/arquivo_de_entrada.txt` pelo caminho para o arquivo de texto que você deseja traduzir e `caminho/para/arquivo_de_saida.txt` pelo caminho para o arquivo onde a tradução será salva. Além disso, especifique os códigos dos idiomas de entrada e saída conforme necessário.

   - **Integrando o código em seu próprio projeto:**

     Se preferir, você pode integrar o código diretamente em seu próprio projeto Python. Importe a função `translate_text` do módulo `translator` e utilize-a para realizar traduções de texto conforme necessário.

     ```python
     from translator import translate_text

     # Texto de entrada
     input_text = "Hello, world!"

     # Tradução para o idioma desejado
     translated_text = translate_text(input_text, source_language="en", target_language="fr")

     print("Texto Traduzido:", translated_text)
     ```

3. **Ajustes e Configurações:**

O projeto também oferece a flexibilidade de ajustes e configurações adicionais, como especificar o modelo de tradução, definir parâmetros de pré-processamento e pós-processamento, entre outros. Consulte a documentação do código-fonte para obter detalhes sobre as opções disponíveis.

## Projeto de Tradução de Texto com T5-Base

Este projeto visa implementar um sistema de tradução de texto utilizando o modelo T5-Base, uma implementação do Text-To-Text Transfer Transformer (T5) desenvolvido pelo Google AI. O sistema permite traduzir textos de um idioma de entrada para um idioma de saída, fornecendo uma solução flexível e eficaz para tarefas de tradução de texto.

## Funcionalidades Principais:

- **Tradução de Texto:** O sistema é capaz de traduzir textos de entrada em um idioma específico para um idioma de saída desejado.
- **Detecção Automática de Idioma:** Utiliza técnicas avançadas para detectar automaticamente o idioma do texto de entrada, facilitando o processo de tradução.
- **Suporte a Múltiplos Idiomas:** Oferece suporte a uma ampla variedade de idiomas, permitindo traduzir textos em diferentes línguas.
- **Qualidade da Tradução:** Utiliza o modelo T5-Base, conhecido por seu desempenho robusto e resultados de alta qualidade em tarefas de processamento de linguagem natural.

## Como Utilizar o Sistema:

1. **Instalação das Dependências:**

   Certifique-se de ter o PyTorch e a biblioteca Transformers instalados no seu ambiente Python. Você pode instalá-los utilizando o seguinte comando:

pip install torch transformers


2. **Execução do Código:**

Clone o repositório do projeto e navegue até o diretório raiz. Execute o script principal do projeto, fornecendo o texto de entrada e o idioma de destino como argumentos:

python translate.py --input_text "Seu texto de entrada aqui" --target_language "en"


O texto traduzido será exibido no console.

## Exemplo de Uso:

```python
from translator import translate_text

input_text = "Bonjour tout le monde"
target_language = "en"

translated_text = translate_text(input_text, target_language)
print("Texto Traduzido:", translated_text)

Detalhes Técnicos do T5-Base
O modelo T5-Base é uma implementação do Text-To-Text Transfer Transformer (T5), desenvolvido pelo Google AI. Abaixo estão os detalhes técnicos do T5-Base:

Arquitetura: O T5-Base utiliza a arquitetura Transformer, uma rede neural que se destacou em uma variedade de tarefas de processamento de linguagem natural (PLN).
Número de Parâmetros: O modelo T5-Base possui aproximadamente 220 milhões de parâmetros.
Treinamento: Foi treinado em uma ampla variedade de dados textuais multilíngues para capturar a complexidade e diversidade da linguagem.
Pré-Treinamento e Ajuste Fino: O T5-Base pode ser pré-treinado em grandes conjuntos de dados textuais e ajustado finamente para tarefas específicas de PLN.
Desempenho: Demonstrou competência em diversas tarefas de PLN, incluindo tradução de texto, sumarização, geração de texto e muito mais.
Melhorias e Recursos Futuros
Detecção de Linguagem: Adicionar recursos de detecção automática de idioma para identificar o idioma do texto de entrada.
Controle de Qualidade: Implementar técnicas de controle de qualidade para garantir traduções precisas e de alta qualidade.
Suporte a Mais Idiomas: Ampliar o suporte a uma variedade maior de idiomas para atender às necessidades globais.
Integração com Outros Modelos: Explorar a integração com outros modelos de PLN para oferecer opções adicionais aos usuários.
Licença
Este projeto é licenciado sob a MIT License.


# Detalhes Técnicos do Modelo T5-Base

O T5-Base é uma versão menor do Text-To-Text Transfer Transformer (T5), desenvolvido pelo Google AI. Ele faz parte da família Transformer, que revolucionou o campo do processamento de linguagem natural (PLN) nos últimos anos.

## Especificações Técnicas:

- **Número de Parâmetros:** Aproximadamente 220 milhões.
- **Arquitetura:** Transformer.
- **Treinamento:** Realizado em uma grande quantidade de dados textuais.
- **Pré-treinamento:** O modelo é pré-treinado em uma variedade de tarefas de PLN, incluindo tradução de texto, sumarização, questionamento e resposta, entre outras.
- **Finetuning:** Pode ser finetunado para tarefas específicas de PLN, ajustando-se aos requisitos do projeto.

## Desempenho Geral:

O T5-Base demonstra um bom desempenho em uma ampla variedade de tarefas de PLN, especialmente em tradução de texto.

Agora, vamos adicionar o código fornecido anteriormente para a classe T5Translator e os exemplos de uso:

# Tradução com T5-Base

Este é um exemplo de como usar o modelo T5-Base para tradução de texto. O T5-Base é uma versão menor do Text-To-Text Transfer Transformer (T5), desenvolvido pelo Google AI, que demonstra um bom desempenho em uma ampla variedade de tarefas de Processamento de Linguagem Natural (PLN).

## Código Python para Tradução com T5-Base

```python
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

class T5Translator:
    def __init__(self, model_name="t5-base", device="cpu"):
        self.model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.device = device
    
    def translate(self, text, target_language="pt"):
        self.model.eval()
        with torch.no_grad():
            inputs = self.tokenizer.encode(text, return_tensors="pt").to(self.device)
            outputs = self.model.generate(inputs, max_length=100, num_beams=4, early_stopping=True, 
                                          num_return_sequences=1, decoder_start_token_id=self.tokenizer.pad_token_id, 
                                          forced_bos_token_id=self.tokenizer.pad_token_id, 
                                          forced_eos_token_id=self.tokenizer.eos_token_id, 
                                          use_cache=True, do_sample=False)
            translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated_text

# Exemplo de uso
translator = T5Translator()

# Texto para traduzir
text_to_translate = "Hello, how are you?"

# Traduzindo o texto
translated_text = translator.translate(text_to_translate, target_language="pt")

# Imprimindo os resultados
print("Texto Original:", text_to_translate)
print("Texto Traduzido:", translated_text)

Funcionamento
Este código Python utiliza a biblioteca transformers da Hugging Face para carregar o modelo T5-Base pré-treinado e o tokenizer correspondente. Em seguida, define uma classe T5Translator que encapsula a lógica de tradução usando o modelo T5-Base. O método translate() desta classe recebe um texto de entrada e retorna a tradução para o idioma especificado (por padrão, português).

Ajuste Fino (Fine-Tuning)
O modelo T5-Base pode ser ajustado fino para tarefas específicas de PLN, como tradução de textos em domínios específicos. Isso requer treinamento adicional com conjuntos de dados específicos e pode melhorar a qualidade das traduções em contextos específicos.

Requisitos de Instalação
Antes de executar o código, é necessário instalar as dependências usando o seguinte comando:

pip install torch transformers

Considerações Finais
Este exemplo mostra apenas uma utilização básica do modelo T5-Base para tradução de texto. Experimente com diferentes textos e idiomas para explorar mais as capacidades do modelo.


Este arquivo Markdown fornece uma visão geral do código Python para tradução usando o modelo T5-Base, explica como o código funciona, discute opções de ajuste fino, fornece instruções de instalação e oferece considerações finais.


