from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host input to ensure it's a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host format'}
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}