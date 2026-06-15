from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Dict

app = FastAPI()

def safe_ping(host: str) -> Dict[str, str]:
    try:
        result = subprocess.run(['ping', '-c 1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.__str__()}

@app.get('/ping')
def ping(host: str) -> Dict[str, str]:
    return safe_ping(host)