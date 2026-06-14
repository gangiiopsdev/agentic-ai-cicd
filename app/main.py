from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host to ensure it does not contain any unexpected characters or patterns that could be used for injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'error': 'Invalid input'}, 400
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}