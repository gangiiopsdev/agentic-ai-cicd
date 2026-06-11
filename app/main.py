from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.replace('.', '').isnumeric() or len(host.split('.')) != 4:
        return {'status': 'error', 'message': 'Invalid host'}

    result = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True)
    return {'status': 'completed', 'output': jsonable_encoder(result.stdout)}