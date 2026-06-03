from fastapi import FastAPI
import subprocess
g-import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, shell=False)
    
    return {"status": "completed"}