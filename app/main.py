from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'response': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}