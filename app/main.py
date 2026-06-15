from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    return all(c.isalnum() or c in '._-' for c in host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host) or ' ' in host:
        return {"status": "failed", "error": "Invalid host input"}

    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}