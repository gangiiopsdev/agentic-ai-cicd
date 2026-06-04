from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = subprocess.quote(host)
    try:
        output = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'