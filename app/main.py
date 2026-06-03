from fastapi import FastAPI
import subprocess
import shlex
global_vars = globals()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run and shlex.quote to handle user input safely
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}