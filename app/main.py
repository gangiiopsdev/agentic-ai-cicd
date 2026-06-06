from fastapi import FastAPI
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters or patterns
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)