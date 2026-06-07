from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c.isdigit())

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}