from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from middleware import verificar_token
from routes import router

app = FastAPI()

@app.middleware("http")
async def middleware_autenticacao(request: Request, call_next):
    if request.url.path not in ["/api/login"]:
        try:
            request.state.token = verificar_token(request.headers.get("Authorization"))
        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"success": True if e.status_code == 200 else False, "message": e.detail})
    response = await call_next(request)
    return response

app.include_router(router, prefix="/api")
