from fastapi import FastAPI
import subprocess
def safe_ping(host):
    valid_hosts = ["example.com", "localhost"]
    if host in valid_hosts:
        try:
            result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "message": str(e)}
    else:
        return {"status": "error", "message": "Invalid host"}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)