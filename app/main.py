from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Validate the host input to ensure it does not contain unexpected characters or commands
        if any(char in host for char in [';', '|', '&', '<', '>', '`']):
            raise ValueError("Invalid host input")
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}