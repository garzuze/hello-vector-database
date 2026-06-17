import sys
import chromadb
from config import DB_PATH, COLLECTION_NAME
from chromadb.utils import embedding_functions

 
def buscar(query_texto: str, n_resultados: int = 3, categoria: str | None = None):
    client = chromadb.PersistentClient(path=DB_PATH)
    embedding_fn = embedding_functions.DefaultEmbeddingFunction()
 
    try:
        collection = client.get_collection(name=COLLECTION_NAME,embedding_function=embedding_fn)
    except Exception:
        print("Coleção não encontrada. Execute 'python populate_db.py' primeiro.")
        sys.exit(1)
 
    # monta o filtro de metadados, seria equivalente a um WHERE categoria = ?
    filtro = {"categoria": categoria} if categoria else None
 
    resultado = collection.query(
        query_texts=[query_texto],
        n_results=n_resultados,
        where=filtro,
    )
 
    documentos = resultado["documents"][0]
    metadados = resultado["metadatas"][0]
    distancias = resultado["distances"][0]
 
    print(f"\nBusca: '{query_texto}'" + (f"  |  filtro categoria='{categoria}'" if categoria else ""))
    print("-" * 70)
    if not documentos:
        print("Nenhum resultado encontrado.")
        return
 
    for i, (doc, meta, dist) in enumerate(zip(documentos, metadados, distancias), start=1):
        # 'dist' é a distância vetorial, quanto menor, mais parecido em significado
        print(f"{i}. {doc}")
        print(f"   categoria: {meta['categoria']} | preço: R$ {meta['preco']:.2f} | distância: {dist:.4f}")
    print()
 
 
if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = sys.argv[1]
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        buscar(query, n_resultados=n)
    else:
        # demonstração com algumas consultas prontas
        buscar("presente para quem gosta de cozinhar", n_resultados=2)
        buscar("quero algo para fazer exercício em casa", n_resultados=2)
        buscar("preciso de um aparelho para trabalhar e estudar", n_resultados=2)
        buscar("livro para ler na praia", n_resultados=2, categoria="livros")
