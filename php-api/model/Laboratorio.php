<?php

class Laboratorio {

    public function __construct(
        public ?int $id = null,
        public string $nome,
        public string $sigla,
        public string $bloco,
        public int $sala,
    ) {
        $this->id       = $id;
        $this->nome     = $nome;
        $this->sigla    = $sigla;
        $this->bloco     = $bloco;
        $this->sala     = $sala;
    }
}
