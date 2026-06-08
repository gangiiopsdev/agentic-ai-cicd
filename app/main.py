from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        sanitized_host = host.strip()
        if ' ' in sanitized_host or ';' in sanitized_host:
            return {'status': 'failed', 'error': 'Invalid input'}
        subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}