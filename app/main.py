from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host to ensure it only contains expected characters
    if not all(char.isalnum() or char in '.-_' for char in host):
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}