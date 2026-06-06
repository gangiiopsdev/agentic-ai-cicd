from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.stderr}'