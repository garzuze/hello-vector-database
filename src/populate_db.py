import chromadb
from config import DB_PATH, COLLECTION_NAME

PRODUTOS = [
    {
        "id": "p001",
        "documento": "Tênis de corrida leve, com solado amortecido, ideal para treinos de longa distância.",
        "categoria": "esporte",
        "preco": 349.90,
    },
    {
        "id": "p002",
        "documento": "Bicicleta de montanha com quadro em alumínio, suspensão dianteira e 21 marchas.",
        "categoria": "esporte",
        "preco": 1899.00,
    },
    {
        "id": "p003",
        "documento": "Notebook ultrafino com 16GB de RAM, ótimo para trabalho remoto e estudos.",
        "categoria": "eletronicos",
        "preco": 4299.00,
    },
    {
        "id": "p004",
        "documento": "Fone de ouvido sem fio com cancelamento de ruído, bateria de longa duração.",
        "categoria": "eletronicos",
        "preco": 599.90,
    },
    {
        "id": "p005",
        "documento": "Jogo de panelas antiaderentes em aço inox, conjunto com 5 peças para o dia a dia na cozinha.",
        "categoria": "casa",
        "preco": 459.00,
    },
    {
        "id": "p006",
        "documento": "Aspirador de pó robô com mapeamento automático do ambiente e controle por aplicativo.",
        "categoria": "casa",
        "preco": 1299.00,
    },
    {
        "id": "p007",
        "documento": "Romance de ficção científica sobre exploração espacial e contato com civilizações alienígenas.",
        "categoria": "livros",
        "preco": 39.90,
    },
    {
        "id": "p008",
        "documento": "Livro de receitas com pratos típicos da culinária italiana, focado em massas e risotos.",
        "categoria": "livros",
        "preco": 54.90,
    },
    {
        "id": "p009",
        "documento": "Colchonete para yoga e exercícios de alongamento, material antiderrapante.",
        "categoria": "esporte",
        "preco": 89.90,
    },
    {
        "id": "p010",
        "documento": "Smartwatch com monitor de frequência cardíaca, GPS integrado e resistência à água.",
        "categoria": "eletronicos",
        "preco": 899.00,
    },
]
 
 
def popular_banco():
    client = chromadb.PersistentClient(path=DB_PATH)
 
    # CREATE TABLE IF NOT EXISTS produtos (...)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    if collection.count() > 0:
      print(f"O banco já contém {collection.count()} documentos. Nada foi alterado.")
      return
 
    # INSERT INTO produtos (id, descricao, categoria, preco) VALUES (...)
    collection.add(
        ids=[p["id"] for p in PRODUTOS],
        documents=[p["documento"] for p in PRODUTOS],
        metadatas=[{"categoria": p["categoria"], "preco": p["preco"]} for p in PRODUTOS],
    )
 
    print(f"Banco populado com sucesso em '{DB_PATH}'.")
    print(f"Coleção '{COLLECTION_NAME}' agora possui {collection.count()} produtos.")
 
 
if __name__ == "__main__":
    popular_banco()