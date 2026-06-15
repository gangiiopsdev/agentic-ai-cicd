from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use a list to pass arguments safely
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    return safe_ping(host)