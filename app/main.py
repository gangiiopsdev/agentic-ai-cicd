from fastapi import FastAPI
import subprocess
call = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = call.stdout if call.returncode == 0 else call.stderr
    return {'status': 'completed', 'result': result}