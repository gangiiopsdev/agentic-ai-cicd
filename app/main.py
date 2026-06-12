from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    return subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '&&' in host or ';' in host:
        return {"error": "Invalid input"}, 400
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}