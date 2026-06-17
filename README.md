# Olá Mundo DB: Bancos de Dados Vetoriais

Alunos: Lucas Garzuze Cordeiro & Sabrina Dorigoni

## Propósito

O projeto irá consistir em arquivos python que utilizam a biblioteca do Chroma para implementar um pequeno sistema
de busca semântica. O banco será populado com dados de produtos e os usuários serão capazes de realizar consultas, em 
linguagem natural, acerca de suas necessidades ou desejos de compra. O sistema, então, irá realizar uma busca vetorial 
para achar produtos que estejam relacionados a tal consulta e retornará para o usuário. O ponto central da aplicação é 
demonstrar que a busca retorna resultados relevantes mesmo quando nenhuma query aparece nos documentos.

## Pré-requisitos

- Python 3.9+

## Instalação

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

## Executando

Passo 1: popula o banco (executar apenas uma vez)

```
python src/populate_db.py
```

Passo 2: realiza buscas semânticas

```
python src/search.py
```
