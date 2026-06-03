from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e}'}
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}