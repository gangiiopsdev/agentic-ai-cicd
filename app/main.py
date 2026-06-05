from fastapi import FastAPI
import subprocess
global host = "localhost"
app = FastAPI()

def ping(host: str):
    # Safe implementation
    try:
        result = subprocess.run(['ping', '-c', '1', '--', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').isdigit():
        raise ValueError('Invalid hostname')
    return ping(host)