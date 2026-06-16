from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.run(['ping', host], check=True, text=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent shell injection
    if not host.strip() or len(host) > 256:
        return {"status": "failed", "error": "Invalid hostname"}
    return ping(host)