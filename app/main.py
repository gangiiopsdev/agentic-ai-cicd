from fastapi import FastAPI
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None or ':' not in host:
        return {'error': 'Invalid host'}
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}