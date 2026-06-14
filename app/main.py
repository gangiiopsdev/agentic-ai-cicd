from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    try:
        # Enhanced input validation to prevent command injection
        if not re.match(r'^[a-zA-Z0-9-.]+$', host):
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except ValueError as ve:
        return {"status": "failed", "error": str(ve)}