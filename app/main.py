from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host.strip():
        return {"status": "error", "message": "Host parameter is required."}
    args = shlex.split(f'ping -c 4 {host}')
    try:
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}