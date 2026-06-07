from fastapi import FastAPI
import subprocess
cimport = ['ping']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    safe_host = subprocess.shlex_quote(host)
    subprocess.run(cimport + [safe_host], check=True)
    return {'status': 'completed'}