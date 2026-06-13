from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return {"status": "error", "output": "Invalid input"}
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}