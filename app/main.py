from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.run(["ping", f'"{host}"'], check=True)
    return {"status": "completed"}