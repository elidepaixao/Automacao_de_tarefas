# O que a autoimação deve fazer?
# Abrir o navegador
# Acessar o site do sistema com login e senha
# Inserir todas as informações do produto
# Enviar as informações para o sistema
# Repetir o cadastro até acabar o cadastro de todos os produtos

#Passo 1: Entrar no sistema da empresa:  https://dlp.hashtagtreinamentos.com/python/intensivao/login


import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

#fazer login
# selecionar o campo de email


pyautogui.click(x=663, y=399) 
pyautogui.write("email@email.com")
pyautogui.press("tab")

#digitar a senha
pyautogui.write("senha1234")
pyautogui.click(x=701, y=569)

#abrindo a base de dados
tabela = pd.read_csv("produtos.csv")#atencao com o caminho do arquivo. como esta no mesmo lugar do codigo, nao precisa colocar o caminho completo
print(tabela)


#codigo do produto

for linha in tabela.index: #index corresponde as linhas da tabela, columns corresponde as colunas
  ##cadastrando os produtos:
  #primeiro verificar a posicao do click no primeiro campo:

    pyautogui.click(x=591, y=290)
    #em tabelas do python, para localizar uma informacao, coloca entre colchetes. Nesse exemplo, entre colchetes passa a linha e a coluna desejadas
    
    #codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #tipo do produto
    produto = tabela.loc[linha, "tipo"]
    pyautogui.write(str(produto))
    pyautogui.press("tab")
    #categoria do produto
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #preco unitario do produto
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    #custo do produto
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #obs - usar o if para verificar se tem ou nao obs
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    #enviar
    pyautogui.press("enter")

    #voltar para o inicio do cadastro
    pyautogui.scroll(5000) #numeros positivos, scroll para cima; negativos, scroll para baixo






