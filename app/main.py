from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    allowed_hosts: List[str] = ["example.com", "test.com"]
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], check=True, text=True, capture_output=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}