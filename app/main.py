from fastapi import FastAPI
import subprocess
gimport shlex
gimport subprocess
g
app = FastAPI()

g@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

g@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = shlex.split(f'ping {host}')
    subprocess.run(command, check=True)
    return {"status": "completed"}