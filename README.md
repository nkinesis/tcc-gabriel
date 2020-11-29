# TCC - Gabriel C. Ullmann

## Descrição
Geração de sugestões de produtos através de IA com base no histórico de compras de clientes em um e-commerce

## Instalação
- Baixe o Python 3.7.x (https://www.python.org/downloads/)
- Instale as dependências (pip install -r requirements.txt)
- Instale o MongoDB (https://www.mongodb.com/try/download/community)

## Estrutura
- Pasta "data" contém datasets utilizados
- Pasta "notebooks" contém código em formato .ipynb que pode ser executado no editor interativo Jupyter (https://jupyter.org/)
- Pasta "src" contém código no formato .py que pode ser executado da linha de comando

# Referência de comandos e rotinas

## Classification
- Algoritmo de classificação funcional em notebooks/classif/2020_2

## Clustering
- Rodar algoritmo de clustering: python .\clusterizeDataset.py [num_de_clusters]
- Rodar servidor de sugestões: python .\recommendationAPI.py

## Registrar comandos
- Executar "nano .bashrc" dentro da pasta /home/username


    alias tcc-activate='source /home/ullmann/envs/bin/activate'
    alias tcc-gotorepo='cd /home/ullmann/tcc-gabriel'
    alias tcc-gototest='cd /home/ullmann/tcc-gabriel/src/classif/2020_2/recomm'

## Executar processos no ssh
- Conectar utilizando o comando "ssh usuario@servidor"
- Digite "screen"
- Inicie o processo desejado
- Pressione Ctrl-A e depois Ctrl-D. Isso irá separar a sessão do "screen"
- Faça logout
- Ao logar novamente, digite "screen -r" para voltar ao processo
