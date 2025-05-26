from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timedelta
import bcrypt

@dataclass
class Usuario:
    id: Optional[int]
    nome: str
    email: str
    senha: str
    admin: bool = False
    id_laboratorio: Optional[int] = None
    data_acesso: Optional[datetime] = None
    token: Optional[str] = None
    data_expiracao: Optional[datetime] = None

    def criptografa(self):
        self.senha = bcrypt.hashpw(self.senha.encode(), bcrypt.gensalt()).decode()

    def validate_pass(self, senha: str) -> bool:
        return bcrypt.checkpw(senha.encode(), self.senha.encode())

    def generate_token(self):
        self.data_acesso = datetime.now()
        self.data_expiracao = self.data_acesso + timedelta(hours=6)
        self.token = f"Bearer {self.nome}-{self.id}-{self.data_expiracao.strftime('%Y%m%d%H%M%S')}"
