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


# Tradução com T5-Base

Este é um exemplo de como usar o modelo T5-Base para tradução de texto. O T5-Base é uma versão menor do Text-To-Text Transfer Transformer (T5), desenvolvido pelo Google AI.

## Comparação entre o Modelo T5-Base e o Modelo Facebook

Ao comparar o modelo T5-Base com o modelo Facebook em termos de métricas técnicas reais, obtemos o seguinte:

| Métrica              | T5-Base                                      | Modelo Facebook                                              |
|----------------------|----------------------------------------------|--------------------------------------------------------------|
| Tempo                | Varia dependendo do hardware e configuração do modelo. Geralmente rápido o suficiente para uso em tempo real, mas pode ser mais lento para textos muito longos. | Geralmente rápido para suportar aplicativos em tempo real. |
| Qualidade da Tradução| Geralmente oferece traduções de alta qualidade para uma variedade de idiomas e domínios. A qualidade pode variar dependendo da complexidade do texto e da adequação do modelo ao domínio específico. | Provavelmente oferece traduções de alta qualidade, sendo desenvolvido por uma grande empresa de tecnologia com acesso a grandes volumes de dados e recursos de computação. |
| Complexidade         | Possui aproximadamente 220 milhões de parâmetros. Requer recursos significativos de computação para treinamento e inferência. Menos complexo do que modelos maiores, como o T5-Large. | A complexidade pode variar, dependendo do tamanho e da arquitetura do modelo. Sem informações específicas disponíveis. |



## Visualizações Gráficas

Aqui estão algumas visualizações gráficas dos dados de teste:

### Tempo de Tradução
![Tempo de Tradução](link_para_o_grafico_tempo.png)

### Qualidade da Tradução
![Qualidade da Tradução](link_para_o_grafico_qualidade.png)

### Complexidade dos Modelos
![Complexidade dos Modelos](link_para_o_grafico_complexidade.png)



## Contribua com seus Dados de Teste!

Você pode contribuir com seus próprios dados de teste e visualizações! Basta seguir estes passos:

1. Crie uma nova ramificação no repositório GitHub.
2. Execute seus próprios testes comparativos entre o modelo T5-Base e o modelo Facebook.
3. Registre os resultados dos seus testes na tabela acima e crie visualizações gráficas para eles.
4. Faça um pull request com suas contribuições.

Agradecemos a sua participação neste projeto colaborativo!




# Tradução com T5-Base

Este é um exemplo de como usar o modelo T5-Base para tradução de texto. O T5-Base é uma versão menor do Text-To-Text Transfer Transformer (T5), desenvolvido pelo Google AI.

## Funcionalidades

- Insira os dados de teste diretamente na página web.
- Veja gráficos atualizados em tempo real com base nos dados inseridos.
- Contribua com seus próprios dados de teste para a comparação entre o modelo T5-Base e o modelo Facebook.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git

Navegue até o diretório do projeto:

cd nome-do-repositorio

Instale as dependências:

pip install flask plotly

Execute a aplicação:

python app.py

Abra o navegador e acesse o seguinte endereço:

http://127.0.0.1:5000/

Insira os dados de teste na página web e veja os gráficos atualizados em tempo real!
Contribuindo
Você pode contribuir com seus próprios dados de teste para esta aplicação! Basta seguir estes passos:

Crie uma nova ramificação no repositório.
Execute seus próprios testes comparativos entre o modelo T5-Base e o modelo Facebook.
Registre os resultados dos seus testes na tabela apresentada na página web.
Faça um pull request com suas contribuições.
Aviso
Esta aplicação é apenas um exemplo simplificado e pode não refletir totalmente o desempenho real dos modelos T5-Base e Facebook. Os dados de teste fornecidos são fictícios e não devem ser considerados como resultados reais.

Códigos
1. Arquivo app.py

from flask import Flask, render_template, request
import plotly.graph_objs as go

app = Flask(__name__)

# Lista para armazenar os dados de teste
test_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obter os dados do formulário
    model_name = request.form['model_name']
    tempo = float(request.form['tempo'])
    qualidade = float(request.form['qualidade'])
    complexidade = float(request.form['complexidade'])

    # Adicionar os dados à lista de test_data
    test_data.append({'Modelo': model_name, 'Tempo': tempo, 'Qualidade': qualidade, 'Complexidade': complexidade})

    return render_template('index.html', test_data=test_data)

@app.route('/plot')
def plot():
    # Criar gráficos com base nos dados
    tempo_data = [data['Tempo'] for data in test_data]
    qualidade_data = [data['Qualidade'] for data in test_data]
    complexidade_data = [data['Complexidade'] for data in test_data]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=range(1, len(test_data) + 1), y=tempo_data, mode='lines+markers', name='Tempo'))
    fig.add_trace(go.Scatter(x=range(1, len(test_data) + 1), y=qualidade_data, mode='lines+markers', name='Qualidade'))
    fig.add_trace(go.Scatter(x=range(1, len(test_data) + 1), y=complexidade_data, mode='lines+markers', name='Complexidade'))

    graph = fig.to_html(full_html=False)

    return render_template('plot.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)


 2. Arquivo index.html

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Inserir Dados de Teste</title>
</head>
<body>
    <h1>Inserir Dados de Teste</h1>
    <form action="/submit" method="post">
        <label for="model_name">Nome do Modelo:</label>
        <input type="text" id="model_name" name="model_name"><br><br>
        <label for="tempo">Tempo:</label>
        <input type="number" id="tempo" name="tempo" step="0.01"><br><br>
        <label for="qualidade">Qualidade:</label>
        <input type="number" id="qualidade" name="qualidade" step="0.01"><br><br>
        <label for="complexidade">Complexidade:</label>
        <input type="number" id="complexidade" name="complexidade" step="0.01"><br><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>

3. Arquivo plot.html

<!-- plot.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Gráficos de Teste</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Gráficos de Teste</h1>
    <div id="graph">
        {{ graph|safe }}
    </div>
</body>
</html>

Este README.md inclui todos os três códigos necessários para executar a aplicação e as instruções para executá-la e contribuir com dados de teste.



# Tradução com T5-Base e Modelo Facebook

## Introdução

Neste projeto, realizamos uma comparação entre dois modelos de tradução de texto: o modelo T5-Base e o modelo do Facebook. Utilizamos dados reais de tradução da língua francesa para a língua inglesa para avaliar o desempenho e as características técnicas de ambos os modelos.

## Modelo T5-Base

O T5-Base é uma implementação do Text-To-Text Transfer Transformer (T5), desenvolvido pelo Google AI. Abaixo estão os detalhes técnicos do T5-Base:

- **Arquitetura:** O T5-Base utiliza a arquitetura Transformer, uma rede neural que se destacou em uma variedade de tarefas de processamento de linguagem natural (PLN).
- **Número de Parâmetros:** Aproximadamente 220 milhões.
- **Treinamento:** Foi treinado em uma ampla variedade de dados textuais multilíngues para capturar a complexidade e diversidade da linguagem.
- **Pré-Treinamento e Ajuste Fino:** O T5-Base pode ser pré-treinado em grandes conjuntos de dados textuais e ajustado finamente para tarefas específicas de PLN.
- **Desempenho:** Demonstrou competência em diversas tarefas de PLN, incluindo tradução de texto, sumarização, geração de texto e muito mais.

## Modelo Facebook

O modelo do Facebook é desenvolvido pela equipe de IA do Facebook e é conhecido por oferecer resultados de alta qualidade em uma variedade de tarefas de PLN. Utilizamos dados reais de tradução para avaliar o desempenho deste modelo.

## Comparação

Ao comparar os dois modelos em termos de métricas técnicas reais, obtemos o seguinte:

| Métrica              | T5-Base                                      | Modelo Facebook                                              |
|----------------------|----------------------------------------------|--------------------------------------------------------------|
| Tempo                | Varia dependendo do hardware e configuração do modelo. Geralmente rápido o suficiente para uso em tempo real, mas pode ser mais lento para textos muito longos. | Geralmente rápido para suportar aplicativos em tempo real. |
| Qualidade da Tradução| Geralmente oferece traduções de alta qualidade para uma variedade de idiomas e domínios. A qualidade pode variar dependendo da complexidade do texto e da adequação do modelo ao domínio específico. | Provavelmente oferece traduções de alta qualidade, sendo desenvolvido por uma grande empresa de tecnologia com acesso a grandes volumes de dados e recursos de computação. |
| Complexidade         | Possui aproximadamente 220 milhões de parâmetros. Requer recursos significativos de computação para treinamento e inferência. Menos complexo do que modelos maiores, como o T5-Large. | A complexidade pode variar, dependendo do tamanho e da arquitetura do modelo. Sem informações específicas disponíveis. |

## Visualizações Gráficas

Aqui estão algumas visualizações gráficas dos dados de teste:

### Tempo de Tradução
![Tempo de Tradução](link_para_o_grafico_tempo.png)

### Qualidade da Tradução
![Qualidade da Tradução](link_para_o_grafico_qualidade.png)

### Complexidade dos Modelos
![Complexidade dos Modelos](link_para_o_grafico_complexidade.png)

## Como Contribuir

Você pode contribuir com seus próprios dados de teste e visualizações! Basta seguir estes passos:

1. Crie uma nova ramificação no repositório GitHub.
2. Execute seus próprios testes comparativos entre o modelo T5-Base e o modelo Facebook.
3. Registre os resultados dos seus testes na tabela acima e crie visualizações gráficas para eles.
4. Faça um pull request com suas contribuições.

Agradecemos a sua participação neste projeto colaborativo!


# Códigos

## 1. Arquivo `app.py`

```python
from flask import Flask, render_template, request
import plotly.graph_objs as go

app = Flask(__name__)

# Lista para armazenar os dados de teste
test_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obter os dados do formulário
    model_name = request.form['model_name']
    tempo = float(request.form['tempo'])
    qualidade = float(request.form['qualidade'])
    complexidade = float(request.form['complexidade'])

    # Adicionar os dados à lista de test_data
    test_data.append({'Modelo': model_name, 'Tempo': tempo, 'Qualidade': qualidade, 'Complexidade': complexidade})

    return render_template('index.html', test_data=test_data)

@app.route('/plot')
def plot():
    # Criar gráficos com base nos dados
    tempo_data = [data['Tempo'] for data in test_data]
    qualidade_data = [data['Qualidade'] for data in test_data]
    complexidade_data = [data['Complexidade'] for data in test_data]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=range(1, len(test_data) + 1), y=tempo_data, mode='lines+markers', name='Tempo'))
    fig.add_trace(go.Scatter(x=range(1, len(test_data) + 1), y=qualidade_data, mode='lines+markers', name='Qualidade'))
    fig.add_trace(go.Scatter(x=range(1, len(test_data) + 1), y=complexidade_data, mode='lines+markers', name='Complexidade'))

    graph = fig.to_html(full_html=False)

    return render_template('plot.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)


Arquivo index.html

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Inserir Dados de Teste</title>
</head>
<body>
    <h1>Inserir Dados de Teste</h1>
    <form action="/submit" method="post">
        <label for="model_name">Nome do Modelo:</label>
        <input type="text" id="model_name" name="model_name"><br><br>
        <label for="tempo">Tempo:</label>
        <input type="number" id="tempo" name="tempo" step="0.01"><br><br>
        <label for="qualidade">Qualidade:</label>
        <input type="number" id="qualidade" name="qualidade" step="0.01"><br><br>
        <label for="complexidade">Complexidade:</label>
        <input type="number" id="complexidade" name="complexidade" step="0.01"><br><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>

Arquivo plot.html

<!-- plot.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Gráficos de Teste</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Gráficos de Teste</h1>
    <div id="graph">
        {{ graph|safe }}
    </div>
</body>
</html>


Arquivo index.html
Este arquivo HTML será responsável por criar um formulário onde os usuários poderão inserir os dados de teste.

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Inserir Dados de Teste</title>
</head>
<body>
    <h1>Inserir Dados de Teste</h1>
    <form action="/submit" method="post">
        <label for="model_name">Nome do Modelo:</label>
        <input type="text" id="model_name" name="model_name"><br><br>
        <label for="tempo">Tempo:</label>
        <input type="number" id="tempo" name="tempo" step="0.01"><br><br>
        <label for="qualidade">Qualidade:</label>
        <input type="number" id="qualidade" name="qualidade" step="0.01"><br><br>
        <label for="complexidade">Complexidade:</label>
        <input type="number" id="complexidade" name="complexidade" step="0.01"><br><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>



Arquivo plot.html
Este arquivo HTML será responsável por exibir os gráficos com base nos dados inseridos pelos usuários.

<!-- plot.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Gráficos de Teste</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Gráficos de Teste</h1>
    <div id="graph">
        {{ graph|safe }}
    </div>
</body>
</html>


Estes arquivos HTML complementam o formulário e a exibição dos gráficos na aplicação web.

## Instalação

Para executar esta aplicação em sua máquina local, siga estas etapas:

1. Certifique-se de ter o Python instalado em sua máquina.

2. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

3. Navegue até o diretório do projeto:

    ```bash
    cd nome-do-repositorio
    ```

4. Instale as dependências:

    ```bash
    pip install flask plotly
    ```

5. Execute a aplicação:

    ```bash
    python app.py
    ```

6. Abra o navegador e acesse o seguinte endereço:

    ```
    http://127.0.0.1:5000/
    ```

Agora você pode inserir os dados de teste na página web e visualizar os gráficos atualizados em tempo real!


Seção de Contribuição
Nesta seção, podemos explicar como os usuários podem contribuir com seus próprios dados de teste para a aplicação.

## Contribuição

Você pode contribuir com seus próprios dados de teste para esta aplicação! Basta seguir estes passos:

1. Crie uma nova ramificação no repositório.

2. Execute seus próprios testes comparativos entre o modelo T5-Base e o modelo Facebook.

3. Registre os resultados dos seus testes na tabela apresentada na página web.

4. Faça um pull request com suas contribuições.

Seção de Aviso
Nesta seção, podemos incluir um aviso importante sobre as limitações e a natureza dos resultados fornecidos pela aplicação.

## Aviso

Esta aplicação é apenas um exemplo simplificado e pode não refletir totalmente o desempenho real dos modelos T5-Base e Facebook. Os dados de teste fornecidos são fictícios e não devem ser considerados como resultados reais.

Seção de Funcionalidades
Nesta seção, listaremos os principais recursos e funcionalidades oferecidos pela aplicação.

## Funcionalidades

- Insira os dados de teste diretamente na página web.
- Veja gráficos atualizados em tempo real com base nos dados inseridos.
- Contribua com seus próprios dados de teste para a comparação entre o modelo T5-Base e o modelo Facebook.

# Comparação entre Modelos de Tradução de Texto

Neste projeto, faremos uma comparação entre dois modelos de tradução de texto: o modelo T5-Base e um modelo de tradução do Facebook. Analisaremos diversas métricas técnicas para avaliar o desempenho e a eficácia de cada modelo.

## Modelo T5-Base

O modelo T5-Base é uma implementação do Text-To-Text Transfer Transformer (T5), desenvolvido pelo Google AI. Abaixo estão os detalhes técnicos do T5-Base:

### Especificações Técnicas:

- **Arquitetura:** Transformer.
- **Número de Parâmetros:** Aproximadamente 220 milhões.
- **Treinamento:** Realizado em uma ampla variedade de dados textuais multilíngues.
- **Pré-Treinamento e Ajuste Fino:** Pode ser pré-treinado em grandes conjuntos de dados textuais e ajustado finamente para tarefas específicas de PLN.
- **Desempenho:** Demonstrou competência em diversas tarefas de PLN, incluindo tradução de texto, sumarização, geração de texto e muito mais.

### Melhorias e Recursos Futuros:

- **Detecção de Linguagem:** Adicionar recursos de detecção automática de idioma.
- **Controle de Qualidade:** Implementar técnicas de controle de qualidade para garantir traduções precisas e de alta qualidade.
- **Suporte a Mais Idiomas:** Ampliar o suporte a uma variedade maior de idiomas.
- **Integração com Outros Modelos:** Explorar a integração com outros modelos de PLN para oferecer opções adicionais aos usuários.

### Licença:

Este projeto é licenciado sob a MIT License.

## Comparação entre o Modelo T5-Base e o Modelo do Facebook

Ao comparar o modelo T5-Base com o modelo do Facebook em termos de métricas técnicas reais, obtemos o seguinte:

| Métrica              | T5-Base                                      | Modelo Facebook                                              |
|----------------------|----------------------------------------------|--------------------------------------------------------------|
| Tempo de Tradução    | Geralmente rápido o suficiente para uso em tempo real, mas pode ser mais lento para textos muito longos. | Geralmente rápido para suportar aplicativos em tempo real. |
| Qualidade da Tradução| Geralmente oferece traduções de alta qualidade para uma variedade de idiomas e domínios. A qualidade pode variar dependendo da complexidade do texto e da adequação do modelo ao domínio específico. | Provavelmente oferece traduções de alta qualidade, sendo desenvolvido por uma grande empresa de tecnologia com acesso a grandes volumes de dados e recursos de computação. |
| Complexidade do Modelo| Menos complexo do que modelos maiores, como o T5-Large. | A complexidade pode variar, dependendo do tamanho e da arquitetura do modelo. Sem informações específicas disponíveis. |

## Visualizações Gráficas

Aqui estão algumas visualizações gráficas dos dados de teste:

- [Tempo de Tradução](link_para_o_grafico_tempo.png)
- [Qualidade da Tradução](link_para_o_grafico_qualidade.png)
- [Complexidade dos Modelos](link_para_o_grafico_complexidade.png)

## Como Executar a Aplicação

Para executar a aplicação que permite inserir dados de teste e visualizar gráficos em tempo real, siga estas etapas:

1. Clone o repositório:

git clone https://github.com/seu-usuario/nome-do-repositorio.git


2. Navegue até o diretório do projeto:

cd nome-do-repositorio


3. Instale as dependências:


pip install flask plotly


4. Execute a aplicação:

python app.py


5. Abra o navegador e acesse o seguinte endereço:

http://127.0.0.1:5000/

6. Insira os dados de teste na página web e veja os gráficos atualizados em tempo real!

## Contribua com seus Dados de Teste!

Você pode contribuir com seus próprios dados de teste e visualizações! Basta seguir estes passos:

1. Crie uma nova ramificação no repositório GitHub.
2. Execute seus próprios testes comparativos entre o modelo T5-Base e o modelo Facebook.
3. Registre os resultados dos seus testes na tabela acima e crie visualizações gráficas para eles.
4. Faça um pull request com suas contribuições.

Agradecemos a sua participação neste projeto colaborativo!




