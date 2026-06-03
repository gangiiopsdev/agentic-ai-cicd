from fastapi import FastAPI
import subprocess
trom typing import Union

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent Command Injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        output = subprocess.run(['ping', '-c', '1', f'"{host}"'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}