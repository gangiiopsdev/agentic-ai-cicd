from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Validate and sanitize the host input to prevent shell injection
        if not all(c.isalnum() or c in '-.' for c in host):
            return 'Invalid hostname'
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return e.stderr.decode()

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)