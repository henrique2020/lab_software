<?php

include_once "./../env.php";
include_once ROOT_DB . "Database.php";
include_once ROOT_MODEL . "Laboratorio.php";

class LaboratorioDAO {

    public function __construct(private ?Database $db = null) {
        $this->db = $db ?? new Database();
    }

    // Inserir novo laboratório
    public function inserir(Laboratorio $laboratorio) : int {
        $sql = "INSERT INTO laboratorio (nome, sigla, bloco, sala) VALUES (:nome, :sigla, :bloco, :sala)";

        return $this->db->insert($sql, [
            ':nome' => $laboratorio->nome,
            ':sigla' => $laboratorio->sigla,
            ':bloco' => $laboratorio->bloco,
            ':sala' => $laboratorio->sala,
        ]);
    }

    // Atualizar laboratório
    public function atualizar(Laboratorio $laboratorio) : int {
        $sql = "UPDATE laboratorio SET nome = :nome, sigla = :sigla, bloco = :bloco, sala = :sala WHERE id = :id";

        return $this->db->update($sql, [
            ':id' => $laboratorio->id,
            ':nome' => $laboratorio->nome,
            ':sigla' => $laboratorio->sigla,
            ':bloco' => $laboratorio->bloco,
            ':sala' => $laboratorio->sala,
        ]);
    }

    // Deletar laboratório
    public function deletar(int $id) : int {
        $sql = "DELETE FROM laboratorio WHERE id = :id";
        return $this->db->delete($sql, [':id' => $id]);
    }

    // Listar todos os laboratórios
    public function listarTodos() : array {
        $sql = "SELECT * FROM laboratorio ORDER BY nome";
        $resultados = $this->db->select($sql);

        $laboratorios = [];
        foreach ($resultados as $linha) {
            $laboratorios[] = new Laboratorio(...$linha);
        }
        return $laboratorios;
    }

    // Buscar por ID
    public function buscarPorId(int $id) : ?Laboratorio {
        $sql = "SELECT * FROM laboratorio WHERE id = :id";
        $resultados = $this->db->select($sql, [':id' => $id]);

        return !empty($resultados) ? new Laboratorio(...$resultados[0]) : null;
    }
}
