from dao.Database import Database
from model.Usuario import Usuario

class UsuarioDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()

    def inserir(self, usuario: Usuario) -> int:
        sql = """
        INSERT INTO usuario (nome, email, senha, admin, id_laboratorio)
        VALUES (%(nome)s, %(email)s, %(senha)s, %(admin)s, %(id_laboratorio)s)
        """
        return self.db.insert(sql, {
            'nome': usuario.nome,
            'email': usuario.email,
            'senha': usuario.senha,
            'admin': usuario.admin,
            'id_laboratorio': usuario.id_laboratorio
        })

    def atualizar(self, usuario: Usuario) -> int:
        sql = """
        UPDATE usuario SET nome = %(nome)s, email = %(email)s, senha = %(senha)s,
        admin = %(admin)s, id_laboratorio = %(id_laboratorio)s WHERE id = %(id)s
        """
        return self.db.update(sql, {
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'senha': usuario.senha,
            'admin': usuario.admin,
            'id_laboratorio': usuario.id_laboratorio
        })

    def deletar(self, id_: int) -> int:
        return self.db.delete("DELETE FROM usuario WHERE id = %(id)s", {'id': id_})

    def listar_todos(self) -> list[Usuario]:
        resultados = self.db.select("SELECT * FROM usuario ORDER BY nome")
        return [Usuario(**linha) for linha in resultados]

    def buscar_por_id(self, id_: int) -> Usuario | None:
        resultado = self.db.select("SELECT * FROM usuario WHERE id = %(id)s", {'id': id_})
        return Usuario(**resultado[0]) if resultado else None

    def buscar_por_email(self, email: str) -> Usuario | None:
        resultado = self.db.select("SELECT * FROM usuario WHERE email = %(email)s", {'email': email})
        return Usuario(**resultado[0]) if resultado else None
