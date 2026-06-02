from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'error': 'Invalid input'}, 400
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}