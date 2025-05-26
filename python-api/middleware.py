from fastapi import Request, HTTPException

def verificar_token_bearer(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Token não informado")
    
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Formato de token inválido")
    
    token = auth_header.split(" ")[1]
    if token != "chave-super-secreta":
        raise HTTPException(status_code=403, detail="Token inválido")
