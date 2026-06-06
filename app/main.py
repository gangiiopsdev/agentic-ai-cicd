from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = sp.check_output(['ping', host], stderr=sp.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}