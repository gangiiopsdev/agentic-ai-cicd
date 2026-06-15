from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host != 'localhost':
        return {"status": "invalid host"}
    args = ["ping", host]
    subprocess.run(args, check=True)
    return {"status": "completed"}