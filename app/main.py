from fastapi import FastAPI
import subprocess
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}