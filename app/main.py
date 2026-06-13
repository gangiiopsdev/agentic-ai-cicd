from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Regular expression to match potentially harmful characters
    if re.search(r'[;&|<>`]', host):
        return {'status': 'failed', 'error': 'Invalid input'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}