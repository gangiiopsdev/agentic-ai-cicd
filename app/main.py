from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safer implementation using subprocess.run to avoid shell=True and partial paths
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}