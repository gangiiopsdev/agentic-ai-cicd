from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using subprocess.run
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate the host input to ensure it does not contain malicious characters or commands
    if any(char in host for char in [';', '|', '&', '<', '>', '(', ')', '[', ']', '{', '}', '$', '`']):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)