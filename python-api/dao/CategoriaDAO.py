from dao.Database import Database
from model.Categoria import Categoria

class CategoriaDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()

    def inserir(self, categoria: Categoria) -> int:
        sql = "INSERT INTO categoria (nome) VALUES (%(nome)s)"
        params = {
            'nome': categoria.nome,
        }
        return self.db.insert(sql, params)

    def atualizar(self, categoria: Categoria) -> int:
        sql = "UPDATE categoria SET nome = %(nome)s WHERE id = %(id)s"
        params = {
            'id': categoria.id,
            'nome': categoria.nome,
        }
        return self.db.update(sql, params)

    def deletar(self, id_: int) -> int:
        sql = "DELETE FROM categoria WHERE id = %(id)s"
        return self.db.delete(sql, {'id': id_})

    def buscar_por_id(self, id_: int) -> Categoria | None:
        sql = "SELECT * FROM categoria WHERE id = %(id)s"
        resultado = self.db.select(sql, {'id': id_})
        return Categoria(**resultado[0]) if resultado else None
    
    def listar_todos(self) -> list[Categoria]:
        sql = "SELECT * FROM categoria ORDER BY nome"
        resultados = self.db.select(sql)
        return [Categoria(**linha) for linha in resultados]
