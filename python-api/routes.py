from fastapi import APIRouter, Request, HTTPException
from dao.UsuarioDAO import UsuarioDAO
from dao.LaboratorioDAO import LaboratorioDAO
from dao.EquipamentoModeloDAO import EquipamentoModeloDAO
from model.Usuario import Usuario
from model.Laboratorio import Laboratorio
from model.EquipamentoModelo import EquipamentoModelo

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
        usuario.generate_token()
        return {"API": {"URI": "/api/login", "METHOD": "POST"}, "success": True, "token": usuario.token}
    return {"API": {"URI": "/api/login", "METHOD": "POST"}, "success": False, "message": "Usuário e/ou senha incorreto"}

@router.get("/equipamentos")
def listar_equipamentos():
    return {"API": {"URI": "/api/equipamentos", "METHOD": "GET"}, "DATA": emdao.listar_todos()}

@router.get("/laboratorios")
def listar_laboratorios():
    return {"API": {"URI": "/api/laboratorios", "METHOD": "GET"}, "DATA": ldao.listar_todos()}

@router.get("/usuarios")
def listar_usuarios():
    return {"API": {"URI": "/api/usuarios", "METHOD": "GET"}, "DATA": udao.listar_todos()}

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
