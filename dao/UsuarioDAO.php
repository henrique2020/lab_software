<?php

include_once "./../env.php";
include_once ROOT_DB . "Database.php";
include_once ROOT_MODEL . "Usuario.php";

class UsuarioDAO {
    
    public function __construct(private ?Database $db = null) {
        $this->db = $db ?? new Database();
    }

    // Inserir novo usuário
    public function inserir(Usuario $usuario) : int {
        $sql = "INSERT INTO usuario (nome, email, tipo, id_laboratorio)
                VALUES (:nome, :email, :tipo, :id_laboratorio)";

        return $this->db->insert($sql, [
            ':nome' => $usuario->nome,
            ':email' => $usuario->email,
            ':tipo' => $usuario->tipo,
            ':id_laboratorio' => $usuario->id_laboratorio,
        ]);
    }

    // Atualizar usuário
    public function atualizar(Usuario $usuario) : int {
        $sql = "UPDATE usuario SET nome = :nome, email = :email, tipo = :tipo,
                id_laboratorio = :id_laboratorio WHERE id = :id";

        return $this->db->update($sql, [
            ':id' => $usuario->id,
            ':nome' => $usuario->nome,
            ':email' => $usuario->email,
            ':tipo' => $usuario->tipo,
            ':id_laboratorio' => $usuario->id_laboratorio,
        ]);
    }

    // Deletar usuário por ID
    public function deletar(int $id) : int {
        $sql = "DELETE FROM usuario WHERE id = :id";
        return $this->db->delete($sql, [':id' => $id]);
    }

    // Listar todos os usuários
    public function listarTodos() : array {
        $sql = "SELECT * FROM usuario ORDER BY nome";
        $resultados = $this->db->select($sql);

        $usuarios = [];
        foreach ($resultados as $linha) {
            $usuarios[] = new Usuario(...$linha);
        }
        return $usuarios;
    }

    // Buscar por ID
    public function buscarPorId(int $id) : ?Usuario {
        $sql = "SELECT * FROM usuario WHERE id = :id";
        $resultados = $this->db->select($sql, [':id' => $id]);

        return !empty($resultados) ? new Usuario(...$resultados[0]) : null;
    }
}
