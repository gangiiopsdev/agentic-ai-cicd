from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Ensure the host input does not contain dangerous characters or patterns.
    if any(char in host for char in [';', '&', '|', '>', '<', '`']):
        return {'error': 'Invalid input'}, 400
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}