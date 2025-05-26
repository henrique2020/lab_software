from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from middleware import verificar_token_bearer
from routes import router

app = FastAPI()

@app.middleware("http")
async def middleware_autenticacao(request: Request, call_next):
    if request.url.path not in ["/api/login"]:
        verificar_token_bearer(request)
    response = await call_next(request)
    return response

app.include_router(router, prefix="/api")
