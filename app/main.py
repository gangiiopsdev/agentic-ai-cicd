from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or ' ' in host:
        raise ValueError('Invalid hostname')
    command = ['ping', '-c 1', f'"{host}"']  # Escape the user input to prevent command injection
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}