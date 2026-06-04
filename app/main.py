from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host to ensure it's a safe hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    # Safe implementation using subprocess.run with shell=False and check=True
    subprocess.run(['ping', host], check=True, shell=False)

@app.get('/ping')
def ping(host: str):
    try:
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}