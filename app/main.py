from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError("Invalid hostname")
    return subprocess.call(['ping', host])

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {
            "status": result.returncode,
            "output": result.stdout if result.returncode == 0 else result.stderr
        }
    except ValueError as e:
        return {"error": str(e), "status": "failed"}