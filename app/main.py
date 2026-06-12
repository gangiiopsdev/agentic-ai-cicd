from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder
def ping(host: str):
    try:
        # Validate and sanitize host input
        if not host.isalnum() or '@' in host:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return jsonable_encoder({'error': str(e)})
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize host input
        if not host.isalnum() or '@' in host:
            raise ValueError('Invalid host format')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return jsonable_encoder({'error': str(e)})
    return {"status": "completed"}