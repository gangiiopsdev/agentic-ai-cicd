from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_handler(host: str):
    # Validate host input to ensure it does not contain unexpected characters
    if not host.strip().replace('.', '').isalnum():
        raise ValueError('Invalid host input')
    return ping(host)