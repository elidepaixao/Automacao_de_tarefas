# Automação de Cadastro de Produtos
# ==================================
# Este script automatiza o processo de cadastro de produtos em um sistema web.
# A automação lê dados de um arquivo CSV e preenche formulários web automaticamente.

# Funcionalidades:
# - Abre o navegador Chrome
# - Acessa o sistema e realiza login
# - Lê produtos de um arquivo CSV
# - Cadastra cada produto automaticamente
# - Repete o processo para todos os produtos da base de dados

import pandas as pd
import pyautogui
import time

# Define o intervalo de pausa entre cada comando do PyAutoGUI (em segundos)
# Isso evita que os comandos sejam executados rápido demais
pyautogui.PAUSE = 0.5

# PASSO 1: ABRIR O NAVEGADOR E ACESSAR O SISTEMA
## Pressiona a tecla Windows para abrir o menu iniciar

pyautogui.press("win")
time.sleep(1)

## Digita "chrome" para buscar o navegador e pressiona Enter para abrir o Chrome
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)

##Digita a URL do sistema e acessa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# PASSO 2: REALIZAR LOGIN NO SISTEMA

## Clica no campo de email (coordenadas x=663, y=399)
## ATENÇÃO: Essas coordenadas podem variar dependendo da resolução da tela
pyautogui.click(x=663, y=399) 
pyautogui.write("email@email.com")
pyautogui.press("tab")

#digitar a senha
pyautogui.write("senha1234")
pyautogui.click(x=701, y=569)

#PASSO 3: IMPORTAR A BASE DE DADOS DE PRODUTOS

# Lê o arquivo CSV contendo os produtos a serem cadastrados
# O arquivo deve estar na mesma pasta que o script
tabela = pd.read_csv("produtos.csv")

# Exibe a tabela no console para conferência
print(tabela)

# PASSO 4: CADASTRAR TODOS OS PRODUTOS DA BASE DE DADOS

## Loop que percorre cada linha (produto) da tabela
## tabela.index retorna todas as linhas da tabela, para colunas usar tabela.columns
for linha in tabela.index:

    #Clica no primeiro campo do formulário (campo de código)
    pyautogui.click(x=591, y=290)

    # CAMPO 1: CÓDIGO DO PRODUTO
    ## Para acessar informações em tabelas do Python, use colchetes com a linha e coluna desejadas.

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # CAMPO 2: MARCA DO PRODUTO
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    # CAMPO 3: TIPO DO PRODUTO
    produto = str(tabela.loc[linha, "tipo"])
    pyautogui.write(produto)
    pyautogui.press("tab")
    # CAMPO 4: CATEGORIA DO PRODUTO
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #CAMPO 5: PREÇO UNITÁRIO DO PRODUTO
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    # CAMPO 6: CUSTO DO PRODUTO
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    # CAMPO 7: OBSERVAÇÕES (OPCIONAL)
    # Verifica se existe observação para o produto
    # Se a célula estiver vazia, o pandas retorna "nan
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    #enviar
    pyautogui.press("enter")

    # Faz scroll para cima para voltar ao início do formulário
    # Valores positivos = scroll para cima; valores negativos = scroll para baixo
    pyautogui.scroll(5000) #numeros positivos, scroll para cima; negativos, scroll para baixo

    # FIM DA AUTOMAÇÃO




