<?php

class Usuario {
    
    public function __construct(
        public ?int $id = null,
        public string $nome,
        public string $email,
        public ?string $tipo = null,
        public ?int $id_laboratorio = null,
    ) {
        $this->id             = $id;
        $this->nome           = $nome;
        $this->email          = $email;
        $this->tipo           = $tipo ?? 'Responsavel';
        $this->id_laboratorio = $id_laboratorio;
    }

    public function isAdministrador(): bool {
        return $this->tipo === 'Administrador';
    }
}
