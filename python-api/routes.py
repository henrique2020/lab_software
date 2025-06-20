from fastapi import APIRouter, Request, HTTPException
import middleware
from dao import *
from model import *

router = APIRouter()

bdao = BlocoDAO()
cadao = CategoriaDAO()
cedao = CertificadoDAO()
eqdao = EquipamentoDAO()
emdao = EquipamentoModeloDAO()
evdao = EventoDAO()
ldao = LaboratorioDAO()
udao = UsuarioDAO()
vdao = ViewDAO()

@router.post("/login")
async def login(request: Request):
    dados = await request.json()
    dados = {k: v.strip() if isinstance(v, str) else v for k, v in dados.items()}
    usuario = udao.buscar_por_email(dados['email'])
    if not usuario or not usuario.ativo:
        return {"API": {"URI": "/api/login", "METHOD": "POST"}, "success": False, "message": "Usuário não encontrado, entre em contato com o administrador"}
    elif usuario.valida_senha(dados['senha']):
        usuario.token, usuario.data_acesso, usuario.data_expiracao = middleware.criar_token({
            "id": usuario.id,
            "nome": usuario.nome, 
            "admin": usuario.admin, 
            "laboratorio": usuario.id_laboratorio
        })
        
        if udao.atualizar_token(usuario):
            return {"API": {"URI": "/api/login", "METHOD": "POST"}, "success": True, "token": usuario.token, 'payload': middleware.verificar_token(usuario.token)}
    
    return {"API": {"URI": "/api/login", "METHOD": "POST"}, "success": False, "message": "Usuário e/ou senha incorreto"}


# Bloco
@router.get("/bloco/{id}")
def buscar_bloco(id: int):
    return {"API": {"URI": f"/api/bloco/{id}", "METHOD": "GET"}, "DATA": bdao.buscar_por_id(id)}

@router.get("/blocos")
def listar_blocos():
    return {"API": {"URI": "/api/blocos", "METHOD": "GET"}, "DATA": bdao.listar_todos()}

@router.post("/bloco")
async def inserir_bloco(request: Request):
    dados = await request.json()
    bloco = Bloco(None, **dados)
    
    return {"success": bool(bdao.inserir(bloco))}

@router.post("/bloco/atualizar")
async def atualizar_bloco(request: Request):
    dados = await request.json()
    bloco = Bloco(**dados)
    
    return {"success": bool(bdao.atualizar(bloco))}

@router.post("/bloco/atualizar/status")
async def atualizar_status_bloco(request: Request):
    dados = await request.json()
    return {"success": bool(bdao.atualizar_status(dados['id']))}


# Categoria
@router.get("/categoria/{id}")
def buscar_categoria(id: int):
    return {"API": {"URI": f"/api/categoria/{id}", "METHOD": "GET"}, "DATA": cadao.buscar_por_id(id)}

@router.get("/categorias")
def listar_categorias():
    return {"API": {"URI": "/api/categorias", "METHOD": "GET"}, "DATA": cadao.listar_todos()}

@router.post("/categoria")
async def inserir_categoria(request: Request):
    dados = await request.json()
    categoria = Categoria(None, **dados)
    
    return {"success": bool(cadao.inserir(categoria))}

@router.post("/categoria/atualizar")
async def atualizar_categoria(request: Request):
    dados = await request.json()
    categoria = Categoria(**dados)
    
    return {"success": bool(cadao.atualizar(categoria))}

@router.post("/categoria/atualizar/status")
async def atualizar_status_categoria(request: Request):
    dados = await request.json()
    return {"success": bool(cadao.atualizar_status(dados['id']))}


# Certificado
@router.get("/certificado/{id}")
def buscar_certificado(id: int):
    return {"API": {"URI": f"/api/certificado/{id}", "METHOD": "GET"}, "DATA": cedao.buscar_por_id(id)}

@router.get("/certificados")
def listar_certificado():
    return {"API": {"URI": "/api/certificados", "METHOD": "GET"}, "DATA": cedao.listar_todos()}

@router.post("/certificado")
async def inserir_certificado(request: Request):
    dados = await request.json()
    certificado = Certificado(None, **dados)
    
    return {"success": bool(cedao.inserir(certificado))}

@router.post("/certificado/atualizar")
async def atualizar_certificado(request: Request):
    dados = await request.json()
    certificado = Certificado(None, **dados)
    
    return {"success": bool(cedao.atualizar(certificado))}


# Equipamento
@router.get("/equipamento/{id}")
def buscar_equipamento(request: Request, id: int):
    if request.state.token['admin']:
        dados = eqdao.buscar_por_id(id)
    else:
        dados = eqdao.buscar_por_id_laboratorio(id, request.state.token['laboratorio'])
        if not dados:
            return HTTPException(404, "Permissões insuficiente")

    return {"API": {"URI": f"/api/equipamento/{id}", "METHOD": "GET"}, "DATA": dados}

@router.get("/equipamentos")
def listar_equipamentos(request: Request):
    if request.state.token['admin']: 
        dados = eqdao.listar_todos()
    else:
        dados = eqdao.listar_por_laboratorio(request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/equipamentos", "METHOD": "GET"}, "DATA": dados}

@router.post("/equipamento")
async def inserir_equipamento(request: Request):
    dados = await request.json()
    equipamento = Equipamento(None, **dados)
    return {"success": bool(eqdao.inserir(equipamento))}

@router.post("/equipamento/atualizar")
async def atualizar_equipamento(request: Request):
    dados = await request.json()
    equipamento = Equipamento(**dados)
    return {"success": bool(eqdao.atualizar(equipamento))}

@router.post("/equipamento/atualizar/status")
async def atualizar_status_equipamento(request: Request):
    dados = await request.json()
    return {"success": bool(eqdao.atualizar_status(dados['id']))}


# Evento
@router.get("/evento/{id}")
def buscar_evento(request: Request, id: int):
    if request.state.token['admin']:
        dados = evdao.buscar_por_id(id)
    else:
        dados = evdao.buscar_por_id_laboratorio(id, request.state.token['laboratorio'])

    return {"API": {"URI": f"/api/evento/{id}", "METHOD": "GET"}, "DATA": dados}

@router.get("/eventos")
def listar_eventos(request: Request):
    if request.state.token['admin']: 
        dados = evdao.listar_todos()
    else:
        dados = evdao.listar_por_laboratorio(request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/eventos", "METHOD": "GET"}, "DATA": dados}

@router.get("/eventos/equipamento/{id}")
def listar_eventos_equipamento(request: Request, id: int):
    if request.state.token['admin']: 
        dados = evdao.listar_por_equipamento(id)
    else:
        dados = evdao.listar_por_equipamento_laboratorio(id, request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/eventos", "METHOD": "GET"}, "DATA": dados}

@router.post("/evento")
async def inserir_evento(request: Request):
    dados = await request.json()
    evento = Evento(None, **dados)
    return {"success": bool(evdao.inserir(evento))}

@router.post("/evento/atualizar")
async def atualizar_evento(request: Request):
    dados = await request.json()
    evento = Evento(**dados)
    return {"success": bool(evdao.atualizar(evento))}


# Equipamento Modelo
@router.get("/modelo/{id}")
def buscar_equipamento_modelo(id: int):
    return {"API": {"URI": f"/api/equipamento/{id}", "METHOD": "GET"}, "DATA": emdao.buscar_por_id(id)}

@router.get("/modelos")
def listar_equipamentos_modelo():
    return {"API": {"URI": "/api/equipamentos", "METHOD": "GET"}, "DATA": emdao.listar_todos()}

@router.post("/modelo/")
async def inserir_equipamento_modelo(request: Request):
    dados = await request.json()
    equipamento = EquipamentoModelo(None, **dados)
    return {"success": bool(emdao.inserir(equipamento))}

@router.post("/modelo/atualizar")
async def atualizar_equipamento_modelo(request: Request):
    dados = await request.json()
    equipamento = EquipamentoModelo(**dados)
    return {"success": bool(emdao.atualizar(equipamento))}

@router.post("/modelo/atualizar/status")
async def atualizar_status_modelo(request: Request):
    dados = await request.json()
    return {"success": bool(emdao.atualizar_status(dados['id']))}


# Laboratório
@router.get("/laboratorio/{id}")
def buscar_laboratorio(request: Request, id: int):
    dados = emdao.buscar_por_id(id)
    if request.state.token['admin'] or id == request.state.token['laboratorio']: 
        dados = ldao.buscar_por_id(id)
    else:
        return HTTPException(404, "Permissões insuficientes")
    
    return {"API": {"URI": f"/api/laboratorio/{id}", "METHOD": "GET"}, "DATA": dados}

@router.get("/laboratorios")
def listar_laboratorios(request: Request):
    if request.state.token['admin']: 
        dados = ldao.listar_todos()
    else:
        dados = ldao.buscar_por_id(request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/laboratorios", "METHOD": "GET"}, "DATA": dados}

@router.post("/laboratorio")
async def inserir_laboratorio(request: Request):
    dados = await request.json()
    laboratorio = Laboratorio(None, **dados)
    return {"success": bool(ldao.inserir(laboratorio))}

@router.post("/laboratorio/atualizar")
async def atualizar_laboratorio(request: Request):
    dados = await request.json()
    laboratorio = Laboratorio(**dados)
    return {"success": bool(ldao.atualizar(laboratorio))}

@router.post("/laboratorio/atualizar/status")
async def atualizar_status_laboratorio(request: Request):
    dados = await request.json()
    return {"success": bool(ldao.atualizar_status(dados['id']))}

# Usuário
@router.get("/usuario/{id}")
def buscar_usuario(request: Request, id: int):
    if request.state.token['admin'] or id == request.state.token['id']: 
        dados = udao.buscar_por_id(id)
    else:
        return HTTPException(status_code=404, detail="Permissões insuficientes")
        
    return {"API": {"URI": f"/api/usuario/{id}", "METHOD": "GET"}, "DATA": dados}

@router.get("/usuarios")
def listar_usuarios(request: Request):
    if request.state.token['admin']: 
        dados = udao.listar_todos()
    else:
        dados = udao.listar_por_laboratorio(request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/usuarios", "METHOD": "GET"}, "DATA": dados}

@router.post("/usuario")
async def inserir_usuario(request: Request):
    dados = await request.json()
    usuario = Usuario(None, **dados)
    usuario.criptografa()
    return {"success": bool(udao.inserir(usuario))}

@router.post("/usuario/atualizar")
async def atualizar_usuario(request: Request):
    dados = await request.json()
    usuario = Usuario(**dados)
    return {"success": bool(udao.atualizar(usuario))}

@router.post("/usuario/atualizar/senha")
async def atualizar_usuario(request: Request):
    dados = await request.json()
    usuario = Usuario(dados['id'], '', '', dados['senha'])
    usuario.criptografa()
    return {"success": bool(udao.atualizar_senha(usuario))}

@router.post("/usuario/atualizar/status")
async def atualizar_status_usuario(request: Request):
    dados = await request.json()
    return {"success": bool(udao.atualizar_status(dados['id']))}


# Views
@router.get("/disponibilidade")
def buscar_disponibilidade():
    return {"API": {"URI": "/api/disponibilidade", "METHOD": "GET"}, "DATA": vdao.listar_disponibilidade()}

# Views
@router.get("/aviso")
def buscar_disponibilidade(request: Request):
    if request.state.token['admin']: 
        dados = vdao.avisos_certifiado()
    else: 
        dados = vdao.avisos_certifiado(request.state.token['laboratorio'])
        
    return {"API": {"URI": "/api/aviso", "METHOD": "GET"}, "DATA": dados}
