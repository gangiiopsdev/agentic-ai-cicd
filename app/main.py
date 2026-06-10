from fastapi import FastAPI
import subprocess

def escape_host(host):
    return host.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        output = subprocess.run(['ping', f'-c 1 {safe_host}'], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}