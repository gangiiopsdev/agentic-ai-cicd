from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Validate the host input to prevent command injection
        if not all(c.isalnum() or c in '.-\' for c in host):
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "output": response}