from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    return ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.run(safe_ping(host), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Secure fix
def safe_ping(host: str):
    if '&&' in host or ';' in host or '|' in host or '`' in host:
        raise ValueError("Unsafe input detected")
    return ['ping', host]

@app.get("/secure-ping")
def secure_ping(host: str):
    try:
        output = subprocess.run(safe_ping(host), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}