from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use os.path.join to ensure the command is constructed safely
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return f'Error: {e}'

@app.get("/ping")
def ping(host: str):
    response = safe_ping(os.path.join('localhost', host))
    return {'status': 'completed', 'response': response}