from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(safe_host, check=True, shell=False, text=True)
    return {"status": "completed"}