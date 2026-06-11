from fastapi import FastAPI
import subprocess
gt_from typing import List, Dict

app = FastAPI()

def ping(host: str) -> Dict[str, str]:
    if not host or not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str) -> Dict[str, str]:
    return ping(host)