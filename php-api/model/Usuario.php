<?php

class Usuario {
    
    public function __construct(
        public ?int $id = null,
        public string $nome,
        public string $email,
        public string $senha,
        public bool $admin = false,
        public ?int $id_laboratorio = null,
        public ?DateTime $data_acesso = null,
        public ?string $token = null,
        public ?DateTime $data_expiracao = null,
    ) {
        $this->id             = $id;
        $this->nome           = $nome;
        $this->email          = $email;
        $this->admin          = $admin;
        $this->id_laboratorio = $id_laboratorio;
        $this->data_acesso    = $data_acesso;
        $this->token          = $token;
        $this->data_expiracao = $data_expiracao;
    }

    public function criptografa(){
        $this->senha = password_hash($this->senha, PASSWORD_BCRYPT);
    }

    public function validatePass($senha){
        return password_verify($senha, $this->senha);
    }

    public function generateToken(){
        $this->data_acesso = new DateTime();

        $this->data_expiracao = new DateTime();
        $this->data_expiracao->modify('+6 hours');
        $this->token = "Bearer {$this->nome}-{$this->id}-{$this->data_expiracao->format('YmdHis')}";
    }
}
