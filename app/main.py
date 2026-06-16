from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to allow only valid IP addresses or domain names
    import re
    if not re.match(r'^([0-9]{1,3}\.[0-9]{1,3}\.){2}[0-9]{1,3}$|^(([a-zA-Z0-9]([-a-zA-Z0-9]*[a-zA-Z0-9])?)\.)+[a-zA-Z]{2,})$', host):
        return {"status": "failed", "error": "Invalid host"}
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}