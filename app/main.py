from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host):
    return bool(re.match(r'^[a-zA-Z0-9-.@_]+$', host))

@app.get('/ping')
def ping(host: str):\n    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid input'}\n    args = ['ping', host]\n    result = subprocess.run(args, capture_output=True, text=True)\n    return {'status': 'completed', 'output': result.stdout}