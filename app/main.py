from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return shlex.quote(host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        escaped_host = escape_host(host)
        output = subprocess.check_output(['ping', escaped_host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}