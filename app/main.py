from fastapi import FastAPI
import subprocess
class MyDependency:
    async def __call__(self):
        return {'message': 'Agentic Self-Healing Pipeline'}

app = FastAPI()

@app.get('/')
def home(deps: dict = Depends(MyDependency)):
    return deps['message']

@app.get('/ping')
def ping(host: str):