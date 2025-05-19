<?php

include_once "./../env.php";
include_once ROOT_DB . "Database.php";
include_once ROOT_MODEL . "EquipamentoModelo.php";

/**
 * DAO para operações com a tabela equipamento_modelo.
 */
class EquipamentoModeloDAO {

    public function __construct(private ?Database $db = null) {
        $this->db = $db ?? new Database();
    }

    public function inserir(EquipamentoModelo $modelo): int {
        $sql = "INSERT INTO equipamento_modelo 
            (numero_patrimonio, identificacao, equipamento, marca, critterio_aceitacao_calibracao, 
             periodicidade_calibracao, periodicidade_manutencao, tipo, id_categoria)
            VALUES 
            (:numero_patrimonio, :identificacao, :equipamento, :marca, :critterio, 
             :periodicidade_calibracao, :periodicidade_manutencao, :tipo, :id_categoria)";

        return $this->db->insert($sql, [
            ':numero_patrimonio'         => $modelo->numero_patrimonio,
            ':identificacao'             => $modelo->identificacao,
            ':equipamento'               => $modelo->equipamento,
            ':marca'                     => $modelo->marca,
            ':critterio'                 => $modelo->critterio_aceitacao_calibracao,
            ':periodicidade_calibracao'  => $modelo->periodicidade_calibracao,
            ':periodicidade_manutencao'  => $modelo->periodicidade_manutencao,
            ':tipo'                      => $modelo->tipo,
            ':id_categoria'              => $modelo->id_categoria,
        ]);
    }

    public function atualizar(EquipamentoModelo $modelo): int {
        $sql = "UPDATE equipamento_modelo SET
            numero_patrimonio = :numero_patrimonio,
            identificacao = :identificacao,
            equipamento = :equipamento,
            marca = :marca,
            critterio_aceitacao_calibracao = :critterio,
            periodicidade_calibracao = :periodicidade_calibracao,
            periodicidade_manutencao = :periodicidade_manutencao,
            tipo = :tipo,
            id_categoria = :id_categoria
            WHERE id = :id";

        return $this->db->update($sql, [
            ':id'                        => $modelo->id,
            ':numero_patrimonio'         => $modelo->numero_patrimonio,
            ':identificacao'             => $modelo->identificacao,
            ':equipamento'               => $modelo->equipamento,
            ':marca'                     => $modelo->marca,
            ':critterio'                 => $modelo->critterio_aceitacao_calibracao,
            ':periodicidade_calibracao'  => $modelo->periodicidade_calibracao,
            ':periodicidade_manutencao'  => $modelo->periodicidade_manutencao,
            ':tipo'                      => $modelo->tipo,
            ':id_categoria'              => $modelo->id_categoria,
        ]);
    }

    public function deletar(int $id): int {
        $sql = "DELETE FROM equipamento_modelo WHERE id = :id";
        return $this->db->delete($sql, [':id' => $id]);
    }

    public function buscarPorId(int $id): ?EquipamentoModelo {
        $sql = "SELECT * FROM equipamento_modelo WHERE id = :id";
        $res = $this->db->select($sql, [':id' => $id]);
        return !empty($res) ? new EquipamentoModelo(...$res[0]) : null;
    }

    public function listarTodos(): array {
        $sql = "SELECT * FROM equipamento_modelo ORDER BY numero_patrimonio";
        $res = $this->db->select($sql);

        $modelos = [];
        foreach ($res as $linha) {
            $modelos[] = new EquipamentoModelo(...$linha);
        }
        return $modelos;
    }
}
