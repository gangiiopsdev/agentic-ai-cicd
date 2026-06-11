from fastapi import FastAPI
import subprocess
cimport = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = cimport.stdout if cimport.returncode == 0 else cimport.stderr
    return {'status': 'completed', 'result': result}