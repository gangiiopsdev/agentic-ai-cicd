from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and sanitization
    if host.isalnum() and len(host) <= 255:
        try:
            result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': e.stderr}
    else:
        raise ValueError('Invalid input for host')