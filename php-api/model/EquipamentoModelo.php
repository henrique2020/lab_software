<?php

/**
 * Representa um modelo de equipamento no sistema.
 */
class EquipamentoModelo {

    public function __construct(
        public ?int $id = null,
        public int $numero_patrimonio,
        public string $identificacao,
        public string $equipamento,
        public string $marca,
        public string $criterio_aceitacao_calibracao,
        public int $periodicidade_calibracao,
        public int $periodicidade_manutencao,
        public string $tipo, // 'Analógico' ou 'Digital'
        public ?int $id_categoria = null,
    ) {
        $this->id                             = $id;
        $this->numero_patrimonio              = $numero_patrimonio;
        $this->identificacao                  = $identificacao;
        $this->equipamento                    = $equipamento;
        $this->marca                          = $marca;
        $this->criterio_aceitacao_calibracao = $criterio_aceitacao_calibracao;
        $this->periodicidade_calibracao       = $periodicidade_calibracao;
        $this->periodicidade_manutencao       = $periodicidade_manutencao;
        $this->tipo                           = $tipo;
        $this->id_categoria                   = $id_categoria;
    }

    public function toArray(): array {
        return [
            'id'                             => $this->id,
            'numero_patrimonio'              => $this->numero_patrimonio,
            'identificacao'                  => $this->identificacao,
            'equipamento'                    => $this->equipamento,
            'marca'                          => $this->marca,
            'criterio_aceitacao_calibracao' => $this->criterio_aceitacao_calibracao,
            'periodicidade_calibracao'       => $this->periodicidade_calibracao,
            'periodicidade_manutencao'       => $this->periodicidade_manutencao,
            'tipo'                           => $this->tipo,
            'id_categoria'                   => $this->id_categoria,
        ];
    }
}
