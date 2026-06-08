from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Safe implementation using subprocess.run with input validation
        if host.isalnum() or '.' in host:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        else:
            raise ValueError("Invalid hostname")
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}