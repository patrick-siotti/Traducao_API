import re
import os
import concurrent.futures
import threading
from time import sleep as sl
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

class TradutorTerminal:
    
    substituir = 'variavel'
    modelo_translate = 'facebook/m2m100_418M'
    de = 'en'
    para = 'pt'
    retira = []
    ignorar = []
    ignorar_sensivel = True
    caminho = None
    reescrever = True
    sep_pasta = '/'
    linhas = None
    regex = ''
    encoding = 'utf-8'
    max_thread = 1
    
    __global_sequenciamento = 1
    __lock = threading.Lock()
    __quantidade_atual = 0
    
    def __init__(self):
        # Inicializar modelo e tokenizador
        self.modelo = M2M100ForConditionalGeneration.from_pretrained(self.modelo_translate)
        self.tokenizador = M2M100Tokenizer.from_pretrained(self.modelo_translate)

    def traduzir_texto(self, texto_ingles, i):
        
        with self.__lock:
            
            texto_ingles_original = texto_ingles
            if self.regex:
                texto_ingles = re.findall(self.regex, texto_ingles)[0]
            else:
                texto_ingles = texto_ingles
            palavra = texto_ingles
            
            # print(f'\ntexto de entrada: {texto_ingles}')
            if self.__verifica_ignorar(texto_ingles):
                texto_ingles, substituicoes = self.__substituir_texto_entre_caracteres(texto_ingles, self.retira)
                traducao = self.__traduzir_texto_modelo(texto_ingles)
                traducao = self.__reinserir_texto(traducao, substituicoes)
                
            else:
                traducao = texto_ingles
            
            while i != self.__global_sequenciamento:
                self.__lock.wait()
                
            if self.reescrever:
                self.__reescrever_em_arquivo(traducao, palavra, texto_ingles_original)
            
            self.__global_sequenciamento += 1
            self.__quantidade_atual -= 1
            self.lock.notify_all()
            
            return traducao
    
    def traduzir_linhas_salvas(self):
        if self.linhas:
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                for i, linha in enumerate(self.linhas, start=1):
                    while True:
                        if self.__quantidade_atual < self.max_thread:
                            break
                        sl(1)
                    self.__quantidade_atual += 1
                        
                    # print('iniciando', i)    
                    executor.submit(self.traduzir_texto, linha, i)
        else:
            raise Exception('Não há nenhuma linhas salvas')

    def __verifica_ignorar(self, texto):
        if self.ignorar:
            if self.ignorar_sensivel:
                self.ignorar = list(map(lambda x: x.lower(), self.ignorar))
                texto = texto.lower()
            if texto in self.ignorar:
                return False
        return True

    def __substituir_texto_entre_caracteres(self, texto, retira):
        substituicoes = []
        for i, (inicio, fim) in enumerate(retira):
            padrao = "\\" + inicio + ".*?\\" + fim
            matches = re.findall(padrao, texto)
            for n, match in enumerate(matches):
                substituicoes.append((f'{self.substituir}{i+1+n}', match))
                texto = texto.replace(match, f'{self.substituir}{i+1+n}', 1)
        return texto, substituicoes

    def __reinserir_texto(self, texto, substituicoes):
        for variavel, substituicao in substituicoes:
            texto = texto.replace(variavel, substituicao)
        return texto

    def __traduzir_texto_modelo(self, texto):
        self.tokenizador.src_lang = self.de
        # print(f'texto para tradução: {texto}')
        encoded_english = self.tokenizador(texto, return_tensors=self.para)
        generated_tokens = self.modelo.generate(**encoded_english, forced_bos_token_id=self.tokenizador.lang_code_to_id[self.para])
        traducao = self.tokenizador.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return traducao
    
    def __reescrever_em_arquivo(self, traduzido, palavra, original):
        if self.caminho == None:
            raise ValueError('Nenhum caminho de arquivo foi informado!')
        if self.reescrever:
            diretorio = f'traduzido/{self.caminho.split(self.sep_pasta)[0]}'
            # Verifica se o diretório existe
            if not os.path.exists('traduzido'):
                # Se não existir, cria o diretório
                os.makedirs('traduzido')
            
            try:
                open(diretorio, 'r', encoding=self.encoding)
            except:
                open(diretorio, 'w', encoding=self.encoding)
                        
            with open(diretorio, 'a', encoding=self.encoding) as arquivo:
                txt = original.replace(palavra, traduzido)
                arquivo.write(f'{txt}')
                print(f'{traduzido} foi inserido no arquivo de tradução')
    
    def retira_texto_de_arquivo(self):
        if self.caminho == None:
            raise ValueError('Nenhum caminho de arquivo foi informado!')
        
        with open(self.caminho, 'r', encoding=self.encoding) as arquivo:
            linhas = arquivo.readlines()
        
        self.linhas = linhas

tradutor_terminal = TradutorTerminal()