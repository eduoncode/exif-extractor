from fastapi import FastAPI
from app.routes.routes import router  # importa as rotas definidas

app = FastAPI()
app.include_router(router)
