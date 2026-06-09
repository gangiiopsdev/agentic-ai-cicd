from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if isinstance(host, str) and host.strip():
        subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    if isinstance(host, str) and host.strip():
        subprocess.run(args, check=True)
    return {"status": "completed"}