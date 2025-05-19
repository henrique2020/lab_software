<?php
include_once "./../env.php";
include_once ROOT_DB . "Conf.inc.php";

/**
 * Classe Database
 * Encapsula operações com banco de dados utilizando PDO.
 * Fornece métodos para SELECT, INSERT, UPDATE, DELETE, além de suporte a chamadas dinâmicas ao PDO.
 */
class Database {
    /** @var PDO Conexão PDO com o banco de dados */
    private $connection;

    /** @var PDOStatement Armazena a query preparada */
    private $query;

    /**
     * Construtor da classe.
     * Inicializa a conexão com o banco de dados usando os dados definidos em env.php
     * Define o modo de erro do PDO para exceções.
     */
    public function __construct(){
        $this->connection = new PDO(
            "mysql:host=" . DB_HOST . ";dbname=" . DB_BANCO . ";charset=utf8mb4",
            DB_USUARIO,
            DB_SENHA
        );
        $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }

    /**
     * Permite chamadas diretas para métodos nativos da instância PDO.
     * Ex: $db->beginTransaction(), $db->commit(), etc.
     */
    public function __call(string $name, $trash = null) : mixed {
        if (method_exists($this->connection, $name)) {
            return $this->connection->$name();
        }
        throw new Exception("O método {$name} não existe.");
    }

    /**
     * Prepara uma query SQL (Prevenção de SQL Injection).
     *
     * @param string $sql Instrução SQL a ser preparada.
     */
    public function prepare($sql){
        $this->query = $this->connection->prepare($sql);
    }

    /**
     * Executa a query preparada.
     *
     * @param array $param Parâmetros para a execução (opcional).
     * @return bool Sucesso ou falha da execução.
     */
    public function execute($param = []){
        if (empty($param)) {
            return $this->query->execute();
        } else {
            return $this->query->execute($param);
        }
    }

    /**
     * Executa uma operação INSERT.
     *
     * @param string $sql Instrução INSERT.
     * @param array $params Parâmetros da query.
     * @return string ID do último registro inserido.
     */
    public function insert($sql, $params = []) {
        $this->prepare($sql);
        $this->execute($params);
        return $this->connection->lastInsertId();
    }

    /**
     * Executa uma operação UPDATE.
     *
     * @param string $sql Instrução UPDATE.
     * @param array $params Parâmetros da query.
     * @return int Número de linhas afetadas.
     */
    public function update($sql, $params = []) {
        $this->prepare($sql);
        $this->execute($params);
        return $this->query->rowCount();
    }

    /**
     * Executa uma operação DELETE.
     *
     * @param string $sql Instrução DELETE.
     * @param array $params Parâmetros da query.
     * @return int Número de linhas excluídas.
     */
    public function delete($sql, $params = []) {
        $this->prepare($sql);
        $this->execute($params);
        return $this->query->rowCount();
    }

    /**
     * Executa uma operação SELECT.
     *
     * @param string $sql Instrução SELECT.
     * @param array $params Parâmetros da query.
     * @param int $fetchMode Modo de retorno (default: PDO::FETCH_ASSOC).
     * @return array Conjunto de resultados da consulta.
     */
    public function select($sql, $params = [], $fetchMode = PDO::FETCH_ASSOC) {
        $this->prepare($sql);
        $this->execute($params);
        return $this->query->fetchAll($fetchMode);
    }
}
?>
