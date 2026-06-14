from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        return {'status': 'failed', 'error': 'Host parameter is empty'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': jsonable_encoder(e.stderr)}

# Preventive Controls:
# 1. Validate and sanitize input to ensure it does not contain malicious content.
# 2. Use full path for the executable (e.g., '/bin/ping') if possible.
# 3. Avoid using shell=True in subprocess calls unless absolutely necessary and thoroughly validate any user inputs.