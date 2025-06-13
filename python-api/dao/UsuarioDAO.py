from dao.Database import Database
from model.Usuario import Usuario

from dao.LaboratorioDAO import LaboratorioDAO

class UsuarioDAO:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()
        
    def _buscar_objetos(self, linha: dict) -> Usuario:
        u = Usuario(**linha)
        u.id_laboratorio = LaboratorioDAO(self.db).buscar_por_id(u.id_laboratorio)
        
        return u

    def inserir(self, usuario: Usuario) -> int:
        sql = "INSERT INTO usuario (nome, email, senha, admin, id_laboratorio) VALUES (%(nome)s, %(email)s, %(senha)s, %(admin)s, %(id_laboratorio)s)"
        return self.db.insert(sql, {
            'nome': usuario.nome,
            'email': usuario.email,
            'senha': usuario.senha,
            'admin': usuario.admin,
            'id_laboratorio': usuario.id_laboratorio
        })

    def atualizar(self, usuario: Usuario) -> int:
        sql = "UPDATE usuario SET nome = %(nome)s, email = %(email)s, senha = %(senha)s, admin = %(admin)s, id_laboratorio = %(id_laboratorio)s WHERE id = %(id)s"
        return self.db.update(sql, {
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'senha': usuario.senha,
            'admin': usuario.admin,
            'id_laboratorio': usuario.id_laboratorio
        })
    
    def atualizar_token(self, usuario: Usuario) -> int:
        sql = "UPDATE usuario SET data_acesso = %(data_acesso)s, token = %(token)s, data_expiracao = %(data_expiracao)s WHERE id = %(id)s"
        return self.db.update(sql, {
            'id': usuario.id,
            'data_acesso': usuario.data_acesso,
            'token': usuario.token,
            'data_expiracao': usuario.data_expiracao
        })

    def deletar(self, id: int) -> int:
        return self.db.delete("DELETE FROM usuario WHERE id = %(id)s", {'id': id})
    
    def buscar_por_id(self, id: int) -> Usuario | None:
        resultado = self.db.select("SELECT * FROM usuario WHERE id = %(id)s", {'id': id})
        return Usuario(**resultado[0]) if resultado else None

    def buscar_por_email(self, email: str) -> Usuario | None:
        resultado = self.db.select("SELECT * FROM usuario WHERE email = %(email)s", {'email': email})
        return Usuario(**resultado[0]) if resultado else None

    def listar_todos(self) -> list[Usuario]:
        resultados = self.db.select("SELECT * FROM usuario ORDER BY nome")
        return [self._buscar_objetos(linha) for linha in resultados]
    
    def listar_por_laboratorio(self, id_laboratorio: int) -> list[Usuario]:
        resultados = self.db.select("SELECT * FROM usuario WHERE id_laboratorio = %(id)s", {'id': id_laboratorio})
        return [self._buscar_objetos(linha) for linha in resultados]

    def atualizar_status(self, id: int) -> bool:
        sql = "UPDATE usuario SET ativo = CASE WHEN ativo = 1 THEN 0 ELSE 1 END WHERE id = %(id)s"
        return self.db.update(sql, {'id': id})