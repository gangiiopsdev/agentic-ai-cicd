from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate the input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'error', 'message': 'Invalid host name'}
    return ping(host)