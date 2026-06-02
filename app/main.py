from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    # Validate input using regex to allow only alphanumeric characters and specific special characters
    if re.match(r'^[a-zA-Z0-9.-_]*$', host):
        try:
            args = ['ping', host]
            subprocess.run(args, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        return {'error': 'Invalid input'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)