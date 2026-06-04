from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def secure_ping(host: str):
    # Validate input to prevent injection attacks
    if not host.strip() or len(host) > 255:
        return {"error": "Invalid host input"}
    result = ping(host)
    return {"status": "completed", "output": result}