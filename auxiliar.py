# Script Auxiliar para Desenvolvimento da Automação
# ==================================================
# Este script ajuda a identificar coordenadas do mouse e visualizar a estrutura dos dados.

# Funcionalidades:
# - Captura a posição atual do mouse na tela (coordenadas x, y)
# - Exibe a estrutura da tabela de produtos para referência

# Como usar:
# 1. Execute o script
# 2. Mova o mouse para o elemento desejado na tela
# 3. Aguarde 5 segundos
# 4. As coordenadas serão exibidas no console

import pyautogui
import time
import pandas as pd

# Aguarda 5 segundos para você posicionar o mouse 
time.sleep(5)

# Captura e exibe a posição atual do mouse (coordenadas x e y)
# Use essas coordenadas no script principal para clicar no campo desejado


# ESTRUTURA DA TABELA DE PRODUTOS (PARA REFERÊNCIA)

#  codigo       marca        tipo  categoria  preco_unitario  custo               obs
# 0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
# 1    MOLO000192    Logitech       Mouse          2           19.95    5.0               NaN
# 2    CAHA000251     Hashtag      Camisa          1           25.00   11.0               NaN
# 3    CAHA000252     Hashtag      Camisa          2           25.00   11.0  Conferir estoque
# 4    MOMU000111  Multilaser       Mouse          1           11.99    3.4               NaN
# ..          ...         ...         ...        ...             ...    ...               ...
# 288  ACAP000192       Apple  Acessorios          2           19.00    3.8               NaN
# 289  ACSA0009.3     Samsung  Acessorios          3            9.55    2.1               NaN
# 290  CEMO000271    Motorola     Celular          1          279.00   72.5               NaN
# 291  FOMO000152    Motorola        Fone          2          150.00   33.0               NaN
# 292  CEMO000223    Motorola     Celular          3          229.00   55.0               NaN

