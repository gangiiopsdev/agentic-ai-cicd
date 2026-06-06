from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize host input
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(["ping", host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output}