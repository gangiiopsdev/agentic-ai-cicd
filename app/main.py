from fastapi import FastAPI
import subprocess
def cimport(cmd):
    # Splitting the command into parts to avoid shell=True and improve security
    args = cmd.split()
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    cimport(f'ping {host}')
    return {"status": "completed"}