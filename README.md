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

## Classification
- Algoritmo de classificação funcional em notebooks/classif/2020_2

## Clustering
- Rodar algoritmo de clustering: python .\clusterizeDataset.py [num_de_clusters]
- Rodar servidor de sugestões: python .\recommendationAPI.py
