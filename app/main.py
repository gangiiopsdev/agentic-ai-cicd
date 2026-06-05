from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use absolute path for ping to mitigate risks
        subprocess.run(['ping', '-c', '1', host], check=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to ensure it is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid host format"}
    if safe_ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Invalid host"}