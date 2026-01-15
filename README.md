#  Automação de Cadastro de Produtos

Projeto de automação em Python que realiza o cadastro automático de produtos em um sistema web, lendo dados de um arquivo CSV e preenchendo formulários de forma autônoma.

##  Descrição

Este projeto automatiza o processo repetitivo de cadastro de produtos em um sistema web. A automação é capaz de:

1. Abrir o navegador Chrome automaticamente
2. Acessar o sistema e realizar login
3. Ler uma base de dados de produtos (arquivo CSV)
4. Preencher e enviar formulários de cadastro para cada produto
5. Processar centenas de produtos sem intervenção manual

##  Funcionalidades

- **Login Automático**: Acessa o sistema e faz login com credenciais predefinidas
- **Leitura de Dados**: Importa produtos de um arquivo CSV usando Pandas
- **Preenchimento Inteligente**: Preenche todos os campos do formulário automaticamente
- **Validação de Dados**: Verifica campos opcionais antes de preencher
- **Processamento em Lote**: Cadastra múltiplos produtos sequencialmente

##  Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal do projeto
- **PyAutoGUI**: Automação de interface gráfica (cliques e digitação)
- **Pandas**: Manipulação e leitura de dados CSV
- **Time**: Controle de intervalos entre ações

##  Estrutura do Projeto

projeto-automacao/
│
├── main.py              # Script principal da automação
├── auxiliar.py          # Script auxiliar para desenvolvimento
├── produtos.csv         # Base de dados com produtos (não incluído)
├── requirements.txt     # Dependências do projeto
├── .gitignore          # Arquivos ignorados pelo Git
└── README.md           # Documentação do projeto