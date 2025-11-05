from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from .users import auth_router, user_router
from .config import settings

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)

app.include_router(auth_router)
app.include_router(user_router)

# я так понимаю на стартовой странице отображаются ссылки на документацию,
# чтобы разработчики не вводили вручную в адресной строке, удобно)
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <a href="http://127.0.0.1:8000/docs">Documentation</a><br>
    <a href="http://127.0.0.1:8000/redoc">ReDoc</a>
    """

# нет вызова main
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
