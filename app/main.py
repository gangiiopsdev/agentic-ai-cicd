from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(str.isalnum, input_str))

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)\n    try:\n        output = subprocess.check_output(['ping', sanitized_host], universal_newlines=True, timeout=5)\n        return {"status": "completed", "output": output}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}\n    except TimeoutExpired:\n        return {"status": "failed", "error": "Command timed out"}