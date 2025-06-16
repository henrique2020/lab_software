from dataclasses import dataclass
from typing import Optional
from datetime import datetime
import bcrypt

from model.Laboratorio import Laboratorio

@dataclass
class Usuario:
    id: Optional[int]
    nome: str
    email: str
    senha: Optional[str] = None
    admin: bool = False
    id_laboratorio: Optional[int]|Optional[Laboratorio] = None
    data_acesso: Optional[datetime] = None
    token: Optional[str] = None
    data_expiracao: Optional[datetime] = None
    ativo: Optional[bool] = True

    def criptografa(self):
        self.senha = bcrypt.hashpw(self.senha.encode(), bcrypt.gensalt()).decode()

    def valida_senha(self, senha: str) -> bool:
        return bcrypt.checkpw(senha.encode(), self.senha.encode())
