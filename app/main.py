from fastapi import FastAPI
import subprocess
import shlex
c
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run to safely escape the input and avoid shell=True
    result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}