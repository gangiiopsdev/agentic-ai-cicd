from fastapi import FastAPI
import subprocess
def safe_subprocess(command: str):
    import shlex
    args = shlex.split(command)
    return args

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')  # Basic input sanitization
    command = f'ping {safe_host}'
    args = safe_subprocess(command)
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}