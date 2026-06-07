from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_str):
    if re.match(r'^[a-zA-Z0-9.-]+$', input_str) and '.' in input_str:
        return False
    return True

@app.get('/ping')
def ping(host: str):
    if not sanitize_input(host):\n        return {'status': 'error', 'output': 'Invalid host'}\n    result = subprocess.run(['ping', host], capture_output=True, text=True)\n    return {'status': 'completed', 'output': result.stdout}