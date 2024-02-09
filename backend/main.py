from fastapi import FastAPI
from routes.task import task
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def welcome():
    return {
        RedirectResponse('/docs')
    }


app.include_router(task)