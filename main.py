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
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

#fazer login
# selecionar o campo de email

pyautogui.click(x=-898, y=580) 
pyautogui.write("email@email.com")
pyautogui.press("tab")

#digitar a senha
pyautogui.write("senha1234")
pyautogui.click(x=-943, y=752)





