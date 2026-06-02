from fastapi import FastAPI
import subprocess
call = subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    result = call.wait()
    return {'status': 'completed' if result == 0 else 'failed'}