from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host to ensure it's a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}