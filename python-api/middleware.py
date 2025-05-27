import os
from fastapi import HTTPException
from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
import re

load_dotenv()

# Configurações
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
EXPIRE_HOURS = int(os.getenv("TOKEN_EXPIRATION_HOURS", 1))

def criar_token(dados: dict) -> str:
    agora = datetime.now()
    expiracao = agora + timedelta(hours=EXPIRE_HOURS)
    dados.update({"exp": expiracao})
    token = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token, agora, expiracao

def verificar_token(token: str) -> dict:
    match = re.match(r"^Bearer\s+(.+)$", str(token))
    if match:
        token = match.group(1)
        
    try:
        dados = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return dados
    except JWTError:
        raise HTTPException(status_code=403, detail="Token inválido ou expirado")
    except:
        raise HTTPException(status_code=403, detail="Houve um erro interno, tente novamente mais tarde")