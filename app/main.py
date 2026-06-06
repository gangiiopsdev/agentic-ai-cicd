from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    if host.replace('.', '').isdigit():
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)