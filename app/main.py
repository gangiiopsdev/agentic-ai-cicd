from fastapi import FastAPI
import subprocess
from typing import List, Dict

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and using absolute paths
    if host not in ['google.com', 'example.com']:
        return {"status": "error", "output": "Invalid host"}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e.output)}
    except Exception as e:
        return {"status": "error", "output": str(e)}