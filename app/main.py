from fastapi import FastAPI
import subprocess
from urllib.parse import quote_plus

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', quote_plus(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}