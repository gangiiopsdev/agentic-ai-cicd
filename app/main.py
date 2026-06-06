from fastapi import FastAPI
import subprocess
global_popen = subprocess.Popen

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    global_popen(f'ping {host}', shell=False)

    return {"status": "completed"}