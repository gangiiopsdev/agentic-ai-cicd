from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(e for e in host if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}