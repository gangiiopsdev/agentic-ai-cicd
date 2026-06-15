from fastapi import FastAPI
import subprocess
generics = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    result = generics.stdout if generics.returncode == 0 else 'Failed to ping'
    return {'status': result}