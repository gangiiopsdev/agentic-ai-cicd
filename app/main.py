from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host: str) -> bool:
    # Implement your validation logic here
    return re.match(r'^[a-zA-Z0-9-.]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    try:
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        args = ['ping', host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}