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

#cadastrando os produtos:
#para cada linha vamos cadastrar um produto

for linha in tabela.index:
    pyautogui.click(x=200, y=200) #clicar no campo nome do produto
    pyautogui.write(tabela["nome"][linha])
    pyautogui.press("tab")
    pyautogui.write(str(tabela["valor"][linha]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela["quantidade"][linha]))
    pyautogui.press("tab")
    pyautogui.write(tabela["categoria"][linha])
    pyautogui.press("tab")
    pyautogui.press("enter") #clicar no botao cadastrar
    time.sleep(2)




