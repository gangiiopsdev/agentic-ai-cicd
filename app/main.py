from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate the host input
        if not all(c.isalnum() or c in '.-' for c in host):
            return {'status': 'failed', 'error': 'Invalid host'}
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}