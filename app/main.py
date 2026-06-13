from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if not host or len(host) > 255:
        return {'status': 'invalid', 'message': 'Invalid host name'}
    return secure_ping(host)