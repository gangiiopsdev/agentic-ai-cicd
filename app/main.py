from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using subprocess.run to avoid shell injection
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Using the safe_ping function to avoid shell injection
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid input')
    output = safe_ping(host)
    return {"status": "completed", "output": output}