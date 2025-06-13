from dao.Database import Database
from model.Bloco import Bloco

class BlocoDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()

    def inserir(self, bloco: Bloco) -> int:
        sql = "INSERT INTO bloco (nome) VALUES (%(nome)s)"
        params = {
            'nome': bloco.nome,
        }
        return self.db.insert(sql, params)

    def atualizar(self, bloco: Bloco) -> int:
        sql = "UPDATE bloco SET nome = %(nome)s WHERE id = %(id)s"
        params = {
            'id': bloco.id,
            'nome': bloco.nome,
        }
        return self.db.update(sql, params)

    def deletar(self, id_: int) -> int:
        sql = "DELETE FROM bloco WHERE id = %(id)s"
        return self.db.delete(sql, {'id': id_})

    def buscar_por_id(self, id_: int) -> Bloco | None:
        sql = "SELECT * FROM bloco WHERE id = %(id)s"
        resultado = self.db.select(sql, {'id': id_})
        return Bloco(**resultado[0]) if resultado else None
    
    def listar_todos(self) -> list[Bloco]:
        sql = "SELECT * FROM bloco ORDER BY nome"
        resultados = self.db.select(sql)
        return [Bloco(**linha) for linha in resultados]

    def atualizar_status(self, id: int) -> bool:
        sql = "UPDATE bloco SET ativo = CASE WHEN ativo = 1 THEN 0 ELSE 1 END WHERE id = %(id)s"
        return self.db.update(sql, {'id': id})