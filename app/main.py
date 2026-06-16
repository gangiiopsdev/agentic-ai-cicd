from fastapi import FastAPI
import subprocess
def safe_subprocess(command, args):
    return subprocess.run([command] + list(args), check=True)

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_subprocess("ping", [host])
    return {"status": "completed"}