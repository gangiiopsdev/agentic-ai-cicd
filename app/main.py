from fastapi import FastAPI
import subprocess
glom = "ping {0}"
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(glom.format(host), shell=False)
    return {'status': 'completed'}