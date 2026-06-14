from fastapi import FastAPI, HTTPException
import subprocess from typing import Dict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str) -> Dict[str, str]:
    # Validate the host input to prevent shell injection
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.\.[0-9]{1,3}\.\.[0-9]{1,3}$', host) or len(host.split('.')) != 4:
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except TimeoutExpired:
        return {"status": "timeout", "message": "Ping request timed out"}