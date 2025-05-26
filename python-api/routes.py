from fastapi import APIRouter, Request, HTTPException
import middleware
from dao import EquipamentoModeloDAO, LaboratorioDAO, UsuarioDAO
from model import EquipamentoModelo, Laboratorio, Usuario


router = APIRouter()

udao = UsuarioDAO()
ldao = LaboratorioDAO()
emdao = EquipamentoModeloDAO()

@router.post("/login")
async def login(request: Request):
    dados = await request.json()
    dados = {k: v.strip() if isinstance(v, str) else v for k, v in dados.items()}
    usuario = udao.buscar_por_email(dados['email'])
    if usuario and usuario.validate_pass(dados['senha']):
        usuario.token, usuario.data_acesso, usuario.data_expiracao, a = middleware.criar_token({
            "nome": usuario.nome, 
            "admin": usuario.admin, 
            "laboratorio": usuario.id_laboratorio
        })
        
        if udao.atualizar_token(usuario):
            return {"API": {"URI": "/api/login", "METHOD": "POST"}, "success": True, "token": usuario.token}
    
    return {"API": {"URI": "/api/login", "METHOD": "POST"}, "success": False, "message": "Usuário e/ou senha incorreto"}

@router.get("/equipamentos")
def listar_equipamentos(request: Request):
    if request.state.token['admin']: 
        dados = emdao.listar_todos()
    else:
        dados = emdao.listar_por_laboratorio(request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/equipamentos", "METHOD": "GET"}, "DATA": dados}

@router.get("/laboratorios")
def listar_laboratorios(request: Request):
    if request.state.token['admin']: 
        dados = ldao.listar_todos()
    else:
        dados = ldao.buscar_por_id(request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/laboratorios", "METHOD": "GET"}, "DATA": dados}

@router.get("/usuarios")
def listar_usuarios(request: Request):
    if request.state.token['admin']: 
        dados = udao.listar_todos()
    else:
        dados = udao.listar_por_laboratorio(request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/usuarios", "METHOD": "GET"}, "DATA": dados}

@router.post("/equipamento")
async def inserir_equipamento(request: Request):
    dados = await request.json()
    equipamento = EquipamentoModelo(**dados)
    sucesso = emdao.inserir(equipamento)
    return {"success": bool(sucesso)}

@router.post("/laboratorio")
async def inserir_laboratorio(request: Request):
    dados = await request.json()
    laboratorio = Laboratorio(**dados)
    sucesso = ldao.inserir(laboratorio)
    return {"success": bool(sucesso)}

@router.post("/usuario")
async def inserir_usuario(request: Request):
    dados = await request.json()
    usuario = Usuario(**dados)
    usuario.criptografa()
    sucesso = udao.inserir(usuario)
    return {"success": bool(sucesso)}
