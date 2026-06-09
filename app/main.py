from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "message": "Invalid host"}
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    except Exception as e:
        return {"status": "error", "message": str(e)}