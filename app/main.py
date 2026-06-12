from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'error': 'Invalid input'}, 400
    subprocess.run(['ping', host], check=True, text=True)
    return {"status": "completed"}