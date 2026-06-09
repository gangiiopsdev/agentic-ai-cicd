from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.isalnum() or '-' in host:
        result = subprocess.run(shlex.split(f"ping {host}"), capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "error": "Invalid host input"}